class Course:

    all_courses = {}

    def __init__(self, name, code:str, credits: int, professor:str, capacity:int, required_completed_courses: list):
        self._name = name
        self.code = code
        self._credits = credits
        self._professor = professor
        self._capacity = capacity
        self._required_completed_courses = required_completed_courses
        Course.all_courses[code] = self


    def __str__(self):
        print(f"\nName: {self._name}.\nCode: {self._code}.\nAssigned professor: {self._professor}.")


    @classmethod
    def show_all_courses(cls):
        for course in cls.all_courses:
            print(course)

