import numpy as np
import joblib
from tensorflow.keras.models import load_model
from concurrent.futures import ThreadPoolExecutor

class PredictionEngine:
    def __init__(self):
        self.models = {
            'rf': joblib.load('models/rf_model.pkl'),
            'lstm': load_model('models/lstm_model.h5')
        }
        self.executor = ThreadPoolExecutor(max_workers=4)

    async def predict(self, data):
        predictions = []
        with self.executor as pool:
            futures = {pool.submit(model.predict, data): name for name, model in self.models.items()}
            for future in futures:
                predictions.append(future.result())
        return np.mean(predictions, axis=0)
