from main import clean_isbn, is_valid_isbn10


def test_clean():
    assert clean_isbn("0-306 40615-2") == "0306406152"


def test_known_book():
    assert is_valid_isbn10("0-306-40615-2")


def test_check_digit_x():
    assert is_valid_isbn10("080442957X")


def test_wrong_checksum():
    assert not is_valid_isbn10("0306406153")


def test_wrong_length():
    assert not is_valid_isbn10("306406152")


def test_invalid_characters():
    for value in ["X804429570", "080442957x", "０306406152"]:
        assert not is_valid_isbn10(value)
