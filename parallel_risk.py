from concurrent.futures import ThreadPoolExecutor, as_completed
import risk_engine

def compute_all_metrics():

    data = risk_engine.load_data()
    results = []

    with ThreadPoolExecutor(max_workers=5) as executor:

        future_to_coin = {
            executor.submit(risk_engine.get_coin_metrics, coin_id, prices): coin_id
            for coin_id, prices in data.items()
        }

        for future in as_completed(future_to_coin):
            coin = future_to_coin[future]
            try:
                result = future.result()
                results.append(result)
            except Exception as e:
                print(f"Error processing {coin}: {e}")

    return results