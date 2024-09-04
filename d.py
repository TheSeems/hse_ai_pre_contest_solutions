import math

class Student:
    def __init__(self, name: str, surname: str, grade) -> None:
        self.name = name
        self.surname = surname
        self.grade = grade

    def add_grade(self) -> None:
        self.grade += 1

    def print_info(self) -> None:
        print(f"Student: {self.name} {self.surname}")
        print(f"Grade: {self.grade}")


class PythonStudent(Student):
    def __init__(
        self, name: str, surname: str, grade, python_mark = 0
    ) -> None:
        super().__init__(name, surname, grade)
        self.python_mark = python_mark
        self.python_learned = False

    def learn_python(self) -> None:
        self.python_learned = True

    def get_mark_python(self, hw1, hw2, hw3, hw4) -> int:
        if not self.python_learned:
            print("Надо пойти учить питон")
            return 0
        self.python_mark = round(0.3 * hw1 + 0.3 * hw2 + 0.3 * hw3 + 0.1 * hw4)
        return self.python_mark

    def print_info(self) -> None:
        super().print_info()
        print(f"Python mark: {self.python_mark}")


if __name__ == "__main__":
    for i in range(8):
        exec(input())
