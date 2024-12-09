# student.py
class Student:
    def __init__(self, student_id, name, age, grade):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade

    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.name}, Age: {self.age}, Grade: {self.grade}"

    def get_student_info(self):
        return {
            'ID': self.student_id,
            'Name': self.name,
            'Age': self.age,
            'Grade': self.grade
        }
