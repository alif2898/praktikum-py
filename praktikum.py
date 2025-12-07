# Latihan Praktikum
#Soal nomor 1
n = 'alif'
print(type(n))
print(n)

u = 17
print(type(u))
print(u)

list = ['a','b','c','d']
list.append('Alif')
list.insert(5,'Alif')
list.extend(['Dapong','Briun'])
print(list)


#Latihan OOP Python
# Test case 1 : Even or Odd
def even_odd(num): 
    return f"The number is {'Even' if num % 2 == 0 else 'Odd'}"

# Test
print(even_odd(4))  # Expected: The number is Even
print(even_odd(7))  # Expected: The number is Odd


# Test case 2 : Positive, Negative, or Zero
def pos_neg_zero(num): return f"The number is {'Positive' if num > 0 else 'Negative' if num < 0 else 'Zero'}"

# Test
print(pos_neg_zero(10))  # Expected: The number is Positive
print(pos_neg_zero(-5))  # Expected: The number is Negative
print(pos_neg_zero(0))   # Expected: The number is Zero


# Test case 3 : Check for Anagrams
def is_anagram(str1, str2): return sorted(str1) == sorted(str2)

# Test
print(is_anagram("listen", "silent"))  # Expected: True
print(is_anagram("hello", "world"))    # Expected: False


# Test case 4 : Factorial
def factorial(n): return 1 if n == 0 else n * factorial(n - 1)

# Test
print(factorial(5))  # Expected: 120
print(factorial(0))  # Expected: 1


# Test case 5 : Palindrome
def is_palindrome(s): return s == s[::-1]

# Test
print(is_palindrome("racecar"))  # Expected: True
print(is_palindrome("python"))   # Expected: False
print(is_palindrome("habibah"))  # Expected: True


# Test case 6 : Armstrong Number
def is_armstrong(num): return num == sum(int(digit) ** len(str(num)) for digit in str(num))

# Test
print(is_armstrong(153))  # Expected: True
print(is_armstrong(370))  # Expected: True
print(is_armstrong(123))  # Expected: False


# Test case 7 : Bank Account Class
class BankAccount:
    def _init_(self, name): self.name, self.balance = name, 0
    def deposit(self, amount):
        self.balance += amount
        return f"Deposited {amount}. New balance: {self.balance}"
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f"Withdrew {amount}. New balance: {self.balance}"
        return "Invalid withdrawal amount or insufficient funds"

# Test
account = BankAccount("Name")
print(account.deposit(1000))  # Expected: Deposited 1000. New balance: 1000
print(account.withdraw(500))  # Expected: Withdrew 500. New balance: 500
print(account.withdraw(600))  # Expected: Invalid withdrawal amount or insufficient funds


# Test case 8 : Student Class
class Student:
    def _init_(self, name): self.name, self.grades = name, []
    def add_grade(self, grade):
        self.grades.append(grade)
        return f"Grade {grade} added."
    def get_average(self):
        return f"Average grade: {sum(self.grades)/len(self.grades)}" if self.grades else "No grades available."

# Test
student = Student("Alice")
print(student.add_grade(90))  # Expected: Grade 90 added.
print(student.add_grade(80))  # Expected: Grade 80 added.
print(student.add_grade(70))  # Expected: Grade 70 added.
print(student.get_average())  # Expected: Average grade: 80.0
