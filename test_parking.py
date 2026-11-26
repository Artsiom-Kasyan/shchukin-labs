import pytest

from main import find_spot_by_plate, free_count, free_spot, init_parking, occupy


def test_parking_lifecycle():
    spots = init_parking(2)
    assert spots == {1: None, 2: None}
    occupy(spots, 2, "А123")
    assert find_spot_by_plate(spots, "А123") == 2
    assert free_count(spots) == 1
    free_spot(spots, 2)
    assert find_spot_by_plate(spots, "А123") is None
    assert free_count(spots) == 2


@pytest.mark.parametrize("size", [0, -1])
def test_invalid_size(size):
    with pytest.raises(ValueError):
        init_parking(size)


def test_busy_space_preserves_plate():
    spots = {1: "А123"}
    with pytest.raises(ValueError):
        occupy(spots, 1, "В456")
    assert spots == {1: "А123"}


def test_unknown_space():
    with pytest.raises(KeyError):
        occupy({}, 1, "А123")
    with pytest.raises(KeyError):
        free_spot({}, 1)


def test_free_space_can_be_released_again():
    spots = init_parking(1)
    free_spot(spots, 1)
    assert free_count(spots) == 1
