from fastapi import FastAPI, HTTPException
from schemas import PerformanceVarianceRequest, PerformanceVarianceResponse
from services import calculate_performance_variance
from utils import validate_variance_request

app = FastAPI(
    title="All-Rounder Analytics - Performance Variance Model API",
    description="Evaluates skill-wise dispersion and joint stability across batting and bowling disciplines.",
    version="1.0.0"
)

@app.get("/health", tags=["Health Check"])
def health_check():
    return {"status": "ok", "service": "Performance Variance Model API"}

@app.post("/analytics/performance-variance", response_model=PerformanceVarianceResponse, tags=["Analytics"])
def analyze_performance_variance(payload: PerformanceVarianceRequest):
    try:
        validate_variance_request(payload)
        return calculate_performance_variance(payload)
    except HTTPException as http_ex:
        raise http_ex
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")
