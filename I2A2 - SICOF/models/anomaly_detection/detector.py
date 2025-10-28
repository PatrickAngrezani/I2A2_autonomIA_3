import pandas as pd
import joblib
from sklearn.ensemble import IsolationForest
from sklearn.pipeline import Pipeline
from preprocessing.pipelines import get_preprocessing_pipeline

MODEL_PATH = 'models/saved_models/anomaly_detector.joblib'

def train_anomaly_detector(X: pd.DataFrame):
    print("Iniciando treinamento do detector de anomalias.")
    
    preprocessor = get_preprocessing_pipeline()
    
    model_pipeline = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('detector', IsolationForest(contamination=0.05, random_state=42)) 
    ])
    
    model_pipeline.fit(X)
    
    joblib.dump(model_pipeline, MODEL_PATH)
    print(f"Detector de anomalias salvo em: {MODEL_PATH}")
    return model_pipeline

def load_anomaly_detector() -> Pipeline:
    """Carrega o detector de anomalias do disco."""
    try:
        model = joblib.load(MODEL_PATH)
        return model
    except FileNotFoundError:
        print(f"Erro: Modelo não encontrado em {MODEL_PATH}. Execute o treinamento primeiro.")
        return None

def predict_anomalies(X: pd.DataFrame) -> pd.Series:
    """
    Carrega o detector e prevê anomalias.
    Retorna -1 para anomalias, 1 para dados normais.
    """
    model = load_anomaly_detector()
    if model:
        # decision_function retorna o "score" de anomalia
        anomaly_scores = model.decision_function(X) 
        # predict retorna -1 (anomalia) ou 1 (normal)
        predictions = model.predict(X)
        return predictions, anomaly_scores
    return None, None