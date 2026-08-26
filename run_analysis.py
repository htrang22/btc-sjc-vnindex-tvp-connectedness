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

baseline = run_specification(
    data,
    name="baseline_0999",
    lambda_beta=0.999,
    kappa_sigma=0.96,
    horizon=10,
)
robustness = run_specification(
    data,
    name="robustness_0997",
    lambda_beta=0.997,
    kappa_sigma=0.96,
    horizon=10,
)

results = [baseline, robustness]
save_results(baseline, ROOT / "outputs/baseline_0999")
save_results(robustness, ROOT / "outputs/robustness_0997")
save_comparison(results, ROOT / "outputs/specification_comparison.csv")

print(compare_specifications(results).round(4).to_string())
