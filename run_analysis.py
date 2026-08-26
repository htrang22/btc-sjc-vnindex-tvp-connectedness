from pathlib import Path

from tvp_connectedness import (
    compare_specifications,
    load_volatility_data,
    run_specification,
    save_comparison,
    save_results,
)


ROOT = Path(__file__).resolve().parent
data = load_volatility_data(ROOT / "data/model2_conditional_volatility.csv")

specifications = [
    {
        "name": "baseline_0999",
        "lambda_beta": 0.999,
        "kappa_sigma": 0.96,
        "horizon": 10,
    },
    {
        "name": "robustness_0997",
        "lambda_beta": 0.997,
        "kappa_sigma": 0.96,
        "horizon": 10,
    },
    {
        "name": "kappa_094",
        "lambda_beta": 0.999,
        "kappa_sigma": 0.94,
        "horizon": 10,
    },
    {
        "name": "kappa_098",
        "lambda_beta": 0.999,
        "kappa_sigma": 0.98,
        "horizon": 10,
    },
    {
        "name": "horizon_05",
        "lambda_beta": 0.999,
        "kappa_sigma": 0.96,
        "horizon": 5,
    },
    {
        "name": "horizon_20",
        "lambda_beta": 0.999,
        "kappa_sigma": 0.96,
        "horizon": 20,
    },
]

results = [
    run_specification(data, initial_covariance=0.01, **specification)
    for specification in specifications
]

for result in results:
    save_results(result, ROOT / "outputs" / result.name)

save_comparison(results, ROOT / "outputs/specification_comparison.csv")
comparison = compare_specifications(results)
comparison.to_csv(ROOT / "outputs/specification_comparison.csv")

print(comparison.round(4).to_string())

baseline = results[0]
unstable_tci = baseline.connectedness.tci.loc[~baseline.stability["stable"]]
stable_tci = baseline.connectedness.tci.loc[baseline.stability["stable"]]
print("\nBaseline local-instability context")
print(f"Unstable observations: {len(unstable_tci)}")
print(f"Unstable episodes: {len(baseline.episodes)}")
print(f"Mean TCI, unstable dates: {unstable_tci.mean():.4f}%")
print(f"Mean TCI, stable dates: {stable_tci.mean():.4f}%")
print(baseline.episodes.to_string(index=False))
