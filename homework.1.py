# 1. Класс Person
class Person:
    def __init__(self, full_name, age, is_married):
        self.full_name = full_name
        self.age = age
        self.is_married = is_married

    # 2. Метод для вывода информации
    def introduce_myself(self):
        print(f"ФИО: {self.full_name}")
        print(f"Возраст: {self.age}")
        print(f"Женат/Замужем: {'Да' if self.is_married else 'Нет'}")

# 3. Класс Student
class Student(Person):
    def __init__(self, full_name, age, is_married, marks):
        super().__init__(full_name, age, is_married)
        self.marks = marks  # словарь предмет:оценка

    # 4. Метод для подсчета средней оценки
    def average_mark(self):
        return sum(self.marks.values()) / len(self.marks)

    # Переопределим метод вывода
    def introduce_myself(self):
        super().introduce_myself()
        print("Оценки:")
        for subject, mark in self.marks.items():
            print(f"  {subject}: {mark}")
        print(f"Средняя оценка: {self.average_mark():.2f}")

# 5. Класс Teacher
class Teacher(Person):
    base_salary = 40000  # 6. Атрибут класса

    def __init__(self, full_name, age, is_married, experience):
        super().__init__(full_name, age, is_married)
        self.experience = experience

    # 7. Метод расчета зарплаты
    def calculate_salary(self):
        bonus_years = max(0, self.experience - 3)
        bonus = Teacher.base_salary * 0.05 * bonus_years
        return Teacher.base_salary + bonus

    # Переопределим метод вывода
    def introduce_myself(self):
        super().introduce_myself()
        print(f"Стаж: {self.experience} лет")
        print(f"Индивидуальная зарплата: {self.calculate_salary():.2f} сом")

# 8. Создание учителя
teacher = Teacher("Иванов Иван Иванович", 40, True, 10)
print("Информация о преподавателе:")
teacher.introduce_myself()

print("\n" + "="*40 + "\n")

# 9. Функция создания студентов
def create_students():
    student1 = Student("Суранбаева Аяна", 16, False, {"Математика": 4, "История": 5, "Физика": 3})
    student2 = Student("Шайлообекова Арууке", 17, False, {"Математика": 5, "История": 5, "Физика": 5})
    student3 = Student("Жекшеева Зарина", 16, False, {"Математика": 3, "История": 4, "Физика": 4})
    return [student1, student2, student3]

# 10. Вызов функции и вывод информации
students = create_students()
for i, student in enumerate(students, 1):
    print(f"Студент {i}:")
    student.introduce_myself()
    print("-" * 30)
