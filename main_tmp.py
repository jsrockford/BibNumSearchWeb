# Bible Number Lookup program to be renamed better later
# Program takes 2-6 digit user number input then returns "Book Chapter:Verse - Text" formatted results
from functions import *
import textwrap as tr


valid = False
while not valid:
    my_number = input("Enter your number [2 to 6 digits]: ")
    valid = validate_input(my_number)

src_numbers = convert_to_search(my_number)

answer = test_match(src_numbers)   # changed program to search kjv_text directly

for scripture in answer:
    line = f"{scripture[0]} {scripture[1]} - {scripture[2]}"
    print(tr.fill(line, width=140))