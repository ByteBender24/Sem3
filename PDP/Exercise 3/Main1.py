'''
Create Application to receive the personal details from a student for a competitions for under 17
Age category. Check the age using the packages and accept only the children of age 17 or less. The
registration is valid for 6 month. When person shows the registration details, check and display,
whether its valid today, with respect to age and registration Date.

Author : Harishraj S
Date : 27-09-2023
'''

from Date import Convert, Current, Date, Difference, Validity


class Student:

    def __init__(self, name, dob, contact, date_registered, achievements=None):
        self.name = name
        self.dob = Date.date_obj_converter(dob, '%d.%m.%Y')
        self.contact = contact
        self.achievements = achievements
        self.registration_date = date_registered

    def is_valid_registered(self):
        days = Difference.difference_with_current(self.registration_date)
        if days >= 180:
            return False
        return True

    def is_valid(self):
        '''
        Checks the given date is below or equal to 17 years from the registration date

        Return : bool (True / False)
        '''
        days = Difference.difference(self.dob, self.registration_date)
        years = abs(Convert.convert_days_years(days))
        if years <= 17:
            return True
        return False


class DateError(Exception):
    pass


class Valid_students:

    def __init__(self, list_of_valid_students=[]):
        self.list = list_of_valid_students

    def remove_student(self, name, dob=None):
        obj = self.identify_student(name, dob)
        self.list.remove(obj)
        del obj

    def identify_student(self, name, dob=None):
        for _ in self.list:
            if (_.name, _.dob) == (name, dob):
                return _

    def add_student(self, obj: Student):
        self.list.append(obj)

    def remove_expired(self):
        for _ in self.list:
            if not _.is_valid_registered():
                self.list.remove(_)

    def __str__(self):
        return str(self.list)

    def show_students(self):
        self.remove_expired()
        return self.list
    
def get_details():
    name = input("Enter name :")
    dob = input("Enter dob as dd.mm.yyyy format:")
    if not Validity.is_valid_date(dob):
        raise DateError("Enter valid date!")
    contact = input("Enter contact number:")
    date_registered = Current.current_date()
    date_registered = Date.date_obj_converter(date_registered, "%d.%m.%Y")
    achievements = input("Enter achievements (If ANY!):")

    if achievements == "":
        achievements = None

    return Student(name, dob, contact, date_registered, achievements)

def main():
    students_valid = Valid_students()

    while True:
        print("Student Registration for Under 17 Age Category")
        print("Enter 'q' to quit.")

        try:
            student = get_details()
            if student.is_valid():
                print (student.is_valid())
                students_valid.add_student(student)
                print("Student registration successful!")
            else:
                print("Student is not eligible for the competition.")
        except DateError as e:
            print(f"Error: {e}")

        print (students_valid)

        choice = input("Do you want to register another student? (y/n): ")
        if choice.lower() != 'y':
            break
    
    

    # Remove expired registrations
    students_valid.remove_expired()

    print("\nValid Registrations:")
    for student in students_valid.show_students():
        print(f"Name: {student.name}, DOB: {student.dob}, Contact: {student.contact}")

if __name__ == "__main__":
    main()

