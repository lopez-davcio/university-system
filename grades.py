
class Grades:

    def __init__(self, student_id, gpa=None):
        self._student_id = student_id
        self._grades = {}
        self._gpa = gpa
        
        
    def recalculate_gpa(self):
        """Recalculate the GPA by averaging all grades in _grades, and update the _gpa attribute."""
        grade_sum = 0
        grade_count = len(self._grades)
        for key, value in self._grades:
            grade_sum += value
        new_gpa = grade_sum / grade_count
        self._gpa = new_gpa
        

    def show_courses_and_grades(self):
        for key, value in self._grades:
            print(f"Course code: {key}, grade: {value}")


    
