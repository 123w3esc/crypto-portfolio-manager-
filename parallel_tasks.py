from concurrent.futures import ThreadPoolExecutor
import risk_checker
import prediction_engine

def run_parallel_tasks():

    with ThreadPoolExecutor(max_workers=2) as executor:

        risk_future = executor.submit(risk_checker.generate_risk_report)
        prediction_future = executor.submit(prediction_engine.predict_next_day)

        risk_report = risk_future.result()
        predictions = prediction_future.result()

    return risk_report, predictions
