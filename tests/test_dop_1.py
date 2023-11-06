import pytest
from src.dop_1 import sum_divisible_by_3_or_5


@pytest.mark.parametrize("number, expected_result", [([1, 2, 3, 4, 5], 8),
                                                     ([], 0),
                                                     ([1, 2, 4, 7], 0)])
def test_sum_divisible_by_3_or_5(number, expected_result):
    assert sum_divisible_by_3_or_5(number) == expected_result
