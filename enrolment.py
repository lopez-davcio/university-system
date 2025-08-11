
class Enrolment:

    def __init__(self, course: object, student:object):

        self._course = course
        self._student = student
        self.student_fulfills_requirements = self.check_requirements()
        self.registration_management()
        


    def check_requirements(self):
        courses = self.check_required_completed_courses()
        availability = self.course_not_full()
        credits = self.student_has_enough_credits()
        if courses and availability and credits:
            return True
        else:
            if not courses:
                print("The student hasn't completed all courses required to access the current course.")
                return False
            if not availability:
                print("The course is full, no more students are accepted.")
                return False
            if not credits:
                print("The student does not have enough credits to access this course.")
                return False

    
    def check_required_completed_courses(self):
        pass


    def course_not_full(self):
        pass
    
    def student_has_enough_credits(self):
        pass

    def registration_management(self):
        if self.student_fulfills_requirements:
            self.take_credits_from_student()
            self.add_student_to_course()
            self.add_course_to_student()

    def take_credits_from_student(self):
        pass

    def add_student_to_course(self):
        pass

    def add_course_to_student(self):
        pass


    def deregister_from_course(student:object, course: object):
        pass