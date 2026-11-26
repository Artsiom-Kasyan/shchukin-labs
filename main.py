def clean_isbn(raw: str) -> str:
    return raw.replace("-", "").replace(" ", "")


def is_valid_isbn10(raw: str) -> bool:
    code = clean_isbn(raw)
    if len(code) != 10 or any(c not in "0123456789" for c in code[:9]):
        return False
    if code[-1] not in "0123456789X":
        return False
    digits = [10 if c == "X" else int(c) for c in code]
    return sum(weight * digit for weight, digit in zip(range(10, 0, -1), digits)) % 11 == 0
