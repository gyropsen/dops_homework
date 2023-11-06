import pytest

from src.dop_3 import count_number_in_list


@pytest.fixture
def get_data():
    return [[1, 2, 3, 4, 3, 2, 4, 1], [1, 2, 3, 4, 5, 6, 7], [1, 1, 1, 1, 1, 1], []]


def test_count_number_in_list(get_data):
    assert count_number_in_list(get_data[0], 1) == 2
    assert count_number_in_list(get_data[1], 8) == 0
    assert count_number_in_list(get_data[2], 1) == 6
    assert count_number_in_list(get_data[3], 1) == 0
