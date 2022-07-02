import unittest
from client3 import getDataPoint, getRatio


class ClientTest(unittest.TestCase):
    def test_getDataPoint_calculatePrice(self):
        quotes = [
            {
                "top_ask": {"price": 121.2, "size": 36},
                "timestamp": "2019-02-11 22:06:30.572453",
                "top_bid": {"price": 120.48, "size": 109},
                "id": "0.109974697771",
                "stock": "ABC",
            },
            {
                "top_ask": {"price": 121.68, "size": 4},
                "timestamp": "2019-02-11 22:06:30.572453",
                "top_bid": {"price": 117.87, "size": 81},
                "id": "0.109974697771",
                "stock": "DEF",
            },
        ]
        """ ------------ Add the assertion below ------------ """
        # I added the assertion to check if the correct top_bid, top_ask, and price where being outputed
        for quote in quotes:
            self.assertEqual(
                getDataPoint(quote),
                (
                    quote["stock"],
                    quote["top_bid"]["price"],
                    quote["top_ask"]["price"],
                    (quote["top_bid"]["price"] + quote["top_ask"]["price"]) / 2,
                ),
            )

    def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
        quotes = [
            {
                "top_ask": {"price": 119.2, "size": 36},
                "timestamp": "2019-02-11 22:06:30.572453",
                "top_bid": {"price": 120.48, "size": 109},
                "id": "0.109974697771",
                "stock": "ABC",
            },
            {
                "top_ask": {"price": 121.68, "size": 4},
                "timestamp": "2019-02-11 22:06:30.572453",
                "top_bid": {"price": 117.87, "size": 81},
                "id": "0.109974697771",
                "stock": "DEF",
            },
        ]
        """ ------------ Add the assertion below ------------ """
        # I added the assertion to check if the correct the top_ask was greater than top_bid
        for quote in quotes:
            self.assertEqual(
                getDataPoint(quote),
                (
                    quote["stock"],
                    quote["top_bid"]["price"],
                    quote["top_ask"]["price"],
                    (quote["top_bid"]["price"] + quote["top_ask"]["price"]) / 2,
                ),
            )

    """ ------------ Add more unit tests ------------ """
    # I added these four test to check if changes I made in the client where functioning correctly

    def test_getRatio_calculateRatio(self):
        price_a = 112.74
        price_b = 111.80
        self.assertEqual(getRatio(price_a, price_b), price_a / price_b)

    def test_getRatio_price_b_isZero(self):
        price_a = 112.74
        price_b = 0
        self.assertEqual(getRatio(price_a, price_b), 0)

    def test_getRatio_price_a_isZero(self):
        price_a = 0
        price_b = 111.80
        self.assertEqual(getRatio(price_a, price_b), 0)


if __name__ == "__main__":
    unittest.main()
