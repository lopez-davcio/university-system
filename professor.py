from user import User
import utils
class Professor(User):

    def __init__(self, name, title, password):
        super().__init__(name, title, password)
        self._current_courses = {}
        self._past_courses = {}


   
    def professor_menu(self):
        """It controls the flow of the professor menu"""
        while True:
            self.print_professor_menu()
            choice = input()
            match choice:
                case "1":
                    self._current_courses 
                case "2":
                    self._past_courses
                case "3":
                    self.assign_grade()



    def print_professor_menu(self):
        print("""
        --- Professor Menu ---
        Press 1 - View your assigned courses.
        Press 2 - View past courses.
        Press 3 - Input or update student grades.
        Press 4 - Log off.
        """)



    def assign_grade(self):
        """ADD DESCRIPTION"""
        course = self.input_course_to_grade()
        student = self.input_student_to_grade(course)
        grade = self.input_grade() 
        #instantiate a grades object



    def input_course_to_grade(self):    
        """Prompts user to input course, validates that the course is in professors current courses through validate_course(). Returns the course object. Lets the user quit and restarts flow"""

        while True:
            course = input('\nPlease enter the code of the course, or type "c" to cancel: ').lower()

            if course == 'c':
                print('Grade assign cancelled.')
                self.professor_menu()
            
            elif self.validate_course(course):
                return self._current_courses[course]
            else:
                print("That course is not listed as your assigned course.")



    def validate_course(self, course):
        """Checks if the course is in professor's current courses.
        Returns True/False"""
        return course in self._current_courses
    
        

    def input_student_to_grade(self, course):    
        """Prompt user to input student, validate the student is in course's list of current students. Returns the student object. Let the user quit and restarts flow"""

        while True:
            student_id = input('\nPlease enter the ID of the student, or type "c" to cancel: ').lower()

            if student_id == 'c':
                print('Grade assign cancelled.')
                self.professor_menu()
            
            elif self.validate_student(course, student_id):
                student_object = User.get_users_items()[student_id]
                return student_object
            else:
                print("That student is not registered for that course.")



    def validate_student(self, course, student_id):
        """Check if the student is in the course's dict of current students.
        Return True/False"""
        course = None #get course list of current students
        
        return True #return True for now, later return student in list of current students



    def input_grade(self):
        """Prompt the user to enter the grade and convert it to float.
        Check if grade is 0 to 10 and with the help of utils.is_float() catch the error and inform the user if it's an invalid input,in that case start the loop again.
        Prompt to confirm the entered grade is correct.
        Return the grade as a float"""

        while True:
            grade = input("Please enter the grade: ")
            float_grade = utils.is_float(grade)
            if float_grade:
                if float_grade >= 0 and float_grade <= 10:
                    return float_grade
            else:
                print("Invalid input. Enter a number between 0 and 10, with no more than two decimal places.")



