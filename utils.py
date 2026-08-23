from fastapi import HTTPException
from schemas import PerformanceVarianceRequest

def validate_variance_request(payload: PerformanceVarianceRequest):
    if len(payload.match_logs) < 5:
        raise HTTPException(
            status_code=400,
            detail="At least 5 match logs are required to calculate meaningful statistical variance."
        )
