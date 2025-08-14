from student import Student
from professor import Professor
from course import Course
from admin import Admin


def create_mock_objects():
    print(Student('David', 'student', 's', ['mt223', 'al101', 'os202'] , ['ds123','cn404']))
    Student('Alice', 'student', 'Aa123456')
    Student('Bob', 'student', 'Bb654321')
    Student('Charlie', 'student', 'Cc987654')
    Student('Eva', 'student', 'Ee456789')
    Student('Frank', 'student', 'Ff112233')
    Student('Grace', 'student', 'Gg223344')
    Student('Hannah', 'student', 'Hh334455')
    Student('Ian', 'student', 'Ii445566')
    Student('Julia', 'student', 'Jj556678')

    print(Professor('Robert', 'professor', 'p', ['os202','al101'], ['db303']))
    Professor('Linda', 'professor', 'Ln123789')
    Professor('Michael', 'professor', 'Mh987321')
    Professor('Sarah', 'professor', 'Sr456123')
    Professor('Thomas', 'professor', 'Ts789654')
    Professor('Patricia', 'professor', 'Pc321987')
    Professor('James', 'professor', 'Js654789')
    Professor('Barbara', 'professor', 'Bb852963')
    Professor('William', 'professor', 'Wm741852')
    Professor('Elizabeth', 'professor', 'Ez963741')

    Course('Data science', 'ds123', 30, 'Robert', 15, ['mt223'])
    Course('Algorithms', 'al101', 25, 'Linda', 20, ['ma594'])
    Course('Operating Systems', 'os202', 30, 'Michael', 25, ['al101'])
    Course('Databases', 'db303', 20, 'Sarah', 15, ['al101'])
    Course('Computer Networks', 'cn404', 25, 'Thomas', 20, ['os202'])
    Course('Artificial Intelligence', 'ai505', 30, 'Patricia', 20, ['al101', 'mt223'])
    Course('Software Engineering', 'se606', 25, 'James', 30, ['al101'])
    Course('Cybersecurity', 'cs707', 20, 'Barbara', 15, ['os202'])
    Course('Machine Learning', 'mt223', 30, 'William', 25, ['ds123', 'al101'])
    Course('Cloud Computing', 'cc909', 25, 'Elizabeth', 20, ['ds123','os202'])

    print(Admin("Oliwia", "admin", "a"))
