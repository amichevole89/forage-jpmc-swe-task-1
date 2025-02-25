import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
    def test_getDataPoint_calculatePrice(self):
        quotes = [
        {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
        {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        """ ------------ Add the assertion below ------------ """
        for quote in quotes:
            # Arrange
            expected_data_point = (
                quote["stock"],
                float(quote["top_bid"]["price"]),
                float(quote["top_ask"]["price"]),
                (float(quote["top_bid"]["price"]) + float(quote["top_ask"]["price"]))
                / 2,
            )
            # Act
            data_point = getDataPoint(quote)

            # Assert
            self.assertEqual(data_point, expected_data_point)



    def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
        quotes = [
        {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC',},
        {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF',}
        ]
        """ ------------ Add the assertion below ------------ """
        for quote in quotes:
            # Arrange
            expected_data_point = (
                quote["stock"],
                float(quote["top_bid"]["price"]),
                float(quote["top_ask"]["price"]),
                (float(quote["top_bid"]["price"]) + float(quote["top_ask"]["price"]))/2,
            )
            # Act
            data_point = getDataPoint(quote)

            # Assert
            self.assertEqual(data_point, expected_data_point)


    """ ------------ Add more unit tests ------------ """
    def test_getRatio(self):
        # Arrange
        price_a = 342
        price_b = 171
        expected_ratio = price_a / price_b

        # Act
        ratio = getRatio(price_a, price_b)

        # Assert
        self.assertEqual(ratio, expected_ratio)



if __name__ == '__main__':
    unittest.main()
