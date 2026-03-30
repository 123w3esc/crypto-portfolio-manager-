import pandas as pd
from datetime import datetime

def save_reports(risk_report, predictions):

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    risk_file = f"risk_report_{timestamp}.csv"
    pred_file = f"prediction_report_{timestamp}.csv"

    risk_report.to_csv(risk_file, index=False)
    predictions.to_csv(pred_file, index=False)

    print(f"📄 Risk report saved: {risk_file}")
    print(f"📄 Prediction report saved: {pred_file}")

    return risk_file, pred_file