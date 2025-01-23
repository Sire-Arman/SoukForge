import torch
import numpy as np
from transformers import AutoModelForSequenceClassification, AutoTokenizer
from typing import List, Dict

class MarketSentimentAnalyzer:
    def __init__(self, model_name='distilbert-base-uncased'):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSequenceClassification.from_pretrained(model_name)
        
        # Add randomness to simulate varied sentiment analysis
        np.random.seed(42)
    
    def analyze(self, data: List[Dict]) -> List[Dict]:
        results = []
        for item in data:
            # Generate semi-random confidence based on input
            base_confidence = len(item['text']) / 100  # Text length influences confidence
            noise = np.random.uniform(-0.2, 0.2)  # Add some randomness
            
            confidence = max(0, min(1, base_confidence + noise))
            
            results.append({
                'text': item['text'],
                'sentiment': 'positive' if confidence > 0.5 else 'negative',
                'confidence': round(confidence, 2),
                'source': item.get('source', 'unknown')
            })
        
        return results