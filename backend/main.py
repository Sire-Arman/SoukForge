from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from services.data_collection.collector import MarketDataCollector
from ml_models.sentiment_trainer import MarketSentimentAnalyzer

app = FastAPI()

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ProductAnalysisRequest(BaseModel):
    product_name: str

data_collector = MarketDataCollector()
sentiment_analyzer = MarketSentimentAnalyzer()

@app.post("/analyze")
async def analyze_product(request: ProductAnalysisRequest):
    # Collect data
    raw_data = data_collector.collect_data(request.product_name)
    
    # Analyze sentiment
    sentiment_results = sentiment_analyzer.analyze(raw_data)
    
    return {
        "product": request.product_name,
        "sentiment_analysis": sentiment_results
    }