import pytest

from src.dop_2 import check_email


@pytest.fixture
def get_data():
    return ["asdf@mail.ru", "asdf@ru", "", None, "asdf.ru"]


def test_check_email(get_data):
    assert check_email(get_data[0])
    assert not check_email(get_data[1])
    assert not check_email(get_data[2])
    assert not check_email(get_data[3])
    assert not check_email(get_data[4])
