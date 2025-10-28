from sklearn.metrics import accuracy_score, precision_recall_fscore_support # Correct import name

def calculate_classification_metrics(y_true, y_pred):
    """
    Calcula e imprime as métricas de desempenho para classificação.
    """
    accuracy = accuracy_score(y_true, y_pred)
    precision, recall, f1, _ = precision_recall_fscore_support(y_true, y_pred, average='weighted')

    print(f"Acurácia: {accuracy:.4f}")
    print(f"Precisão: {precision:.4f}")
    print(f"Recall:   {recall:.4f}")
    print(f"F1-Score: {f1:.4f}")

    return {"accuracy": accuracy, "precision": precision, "recall": recall, "f1_score": f1}