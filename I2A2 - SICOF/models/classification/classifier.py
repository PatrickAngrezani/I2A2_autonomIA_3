import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from preprocessing.pipelines import get_preprocessing_pipeline

# local para salvar o modelo treinado
MODEL_PATH = 'models/saved_models/fiscal_classifier.joblib'

def train_classifier(X: pd.DataFrame, y: pd.Series):    
    preprocessor = get_preprocessing_pipeline()
    
    model_pipeline = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('classifier', RandomForestClassifier(n_estimators=100, random_state=42))
    ])
    
    # Treina o modelo
    model_pipeline.fit(X, y)
    
    # Salva o pipeline completo
    joblib.dump(model_pipeline, MODEL_PATH)
    print(f"Classificador salvo em: {MODEL_PATH}")
    return model_pipeline

def load_classifier() -> Pipeline:
    try:
        model = joblib.load(MODEL_PATH)
        return model
    except FileNotFoundError:
        print(f"Erro: Modelo não encontrado em {MODEL_PATH}. Execute o treinamento primeiro.")
        return None

def predict_classification(X: pd.DataFrame) -> (pd.Series, pd.DataFrame):
    """
    Carrega o modelo treinado e faz predições.
    X deve ser um DataFrame com os dados brutos.
    """
    model = load_classifier()
    if model:
        predictions = model.predict(X)
        probabilities = model.predict_proba(X)
        return predictions, probabilities
    return None, None