
class Enrolment:

    def __init__(self, course: object, student:object):

        self._course = course
        self._student = student
        self.student_fulfills_requirements = self.check_requirements()
        self.registration_management()
        


    def check_requirements(self):
        """Check that the student has completed the required courses through check_required_completed_courses().
        Check that the course is not full and accepts students through course_accepts_students().
        Check that student has sufficient credits through student.has_enough_credits().
        Return True if all requirements are fulfilled.
        Inform the user if any requirement is not fulfilled and return False.
        """
        courses = self.check_required_completed_courses()
        availability = self._course.course_accepts_students()
        credits = self._student.has_enough_credits()
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
        """Checks that the courses required to enrol in a new course are in the student's completed courses.
        Return True if all required courses have been previously completed.Return False otherwise"""
        course = self._course
        student = self._student
        required = course.required_completed_courses()
        completed = student.completed_courses()
        return all(course in completed for course in required)

    
    def take_credits_from_student(self):
        """Gets the course credits and deduce those credits from the student through reduce_credits()"""
        course_credits = self._course.credits
        self._student.reduce_credits(course_credits)


    def add_student_to_course(self):
        """Add the student id to the list of students on the course instance through add_student_to_students_enrolled()"""
        id = self._student.id
        self._course.add_student_to_students_enrolled(id)


    def add_course_to_student(self):
        course = self._course.code
        self.add_course_to_current_courses(course)



    def registration_management(self):
        if self.student_fulfills_requirements:
            self.take_credits_from_student()
            self.add_student_to_course()
            self.add_course_to_student()
            print(f"The student {self._student.id} has been enrolled in the course {self._course.code}.")
        else:
            print("The registration has not been completed.")
    

    def deregister_from_course(student:object, course: object):
        pass