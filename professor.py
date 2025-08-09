from user import User

class Professor(User):

    def __init__(self, name, title, password):
        super().__init__(name, title, password)
        self._current_courses = {}
        self._past_courses = {}


    #current_courses getter

    #past_courses getter

    """go over again once the loop points towards this functions


    def validate_course(self, course):
        Checks if the course is in professor's current courses
        return course in self._current_courses
    
    def input_course(self):
    
        Asks input to obtain course and student to assign grade

        while True:
            course = input('Please enter the code of the course, or type "q" to quit: ')

            if course.lower() == 'q':
                print('Grade assign cancelled.')
                return 'quit'
            
            if self.validate_course(course):
                break
        return course

    def assign_grade(self):
    
        using validate_course() for validation

        while True:
            course = self.input_course()
            if course == 'quit':
                break
            if course != False:
                if self.validate_course(course) == True:
                    break
        
        
prof = Professor('n', 't', 'p')        
prof.assign_grade()
               
"""