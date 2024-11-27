import logging

#Create a logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

#Create a file handler and a stream handler
file_handler = logging.FileHandler('university.log')
stream_handler = logging.StreamHandler()

#Create a formatter and set it for the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)

#Add the handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(stream_handler)

class University:
    """
    Represents a university with a name and a list of departments.

    Attributes:
        name (str): The name of the university.
        departments (list): A list of Department objects.
    """

    def __init__(self, name):
        """
        Initializes a University object with a name and an empty list of departments.

        Args:
            name (str): The name of the university.
        """
        self.name = name
        self.departments = []
        logger.info(f"University '{name}' created.")

    def add_department(self, department):
        """
        Adds a department to the university's list of departments.

        Args:
            department (Department): The department to add.
        """
        self.departments.append(department)
        logger.info(f"Department '{department.name}' added to university '{self.name}'.")

    def display_departments(self):
        """
        Displays the list of departments in the university.
        """
        logger.info(f"Displaying departments for university '{self.name}':")
        for department in self.departments:
            print(department)

class Department:
    """
    Represents a department with a name and a list of courses.

    Attributes:
        name (str): The name of the department.
        courses (list): A list of Course objects.
    """

    def __init__(self, name):
        """
        Initializes a Department object with a name and an empty list of courses.

        Args:
            name (str): The name of the department.
        """
        self.name = name
        self.courses = []
        logger.info(f"Department '{name}' created.")

    def add_course(self, course):
        """
        Adds a course to the department's list of courses.

        Args:
            course (Course): The course to add.
        """
        self.courses.append(course)
        logger.info(f"Course '{course.name}' added to department '{self.name}'.")

    def display_courses(self):
        """
        Displays the list of courses in the department.
        """
        logger.info(f"Displaying courses for department '{self.name}':")
        for course in self.courses:
            print(course)

    def __str__(self):
        """
        Returns a string representation of the department.
        """
        return f"{self.name} Department"

class Course:
    """
    Represents a course with a name, credits, and a list of students.

    Attributes:
        name (str): The name of the course.
        credits (int): The number of credits for the course.
        students (list): A list of Student objects.
    """

    def __init__(self, name, credits):
        """
        Initializes a Course object with a name, credits, and an empty list of students.

        Args:
            name (str): The name of the course.
            credits (int): The number of credits for the course.
        """
        self.name = name
        self.credits = credits
        self.students = []
        logger.info(f"Course '{name}' created.")

    def add_student(self, student):
        """
        Adds a student to the course's list of students.

        Args:
            student (Student): The student to add.
        """
        self.students.append(student)
        logger.info(f"Student '{student.name}' added to course '{self.name}'.")

    def display_students(self):
        """
        Displays the list of students in the course.
        """
        logger.info(f"Displaying students for course '{self.name}':")
        for student in self.students:
            print(student)

    def __str__(self):
        """
        Returns a string representation of the course.
        """
        return f"{self.name} ({self.credits} credits)"

class Student:
    """
    Represents a student with a name and a roll number.

    Attributes:
        name (str): The name of the student.
        roll_number (str): The roll number of the student.
    """

    def __init__(self, name, roll_number):
        """
        Initializes a Student object with a name and a roll number.

        Args:
            name (str): The name of the student.
            roll_number (str): The roll number of the student.
        """
        self.name = name
        self.roll_number = roll_number
        logger.info(f"Student '{name}' created.")

    def __str__(self):
        pass

def main():
    # Create a university
    university = University("Example University")

    # Create departments
    department1 = Department("Computer Science")
    department2 = Department("Mathematics")

    # Create courses
    course1 = Course("Data Structures", 3)
    course2 = Course("Algorithms", 4)
    course3 = Course("Calculus", 3)

    # Create students
    student1 = Student("John Doe", "CS101")
    student2 = Student("Jane Smith", "CS102")
    student3 = Student("Bob Johnson", "MATH101")

    # Add courses to departments
    department1.add_course(course1)
    department1.add_course(course2)
    department2.add_course(course3)

    # Add students to courses
    course1.add_student(student1)
    course1.add_student(student2)
    course2.add_student(student3)

    # Add departments to university
    university.add_department(department1)
    university.add_department(department2)

    # Display university information
    print("University Departments:")
    university.display_departments()

    print("\nDepartment 1 Courses:")
    department1.display_courses()

    print("\nDepartment 2 Courses:")
    department2.display_courses()

    print("\nCourse 1 Students:")
    course1.display_students()

    print("\nCourse 2 Students:")
    course2.display_students()

if __name__ == "__main__":
    main()


