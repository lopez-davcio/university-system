from user import User
from grades import Grades

class Student(User):

    def __init__(self, name, title, password):
        super().__init__(name, title, password)
        self._current_courses = {}
        self._completed_courses = {}
        self._credits_available = 120
        self.grades = None        


    def __post_init__(self):
        self.grades = Grades(self.id)

