from user import User
from course import Course
import utils
import re

class Admin(User):
    def __init__(self, name, title, password):
        super().__init__(name, title, password)



    def menu(self):
        """It controls the flow of the admin menu"""
        from orchestrator import UniversitySystem
        
        while True:            
            self.print_admin_menu()
            choice = input()
            match choice:
                case "1":
                    user_obj = self._input_user_to_remove()
                    if user_obj:
                        user_obj.remove_user()
                case "2":
                    self.add_new_course()
                case "3":
                    pass
                case "4":
                    print("You have been logged off.")
                    return
                


    
    def _input_user_to_remove(self):    
        """Prompt user to input user and removes it from registry through remove_user(). Let the user quit and restart flow"""

        while True:
            user_id = input('\nPlease enter the ID of the user, or type "c" to cancel: ').lower()
            user_obj = User.get_user_instance(user_id)
            if user_id == 'c':
                print('User removal cancelled.') 
                return                          
            elif user_obj:
                user_obj.remove_user()
                return
            else:
                print("That student is not recognised.")



    def add_new_course(self):
        """With the help of input_course_information(), prompt user to enter the information needed to create a course and then initialize a course object.
        Let the user quit return to admin menu"""

        name = self.input_course_information("name")
        code = self.input_course_code()
        credits = self.input_course_digits("credits")
        professor = self.input_course_information("professor")
        capacity = self.input_course_digits("capacity")
        required_completed_courses = self.input_course_required_completed_courses()

        new_course = Course(name, code, credits, professor, capacity, required_completed_courses)
        print(f"\nA new course has been created:\n{new_course}")
        

    
    def input_course_information(self, info):
        """Prompt the user to enter the info required, the info required is passed on the function as a string.
        Keep user in loop and doublecheck if info is correct and return user input.
        Let the user quit."""

        while True:
            user_input = input(f"\nPlease enter the course {info} or 'q' to quit: ")
            if user_input.lower() == 'q':
                print("The course creation has been cancelled.")
                self.menu()             
            else:
                confirm = input(f"Is {user_input} the correct {info}? (y/n): ")
                if confirm.lower() == "y":
                    return user_input
            


    def input_course_code(self):
        """Prompt the user to enter the course code and validates the pattern. Keep user in loop and doublecheck if code is correct and return it as a str.
        Let the user quit."""

        while True:
            course_code = input(f"\nPlease enter the course code or 'q' to quit: ")
            valid = Admin.validate_course_code_pattern(course_code)        
            if valid:
                confirm = input(f"Is {course_code} the correct code? (y/n):")
                if confirm.lower() == "y":
                    return course_code
            else:
                print("The code must be made of two letters followed by three digits.")



    def input_course_digits(self, info):        
        """Prompt the user to enter the info required, the info required is passed on the function as a string.
        Keep user in loop and doublecheck that the input is an integer.
        Return user input, let the user quit."""

        while True:
            user_input = input(f"\nPlease enter the course {info} or 'q' to quit: ") 
            digits = utils.is_integer(user_input)
            if digits:                
                confirm = input(f"Is {digits} the correct {info}? (y/n): ")
                if confirm.lower() == "y":
                    return digits
            else:
                print("\nOnly digits are valid.")



    def input_course_required_completed_courses(self):
        course_list = []
        while True:
            course_code = input("\nPlease enter the code of the required course, or type 'n' if none, or type 'q' to cancel: ")
            if course_code.lower() == 'q':
                print("The course creation has been cancelled.")
                self.menu()
            if course_code.lower() == 'n': 
                return course_list
            valid = Admin.validate_course_code_pattern(course_code)            
            if valid:
                confirm = input(f"Is {course_code} the correct code? (y/n):")
                if confirm.lower() == "y":
                    course_list.append(course_code)
                    while True:
                        choice = input("Are there more required courses to be entered?: (y/n)").lower()
                        match choice:
                            case "y":
                                break
                            case "n":
                                return course_list
                            case _:
                                print("\nYour selection is not recognised")
            else:
                print("\nThe code must be made of two letters followed by three digits, please add only one course code at a time.")



    @staticmethod
    def validate_course_code_pattern(course_code):
        """Check the code passed as argument against the code pattern required in courses"""
        match = re.fullmatch(r"[a-z]{2}\d{3}", course_code, re.I)
        return match



    @staticmethod
    def print_admin_menu():
        print("""
        --- Admin Menu ---
        Press 1 - Remove an account 
        Press 2 - Add a course
        Press 3 - Remove a course
        Press 4 - Log off
        """)

