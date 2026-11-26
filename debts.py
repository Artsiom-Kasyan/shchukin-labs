class DebtRegister:
    def __init__(self):
        self._debts = {}

    def add(self, student, lab):
        if not student.strip() or lab < 1:
            raise ValueError("Укажите студента и положительный номер работы")
        self._debts.setdefault(student, set()).add(lab)

    def close(self, student, lab):
        if lab not in self._debts.get(student, ()):
            raise KeyError((student, lab))
        self._debts[student].remove(lab)

    def count(self, student):
        return len(self._debts.get(student, ()))


if __name__ == "__main__":
    register = DebtRegister()
    register.add("Студент 1", 3)
    register.add("Студент 1", 4)
    register.close("Студент 1", 3)
    print("# Отчёт по учебному примеру\n")
    print("Осталось работ у студента 1:", register.count("Студент 1"))
