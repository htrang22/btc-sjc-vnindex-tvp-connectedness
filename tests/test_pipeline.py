from pathlib import Path
import unittest

import numpy as np

from tvp_connectedness import load_volatility_data, run_specification


ROOT = Path(__file__).resolve().parents[1]


class PipelineRegressionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = load_volatility_data(
            ROOT / "data/model2_conditional_volatility.csv"
        )

    def test_baseline_reproduces_submitted_notebook_results(self):
        result = run_specification(
            self.data,
            name="baseline",
            lambda_beta=0.999,
            kappa_sigma=0.96,
            horizon=10,
        )

        self.assertEqual(len(result.stability), 747)
        self.assertEqual(int((~result.stability["stable"]).sum()), 14)
        self.assertTrue(
            np.isclose(result.connectedness.tci.mean(), 7.92412042378382)
        )
        self.assertTrue(
            np.isclose(result.connectedness.tci.iloc[-1], 2.2449, atol=5e-5)
        )
        np.testing.assert_allclose(
            result.connectedness.net.mean().to_numpy(),
            [2.8759, 2.2210, -5.0969],
            atol=5e-5,
        )

    def test_robustness_0997_reproduces_local_run(self):
        result = run_specification(
            self.data,
            name="robustness",
            lambda_beta=0.997,
            kappa_sigma=0.96,
            horizon=10,
        )

        self.assertEqual(int((~result.stability["stable"]).sum()), 45)
        self.assertTrue(
            np.isclose(result.connectedness.tci.mean(), 8.881129191359921)
        )
        np.testing.assert_allclose(
            result.connectedness.net.mean().to_numpy(),
            [2.2284, 1.7012, -3.9296],
            atol=5e-5,
        )
