import unittest
from unittest import TestCase


def calculate_largest_lost(prices: []):
    buy = len(prices) - 2
    sell = len(prices) - 1
    largest_lost = None
    while buy >= 0:
        gap = prices[sell] - prices[buy]
        if gap <= 0:
            if largest_lost is None:
                largest_lost = gap
            else:
                largest_lost = min(largest_lost, gap)
        else:
            sell = buy
        buy -= 1
    return largest_lost


class TestCalculateLargestLost(TestCase):
    def test_when_empty_price_list(self):
        prices = []
        largest_lost = calculate_largest_lost(prices)
        self.assertEqual(None, largest_lost)

    def test_when_less_than_two_price_list(self):
        prices = [1]
        largest_lost = calculate_largest_lost(prices)
        self.assertEqual(None, largest_lost)

    def test_when_positive_lost(self):
        prices = [1, 2, 3, 4, 5, 6, 7]
        largest_lost = calculate_largest_lost(prices)
        self.assertEqual(None, largest_lost)

    def test_when_negative_lost(self):
        prices = [7, 6, 5, 4, 1, 2, 3]
        largest_lost = calculate_largest_lost(prices)
        self.assertEqual(-6, largest_lost)

    def test_when_zero_lost(self):
        prices = [1, 1, 1, 1, 1, 1]
        largest_lost = calculate_largest_lost(prices)
        self.assertEqual(0, largest_lost)

    def test_when_large_price_list(self):
        prices = list(reversed(range(5000)))
        largest_lost = calculate_largest_lost(prices)
        self.assertEqual(-4999, largest_lost)


if __name__ == '__main__':
    unittest.main()
