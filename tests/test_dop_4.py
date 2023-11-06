import pytest

from src.dop_4 import calculate_area


@pytest.mark.parametrize("shape, sides, expected_result", [("квадрат", [2], 4),
                                                           ("прямоугольник", [2, 3], 6),
                                                           ("треугольник", [3, 4], 6),
                                                           ("круг", [4], 50.24),
                                                           ("", [], None),
                                                           (None, [1, 2, 3], None),
                                                           ("квадрат", None, None)
                                                           ])
def test_calculate_area(shape, sides, expected_result):
    assert calculate_area(shape, sides) == expected_result
