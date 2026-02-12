import pandas as pd
from datetime import datetime


def load_schemes(path="data/schemes.csv"):
    """
    Loads the schemes dataset from CSV.
    """
    return pd.read_csv(path)


def calculate_score(user, scheme):
    score = 0
    reasons = []

    # Income Match (40 points)
    if scheme["min_income"] <= user["income"] <= scheme["max_income"]:
        score += 40
        reasons.append("Income criteria matched")

    # State Match (30 points)
    if scheme["state"] == "All" or scheme["state"] == user["state"]:
        score += 30
        reasons.append("State criteria matched")

    # Category Match (20 points)
    if scheme["category"] == "All" or scheme["category"] == user["category"]:
        score += 20
        reasons.append("Category criteria matched")

    # Age Match (10 points)
    if scheme["min_age"] <= user["age"] <= scheme["max_age"]:
        score += 10
        reasons.append("Age criteria matched")

    return score, reasons


def classify(score):
    if score >= 80:
        return "Highly Eligible"
    elif score >= 50:
        return "Potentially Eligible"
    else:
        return "Not Eligible"


def check_deadline_alert(deadline_str):
    today = datetime.today()
    deadline = datetime.strptime(deadline_str, "%Y-%m-%d")
    days_left = (deadline - today).days

    if days_left < 0:
        return "Deadline Passed"
    elif days_left <= 30:
        return f"⚠ Deadline approaching in {days_left} days"
    else:
        return f"{days_left} days remaining"


def recommend_schemes(user, path="data/schemes.csv"):
    df = load_schemes(path)
    recommendations = []

    for _, scheme in df.iterrows():
        score, reasons = calculate_score(user, scheme)

        recommendations.append({
            "scheme_name": scheme["scheme_name"],
            "score": score,
            "status": classify(score),
            "reasons": ", ".join(reasons),
            "benefits": scheme["benefits"],
            "documents": scheme["documents"],
            "deadline": scheme["deadline"],
            "alert": check_deadline_alert(scheme["deadline"])
        })

    rec_df = pd.DataFrame(recommendations)
    rec_df = rec_df.sort_values(by="score", ascending=False)

    return rec_df
