import pytest
from src.dop_5 import my_slice


@pytest.mark.parametrize("coll, start, stop, expected_result", [([1, 2, 3, 4, 5, 6, 7], 0, 4, [1, 2, 3, 4]),
                                                                ([1, 2, 3, 4, 5], 0, 3, [1, 2, 3]),
                                                                ([], 2, 2, []),
                                                                ([1, 2, 3, 4, 5], -4, 3, [2, 3]),
                                                                ([1, 2, 3, 4, 5], 0, -1, [1, 2, 3, 4]),
                                                                ([1, 2, 3, 4, 5], -6, -1, [1, 2, 3, 4])])
def test_my_slice(coll, start, stop, expected_result):
    assert my_slice(coll, start, stop) == expected_result
