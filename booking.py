def overlaps(start_a: int, end_a: int, start_b: int, end_b: int) -> bool:
    """Вернуть True, если два слота [start, end) одной аудитории делят минуту."""
    for start, end in ((start_a, end_a), (start_b, end_b)):
        if type(start) is not int or type(end) is not int:
            raise TypeError("Границы слота должны быть целыми минутами")
        if not 0 <= start < end <= 1440:
            raise ValueError("Слот должен быть непустым и находиться в пределах суток")
    return start_a < end_b and start_b < end_a


if __name__ == "__main__":
    print("Конфликт двух соседних пар:", overlaps(540, 630, 630, 720))
