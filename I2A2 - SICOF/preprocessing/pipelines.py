import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.feature_extraction.text import TfidfVectorizer

def get_preprocessing_pipeline() -> ColumnTransformer:
    """
    Cria um pipeline de pré-processamento para os dados fiscais.
    """
    
    # Define as colunas para cada tipo de transformação
    
    # Colunas numéricas: imputa valores faltantes (média) e aplica escala
    numeric_features = ['valor_total_nf', 'valor_icms']
    numeric_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='median')),
        ('scaler', StandardScaler())
    ])

    # Colunas categóricas: imputa valores (constante 'missing') e aplica One-Hot Encoding
    categorical_features = ['cfop', 'ncm']
    categorical_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
        ('onehot', OneHotEncoder(handle_unknown='ignore'))
    ])

    # Coluna de texto (descrição): aplica TF-IDF
    text_features = 'descricao_item'
    text_transformer = Pipeline(steps=[
        ('tfidf', TfidfVectorizer(max_features=100)) # Limita a 100 features por simplicidade
    ])

    # Combina todos os transformadores em um único ColumnTransformer
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numeric_transformer, numeric_features),
            ('cat', categorical_transformer, categorical_features),
            ('txt', text_transformer, text_features)
        ],
        remainder='passthrough' # Mantém colunas não listadas (ex: CNPJs)
    )

    return preprocessor