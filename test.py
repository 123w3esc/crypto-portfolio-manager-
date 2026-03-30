import parallel_risk
import invest_mix_cal
import parallel_tasks
import report_generator
import email_alearts

def main():

    print("Computing Risk Metrics...")
    metrics = parallel_risk.compute_all_metrics()

    print("Allocating Portfolio...")
    allocation = invest_mix_cal.allocate_portfolio(
        metrics,
        total_investment=100000,
        profile="Medium"
    )

    for a in allocation:
        print(a)

    print("Running Parallel Risk + Prediction...")

    risk_report, predictions = parallel_tasks.run_parallel_tasks()

    print("\n--- Predictions ---")
    print(predictions)

    risk_file, pred_file = report_generator.save_reports(risk_report, predictions)

    email_alearts.send_report_link(risk_file)

if __name__ == "__main__":
    main()