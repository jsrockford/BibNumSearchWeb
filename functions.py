from data import *

def validate_input(user_input):
    if user_input.isdigit():
        if 2 <= len(user_input) <= 6:
            return True
        else:
            print("Please number 2 to 6 digits only!\n")
            return False
    else:
        print("Please enter only number 2 to 6 digits in length!\n")
        return False


# Converts user entered numbers to chapt:verse combos LIST
def convert_to_search(user_input):
    # separate digits into LIST
    num_list = []
    for i in user_input:
        num_list.append(i)

    tmp_results = []
    search_src = []
    for i in range(0, len(num_list)-1):
        tmp_list = num_list.copy()
        if i < len(num_list):
            tmp_list.insert(i + 1, ":")
            tmp_results.append(tmp_list)
            i += 1

    # code to join results into one string per entry
    a = 0
    s = ""
    while a < len(tmp_results):
        tmp_hold = tmp_results[a]
        s = "".join(tmp_hold)
        search_src.append(s)
        a += 1

    return search_src     # returns list of formatted scriptures to use in Bible search


def test_match(test_numbers):   # replaced test_numbers with user_numbers_list
    results = []
    for num_list in test_numbers:
        for line in kjv_text:
            if num_list == line[1]:
                results.append(line)
    return results