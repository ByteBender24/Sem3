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
