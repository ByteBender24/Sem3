'''
Create a project that simulates a university's course registration system. There should be a class hierarchy for different types of courses, each with specific properties and methods.Create a base class called Course with a constructor that accepts the course_code, course_name, and 
credit_hours as positional arguments. Initialize these instance variables in the constructor.Create three derived classes: CoreCourse, ElectiveCourse, and LabCourse, each inheriting from the
Course class. These derived classes should accept any number of positional arguments (*args) andkeyword arguments (**kwargs) during initialization. Each derived class should override the __init__
method to add additional properties specific to that type of course.For example, CoreCourse courses can have a required_prerequisites property, ElectiveCourse
courses can have an available_terms property, and LabCourse courses can have a lab_location property. Implement a method called course_info in each derived class that prints information about
the course, including its code, name, credit hours, and any additional properties specific to that type of course.Create instances of various courses from each category (e.g., a core course, an elective course, and a
lab course) with different codes, names, credit hours, and additional properties. Demonstrate that each course object can accept different arguments during initialization and correctly display itsinformation using the course_info method.

Open-ended question section:
Extend the code such that it will demonstrate the diamond inheritance property with overriding of
some few variables and use (*args) and keyword arguments (**kwargs) in the inherited polymorphic
functions other than __init__.

Author : Harishraj S
Date : 04-10-2023
'''


class Course:

    def __init__(self, course_code, course_name, credit_hours):
        """
        Initialize a Course object.

        Args:
        course_code (str): The code of the course.
        course_name (str): The name of the course.
        credit_hours (int): The number of credit hours for the course.
        """
        self.course_code = course_code
        self.course_name = course_name
        self.credit_hours = credit_hours

    def course_info(self):
        """
        Get information about the course.

        Returns:
        str: A formatted string containing course information.
        """
        return f"course_code: {self.course_code}\ncourse_name: {self.course_name}\ncredit_hours: {self.credit_hours}"


class LabCourse(Course):

    def __init__(self, course_code, course_name, credit_hours, *args, **kwargs):
        """
        Initialize a LabCourse object.

        Args:
        course_code (str): The code of the course.
        course_name (str): The name of the course.
        credit_hours (int): The number of credit hours for the course.
        *args: (lab_location) Additional positional arguments.
        **kwargs: Additional keyword arguments.
        """
        super().__init__(course_code, course_name, credit_hours)
        self.lab_location = args
        self.other_info = kwargs

    def course_info(self):
        """
        Get information about the lab course.

        Returns:
        str: A formatted string containing lab course information.
        """
        course_info = super().course_info()
        if self.lab_location != ():
            course_info += "\nLab Locations:"
            for labs in self.lab_location:
                if self.lab_location.index(labs) == len(self.lab_location)-1:
                    course_info += f"{labs}"
                    break
                course_info += f"{labs},"
        if self.other_info != {} and isinstance(self.other_info, dict):
            for info_key, info_value in self.other_info.items():
                course_info += f"\n{info_key}: {info_value}"
        return course_info


class ElectiveCourse(Course):

    def __init__(self, course_code, course_name, credit_hours, *args, **kwargs):
        """
        Initialize an ElectiveCourse object.

        Args:
        course_code (str): The code of the course.
        course_name (str): The name of the course.
        credit_hours (int): The number of credit hours for the course.
        *args: (available_terms) Additional positional arguments.
        **kwargs: Additional keyword arguments.
        """
        super().__init__(course_code, course_name, credit_hours)
        self.available_terms = args
        self.other_info = kwargs

    def course_info(self):
        """
        Get information about the elective course.

        Returns:
        str: A formatted string containing elective course information.
        """
        course_info = super().course_info()
        if self.available_terms != ():
            course_info += "\nAvailable Terms:"
            for term in self.available_terms:
                if self.available_terms.index(term) == len(self.available_terms)-1:
                    course_info += f"{term}"
                    break
                course_info += f"{term},"
        if self.other_info != {} and isinstance(self.other_info, dict):
            for info_key, info_value in self.other_info.items():
                course_info += f"\n{info_key}: {info_value}"
        return course_info


class CoreCourse(Course):

    def __init__(self, course_code, course_name, credit_hours, *args, **kwargs):
        """
        Initialize a CoreCourse object.

        Args:
        course_code (str): The code of the course.
        course_name (str): The name of the course.
        credit_hours (int): The number of credit hours for the course.
        *args: (required_prerequisites) Additional positional arguments.
        **kwargs: Additional keyword arguments.
        """
        super().__init__(course_code, course_name, credit_hours)
        self.required_prerequisites = args
        self.other_info = kwargs

    def course_info(self):
        """
        Get information about the core course.

        Returns:
        str: A formatted string containing core course information.
        """
        course_info = super().course_info()
        if self.required_prerequisites != ():
            course_info += "\nRequired Prerequisites:"
            for prerequisite in self.required_prerequisites:
                if self.required_prerequisites.index(prerequisite) == len(self.required_prerequisites)-1:
                    course_info += f"{prerequisite}"
                    break
                course_info += f"{prerequisite},"
        if self.other_info != {} and isinstance(self.other_info, dict):
            for info_key, info_value in self.other_info.items():
                course_info += f"\n{info_key}: {info_value}"
        return course_info

class Core_cum_Elective(CoreCourse, ElectiveCourse):

    def __init__(self, course_code, course_name, credit_hours, **kwargs):
        super().__init__(course_code, course_name, credit_hours, **kwargs)
        self.required_prerequisites = kwargs.get('required_prerequisites')
        self.available_terms = kwargs.get('available_terms')
        self.other_info = kwargs.get('other_info')

    def course_info(self):
        return super().course_info()

if __name__ == "__main__":

    Core_cum_Elective1 = Core_cum_Elective("CCE1", "TEE", 79, required_prerequisites=[
                                           "PDP", "Python"], available_terms=["Summer", "Winter"], other_info={"nawa": "name"})
    print(Core_cum_Elective1.course_info())

