"""
OOP Fundamentals Exercise
------------------------
Complete the following classes according to the specified requirements.
This exercise covers basic object-oriented programming concepts in Python.
"""

class BankAccount:
    """
    A class representing a simple bank account.
    
    Attributes:
        account_number (str): The account number
        owner_name (str): The name of the account owner
        balance (float): The current balance
        
    Methods:
        deposit(amount): Add the specified amount to the balance
        withdraw(amount): Subtract the specified amount from the balance if funds are available
        get_balance(): Return the current balance
        add_interest(rate): Add interest to the balance based on the given rate
    """
    
    def __init__(self, account_number, owner_name, initial_balance=0):
        """
        Initialize a new BankAccount instance.
        
        Args:
            account_number (str): The account number
            owner_name (str): The name of the account owner
            initial_balance (float, optional): The starting balance. Defaults to 0.
        """
        # YOUR CODE HERE
        pass
    
    def deposit(self, amount):
        """
        Add the specified amount to the balance.
        
        Args:
            amount (float): The amount to deposit
            
        Returns:
            float: The new balance
            
        Raises:
            ValueError: If amount is negative
        """
        # YOUR CODE HERE
        pass
    
    def withdraw(self, amount):
        """
        Subtract the specified amount from the balance if funds are available.
        
        Args:
            amount (float): The amount to withdraw
            
        Returns:
            float: The new balance
            
        Raises:
            ValueError: If amount is negative
            ValueError: If insufficient funds
        """
        # YOUR CODE HERE
        pass
    
    def get_balance(self):
        """
        Return the current balance.
        
        Returns:
            float: The current balance
        """
        # YOUR CODE HERE
        pass
    
    def add_interest(self, rate):
        """
        Add interest to the balance.
        
        Args:
            rate (float): The interest rate as a decimal (e.g., 0.05 for 5%)
            
        Returns:
            float: The new balance
        """
        # YOUR CODE HERE
        pass


class Rectangle:
    """
    A class representing a rectangle.
    
    Attributes:
        width (float): The width of the rectangle
        height (float): The height of the rectangle
        
    Methods:
        area(): Calculate the area of the rectangle
        perimeter(): Calculate the perimeter of the rectangle
        is_square(): Check if the rectangle is a square
        scale(factor): Scale the rectangle by the given factor
    """
    
    def __init__(self, width, height):
        """
        Initialize a new Rectangle instance.
        
        Args:
            width (float): The width of the rectangle
            height (float): The height of the rectangle
            
        Raises:
            ValueError: If width or height is not positive
        """
        # YOUR CODE HERE
        pass
    
    def area(self):
        """
        Calculate the area of the rectangle.
        
        Returns:
            float: The area (width * height)
        """
        # YOUR CODE HERE
        pass
    
    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.
        
        Returns:
            float: The perimeter (2 * width + 2 * height)
        """
        # YOUR CODE HERE
        pass
    
    def is_square(self):
        """
        Check if the rectangle is a square.
        
        Returns:
            bool: True if width equals height, False otherwise
        """
        # YOUR CODE HERE
        pass
    
    def scale(self, factor):
        """
        Scale the rectangle by the given factor.
        
        Args:
            factor (float): The scaling factor
            
        Returns:
            Rectangle: A new Rectangle instance with scaled dimensions
            
        Raises:
            ValueError: If factor is not positive
        """
        # YOUR CODE HERE
        pass


class Student:
    """
    A class representing a student.
    
    Attributes:
        name (str): The student's name
        student_id (str): The student's ID
        courses (dict): Dictionary mapping course names to grades
        
    Methods:
        add_course(course_name, grade): Add a course and grade to the student's record
        get_gpa(): Calculate the student's GPA (average of all grades)
        get_courses(): Get a list of all courses the student is taking
        is_passing(): Check if the student is passing all courses (grade >= 60)
    """
    
    def __init__(self, name, student_id):
        """
        Initialize a new Student instance.
        
        Args:
            name (str): The student's name
            student_id (str): The student's ID
        """
        # YOUR CODE HERE
        pass
    
    def add_course(self, course_name, grade):
        """
        Add a course and grade to the student's record.
        
        Args:
            course_name (str): The name of the course
            grade (float): The grade received (0-100)
            
        Raises:
            ValueError: If grade is not between 0 and 100
        """
        # YOUR CODE HERE
        pass
    
    def get_gpa(self):
        """
        Calculate the student's GPA (average of all grades).
        
        Returns:
            float: The GPA, or 0.0 if no courses
        """
        # YOUR CODE HERE
        pass
    
    def get_courses(self):
        """
        Get a list of all courses the student is taking.
        
        Returns:
            list: A list of course names
        """
        # YOUR CODE HERE
        pass
    
    def is_passing(self):
        """
        Check if the student is passing all courses (grade >= 60).
        
        Returns:
            bool: True if all courses have a grade of 60 or higher, False otherwise
            If no courses, returns True
        """
        # YOUR CODE HERE
        pass


def main():
    """Test the classes with some examples."""
    # Test BankAccount
    print("Testing BankAccount class...")
    account = BankAccount("12345", "Alice Smith", 1000)
    account.deposit(500)
    account.withdraw(200)
    account.add_interest(0.05)
    print(f"Account balance: ${account.get_balance():.2f}")
    
    # Test Rectangle
    print("\nTesting Rectangle class...")
    rect = Rectangle(5, 10)
    print(f"Rectangle area: {rect.area()}")
    print(f"Rectangle perimeter: {rect.perimeter()}")
    print(f"Is square? {rect.is_square()}")
    square = Rectangle(5, 5)
    print(f"Square area: {square.area()}")
    print(f"Is square? {square.is_square()}")
    
    # Test Student
    print("\nTesting Student class...")
    student = Student("Bob Johnson", "S12345")
    student.add_course("Math", 85)
    student.add_course("History", 92)
    student.add_course("Science", 78)
    print(f"Courses: {student.get_courses()}")
    print(f"GPA: {student.get_gpa():.2f}")
    print(f"Is passing all courses? {student.is_passing()}")

if __name__ == "__main__":
    main()