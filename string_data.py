
"""
Module 2 Challenge
Description: String Experimentation, Variables, and Formatted Printing
Author: Akmal Elsayed
MIT License, 2026
"""

print(f'\nWelcome to Module 2: Comments, Variables, and Formatted Printing')

"""
Triple-double-quoted strings are commonly used as docstrings. 
They allow developers to document modules, functions, and classes.
Docstrings can also be accessed by documenetation tools and IDEs. 
"""
# System Variables
system_label = "CORE_OS_v2.6"
user_name ="Admin User"
access_level = 4

# Simulated output
print(f"[{system_label}] Initializing boot sequence...")
print(f"[{system_label}] Welcome back {user_name}. ")
print(f"[{system_label}] Current Access Level: {access_level}")
print(f"----------------------------------------")
print(f"Status: Secure connection established.")

my_name = 'Akmal'
print(f'Your preferred name is: {my_name}')

print(f'Uppercase: {my_name.upper()}')
print(f'Capitalized: {my_name.capitalize()}')
print(f'Title Case: {my_name.title()}')
print(f'Count of "r" {my_name.count("r")}')
