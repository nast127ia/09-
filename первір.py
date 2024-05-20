import unittest
from pydantic import ValidationError
from stats_model import Stats

class StatsModelTest(unittest.TestCase):
    def test_valid_stats(self):
        valid_data = {
            "base": "BTC",
            "quote": "USD",
            "volume_24h": 12345678.90,
            "last_trade_price": 43210.00,
            "bid": 43200.00,
            "ask": 43220.00,
            "high": 44000.00,
            "low": 42000.00,
            "open": 43000.00,
            "change_24h": 0.02
        }
        stats = Stats(**valid_data)
        self.assertEqual(stats.base, "BTC")
        self.assertEqual(stats.quote, "USD")

    def test_invalid_stats(self):
        invalid_data = {
            "base": "BTC123",
            "quote": "USD",
            "volume_24h": -12345678.90,
            "last_trade_price": -43210.00,
            "bid": -43200.00,
            "ask": -43220.00,
            "high": -44000.00,
            "low": -42000.00,
            "open": -43000.00,
            "change_24h": 2.02
        }
        with self.assertRaises(ValidationError):
            Stats(**invalid_data)

if __name__ == '__main__':
    unittest.main()
