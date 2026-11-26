# Лабораторная 3 · Парковка

**Касьян А.С. · Вариант 12**

## Постановка

Напишите тесты и измерьте покрытие для модуля ниже.

```python
# main.py
from typing import Dict, Optional


def occupy(spots: Dict[int, Optional[str]], spot: int, plate: str) -> None:
    if spot not in spots:
        raise KeyError("unknown spot")
    if spots[spot] is not None:
        raise ValueError("spot busy")
    spots[spot] = plate


def free_spot(spots: Dict[int, Optional[str]], spot: int) -> None:
    if spot not in spots:
        raise KeyError("unknown spot")
    spots[spot] = None


def find_spot_by_plate(spots: Dict[int, Optional[str]], plate: str) -> Optional[int]:
    for spot, p in spots.items():
        if p == plate:
            return spot
    return None


def free_count(spots: Dict[int, Optional[str]]) -> int:
    return sum(1 for p in spots.values() if p is None)


def init_parking(n: int) -> Dict[int, Optional[str]]:
    if n <= 0:
        raise ValueError("n must be > 0")
    return {i: None for i in range(1, n + 1)}
```

## Проверка

В виртуальном окружении установите зависимости командой `python -m pip install -r requirements.txt`. Для обычного прогона выполните `python -m pytest -q`, для отчёта по строкам — `python -m pytest --cov=main --cov-report=term-missing --cov-fail-under=90`.

Контрольный прогон: 6 проверок прошли, покрыты 22 из 22 исполняемых строк main.py (100 