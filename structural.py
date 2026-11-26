def create_parking(size):
    if size < 1:
        raise ValueError("Парковка должна содержать хотя бы одно место")
    return dict.fromkeys(range(1, size + 1))


def find(spots, plate):
    return next((number for number, value in spots.items() if value == plate), None)


def occupy(spots, number, plate):
    if spots[number] is not None or not plate or plate in spots.values():
        raise ValueError("Место занято или номер машины недопустим")
    spots[number] = plate


def release(spots, number):
    if spots[number] is None:
        raise ValueError("Место уже свободно")
    spots[number] = None


def free_count(spots):
    return sum(value is None for value in spots.values())


if __name__ == "__main__":
    parking = create_parking(3)
    occupy(parking, 1, "А101")
    occupy(parking, 3, "В303")
    print("Место В303:", find(parking, "В303"))
    print("Свободно:", free_count(parking))
    release(parking, 1)
    print("После выезда:", free_count(parking))
