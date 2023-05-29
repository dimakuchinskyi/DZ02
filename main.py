import logging
class StudentProcessor:
    def __init__(self):
        self.students = []
        self.logger = logging.getLogger('StudentProcessor')
        self.logger.setLevel(logging.INFO)
        console_handler = logging.StreamHandler()
        self.logger.addHandler(console_handler)
    def add_student(self, student):
        self.students.append(student)
        self.logger.info(f"Додано студента: {student}")
    def remove_student(self, student):
        if student in self.students:
            self.students.remove(student)
            self.logger.info(f"Вилучений студент: {student}")
        else:
            self.logger.warning(f"Студент не знайдений: {student}")
    def process_students(self):
        for student in self.students:
            self.logger.info(f"Обробка студента: {student}")
processor = StudentProcessor()
processor.add_student("глеп")
processor.add_student("максік")
processor.remove_student("глеп")
processor.remove_student("діма")
processor.process_students()
