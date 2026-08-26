import numpy as np
import pandas as pd
import unittest

from tvp_connectedness.connectedness import calculate_connectedness


class ConnectednessTests(unittest.TestCase):
    def test_connectedness_orientation_and_net_balance(self):
        theta = np.array(
            [
                [
                    [0.80, 0.15, 0.05],
                    [0.10, 0.85, 0.05],
                    [0.20, 0.10, 0.70],
                ]
            ]
        )
        result = calculate_connectedness(
            theta,
            dates=pd.Index([pd.Timestamp("2026-01-01")]),
            variables=("A", "B", "C"),
        )

        np.testing.assert_allclose(result.from_others.iloc[0], [20, 15, 30])
        np.testing.assert_allclose(result.to_others.iloc[0], [30, 25, 10])
        np.testing.assert_allclose(result.net.iloc[0], [10, 10, -20])
        self.assertTrue(np.isclose(result.net.iloc[0].sum(), 0))
        self.assertTrue(np.isclose(result.tci.iloc[0], 65 / 3))
