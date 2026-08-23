from pydantic import BaseModel, Field
from typing import List

class MatchRoleLog(BaseModel):
    match_id: str = Field(..., description="Unique match identifier")
    batting_impact: float = Field(..., ge=0.0, le=100.0, description="Batting impact score (0 to 100)")
    bowling_impact: float = Field(..., ge=0.0, le=100.0, description="Bowling impact score (0 to 100)")

class PerformanceVarianceRequest(BaseModel):
    player_id: str = Field(..., description="Unique ID of the player")
    player_name: str = Field(..., description="Name of the player")
    match_logs: List[MatchRoleLog] = Field(..., min_items=5, description="List of match performance logs (min 5)")

class PerformanceVarianceResponse(BaseModel):
    player_id: str
    player_name: str
    sample_size: int
    cv_batting: float
    cv_bowling: float
    joint_volatility_index: float
    overall_stability_score: float
    role_stability_grade: str
    analytical_summary: str
