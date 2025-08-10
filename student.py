from user import User
from grades import Grades

class Student(User):

    def __init__(self, name, title, password):
        super().__init__(name, title, password)
        self._current_courses = {}
        self._completed_courses = {}
        self._credits_available = 120
        self._grades = None        


    def __post_init__(self):
        self._grades = Grades(self.id)


    def menu(self):
        """It controls the flow of the student menu"""
        while True:
            self.print_student_menu()
            choice = input()
            match choice:
                case "1":
                    self._current_courses 
                case "2":
                    self._completed_courses
                case "3":
                    pass
                case "4":
                    pass
                case "5":
                    self._grades.show_courses_and_grades()
                case "6":
                    self._grades.show_gpa()
                case "7":
                    print("You have been logged off.")
                    return


    def print_student_menu(self):
        print("""
        --- Student Menu ---
        Press 1 - View your current courses
        Press 2 - View past courses
        Press 3 - Enrol in available courses
        Press 4 - Withdraw from a course
        Press 5 - View grades
        Press 6 - Check your GPA
        Press 7 - Log off
        """)