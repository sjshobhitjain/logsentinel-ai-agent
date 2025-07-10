from sklearn.ensemble import IsolationForest

class LogAnomalyModel:
    def __init__(self):
        self.model = IsolationForest(contamination=0.1, random_state=42)

    def train(self, X):
        self.model.fit(X)

    def predict(self, X):
        return self.model.predict(X)
