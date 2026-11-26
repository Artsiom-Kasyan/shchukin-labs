from dataclasses import dataclass


@dataclass
class Space:
    number: int
    plate: str | None = None

    def park(self, plate):
        if self.plate is not None:
            raise ValueError("Место занято")
        self.plate = plate

    def release(self):
        if self.plate is None:
            raise ValueError("Место уже свободно")
        self.plate = None


class Parking:
    def __init__(self, size):
        if size < 1:
            raise ValueError("Парковка должна содержать хотя бы одно место")
        self._spaces = {n: Space(n) for n in range(1, size + 1)}

    def find(self, plate):
        return next((s.number for s in self._spaces.values() if s.plate == plate), None)

    def occupy(self, number, plate):
        if not plate or self.find(plate) is not None:
            raise ValueError("Пустой или повторный номер машины")
        self._spaces[number].park(plate)

    def release(self, number):
        self._spaces[number].release()

    def free_count(self):
        return sum(s.plate is None for s in self._spaces.values())


if __name__ == "__main__":
    parking = Parking(3)
    parking.occupy(1, "А101")
    parking.occupy(3, "В303")
    print("Место В303:", parking.find("В303"))
    print("Свободно:", parking.free_count())
    parking.release(1)
    print("После выезда:", parking.free_count())
