import unittest
from coinbaseloader import CoinbaseLoader

class CoinbaseLoaderTest(unittest.TestCase):
    def setUp(self):
        self.logger = logging.getLogger('test_logger')
        self.logger.setLevel(logging.DEBUG)
        self.loader = CoinbaseLoader(logger=self.logger)

    def test_successful_data_load(self):
        self.logger.info("Testing successful data load")
        data = self.loader.load_data()
        self.assertIsNotNone(data)
        self.assertIsInstance(data, list)
        self.assertGreater(len(data), 0)
        self.logger.info("Successful data load test passed")

    def test_invalid_symbol(self):
        self.logger.info("Testing invalid symbol handling")
        with self.assertRaises(ValueError):
            self.loader.load_symbol('INVALID_SYMBOL')
        self.logger.info("Invalid symbol handling test passed")

    def test_load_symbol(self):
        self.logger.info("Testing load symbol")
        symbol_data = self.loader.load_symbol('BTC-USD')
        self.assertIsNotNone(symbol_data)
        self.assertIsInstance(symbol_data, dict)
        self.assertIn('symbol', symbol_data)
        self.assertEqual(symbol_data['symbol'], 'BTC-USD')
        self.logger.info("Load symbol test passed")

if __name__ == '__main__':
    unittest.main()
