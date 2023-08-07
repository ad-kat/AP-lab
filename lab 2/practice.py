import random


def read_dictionary_from_user():
    dictionary = {}
    while True:
        key = random.randrange(0, 100)
        value = input("Enter the value for key {}: ".format(key))
        if value == "-999":
            break
        if value.isdigit():
            dictionary[key] = int(value)
        else:
            dictionary[key] = value

    return dictionary


def find_avg(dictionary):
    num_sum = 0
    tot = 0
    for value in dictionary.values():
        if value.isdigit():
            num_sum += value
            tot += 1

    the_avg = num_sum / tot
    return the_avg


def concat_str(dictionary):
    constr = ""
    for value in dictionary.values():
        if type(value) == str:
            constr += value

    return constr


def search_for_it(term, dictionary):
    flag = 0
    ans = 0
    for index, value in dictionary:
        if type(value) == str:
            if value == term:
                flag = 100
                ans = index
    if flag == 100:
        print("found at index", ans)
    else:
        print("not found anywhere")


def print_special(dictionary):
    spec = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"

    for value in dictionary.values():
        all_chars = 1
        if type(value) == str:
            for letter in value:
                if letter not in spec:
                    continue
                else:
                    all_chars = 100
                    break
        if all_chars == 1:
            print(value)


def quest():
    dictionary = read_dictionary_from_user()

    the_average = find_avg(dictionary)
    print("The average of the numbers in the dictionary is: {}.".format(the_average))

    concatenated_strings = concat_str(dictionary)
    print("The concatenated strings in the dictionary are: {}".format(concatenated_strings))

    search_term = input("Enter the string to search for: ")
    search_for_it(search_term, dictionary)

    print_special(dictionary)


quest()
