import math
from schemas import PerformanceVarianceRequest, PerformanceVarianceResponse

def calculate_performance_variance(payload: PerformanceVarianceRequest) -> PerformanceVarianceResponse:
    n = len(payload.match_logs)
    
    bat_scores = [m.batting_impact for m in payload.match_logs]
    bowl_scores = [m.bowling_impact for m in payload.match_logs]

    mean_bat = sum(bat_scores) / n
    mean_bowl = sum(bowl_scores) / n

    var_bat = sum((x - mean_bat) ** 2 for x in bat_scores) / (n - 1) if n > 1 else 0.0
    var_bowl = sum((y - mean_bowl) ** 2 for y in bowl_scores) / (n - 1) if n > 1 else 0.0

    std_bat = math.sqrt(var_bat)
    std_bowl = math.sqrt(var_bowl)

    cv_bat = (std_bat / mean_bat * 100.0) if mean_bat > 0 else 100.0
    cv_bowl = (std_bowl / mean_bowl * 100.0) if mean_bowl > 0 else 100.0

    jvi = math.sqrt(cv_bat ** 2 + cv_bowl ** 2)
    stability_score = round(max(0.0, 100.0 - (jvi * 0.75)), 2)

    # Categorical Classification
    bat_stable = cv_bat < 35.0
    bowl_stable = cv_bowl < 35.0

    if bat_stable and bowl_stable:
        grade = "Dual-Role Anchor"
        summary = f"{payload.player_name} demonstrates high consistency across both batting and bowling, providing dependable dual-discipline value."
    elif bat_stable and not bowl_stable:
        grade = "Stable Bat / Volatile Bowl"
        summary = f"{payload.player_name} offers steady, predictable batting returns but experiences high match-to-match variance in bowling output."
    elif not bat_stable and bowl_stable:
        grade = "Volatile Bat / Stable Bowl"
        summary = f"{payload.player_name} maintains reliable bowling control while exhibiting boom-or-bust fluctuation in batting output."
    else:
        grade = "High-Variance Wildcard"
        summary = f"{payload.player_name} shows significant outcome dispersion in both roles, functioning as a high-risk, high-reward match participant."

    return PerformanceVarianceResponse(
        player_id=payload.player_id,
        player_name=payload.player_name,
        sample_size=n,
        cv_batting=round(cv_bat, 2),
        cv_bowling=round(cv_bowl, 2),
        joint_volatility_index=round(jvi, 2),
        overall_stability_score=stability_score,
        role_stability_grade=grade,
        analytical_summary=summary
    )
