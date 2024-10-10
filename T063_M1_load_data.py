# Maulik Khanna
# Tarik Kartal
# Ayra Mensah
# Tania Pillay


import T063_M1_load_data
import string
from typing import List
import T063_M1_load_data as ld
#from check_equal import check_equal


def student_school_dictionary(file_name: str) -> dict:
    '''The function opens and reads a .csv file, checks for the name of the school in each line of the file and gathers all other data such age, health etc that are associated directly with each school name intials, it then adds each of those data values in individual lists and finally adds all those data values for each school name intials to a dictionary as a value with the key being the name initials of each school
    '''

    file = open(file_name)  # opens the file
    count = 0  # count variable starts to count the iteration for reading through the lines
    student_school = {}  # empty dictionary is created
    for line in file:  # a for loop used to read each line of the file

        # strip and split functions are used to remove commas and newline characters that are added to each last key of the dictionary by default
        row = line.strip('\n').split(',')
        if count == 0:
            column = row
        else:
            if row[0] not in student_school:

                # empty list created for first key value pair
                student_school[row[0]] = []
            student_data = {}  # empty dictionary created

            # each of these values refer to the relation of column and row using their index positions to add specific keys and their values to the dictionary
            student_data[column[1]] = int(row[1])
            student_data[column[2]] = float(row[2])
            student_data[column[3]] = int(row[3])
            student_data[column[4]] = int(row[4])
            student_data[column[5]] = int(row[5])
            student_data[column[6]] = int(row[6])
            student_data[column[7]] = int(row[7])
            student_data[column[8]] = int(row[8])
            # this dictionary defines the main key for the entire large dictionary which in this case is the school name initials and it's related keys and values will be added to the this dictionary
            student_school[row[0]].append(student_data)
        count += 1  # after iterating each line which is a combination of columns and row, the count will increase by one to get to the next line and repeat this entire proccess untill the whole file has been read
    file.close()  # after the reading of the file is done, it is closed
    return student_school  # the final main dictionary is returned by the function


# Function 2


def student_health_dictionary(file_name: str) -> dict:
    """ Returns a dictionary that uses students health state level as key of
    dictionary and the other elemets of a list as values.
    precondition = file is a string representing the path of csv file
    """
    student_health = {1: [], 2: [], 3: [], 4: [],
                      5: []}  # set up dictionary that keys health
    openup = open(file_name)
    next(openup)  # built-in function, will skip to the next row in the file.
    for line in openup:  # goes through every line from student_health
        # removes commas, and will places the variables.
        line = line.split(',')
        result = {'School': line[0], 'Age': int(line[1]), 'StudyTime': float(line[2]), 'Failures': int(line[3]),
                  'Absences': int(line[5]), 'G1': int(line[6]), 'G2': int(line[7]), 'G3': int(line[8].strip('\n'))}  # all of the items in the list is transported to this dictionary, except health
        student_health[int(line[4])] += [result]
    openup.close()
    return student_health


# Function 3

def student_age_dictionary(file_name: str) -> dict:
    """Return a dictionary that uses the students' ages as the key and the 
    other elements of the list as values.

    Preconditions: filename should be a .csv file.
    """
    student_age_dictionary = {15: [], 16: [], 17: [], 18: [], 19: [],
                              20: [], 21: [], 22: []}  # assigns dictionary. line[2], 'Health'
    file = open(file_name)
    next(file)

    for line in file:
        line = line.strip('\n').split(",")

        element = {'School': str(line[0]), 'StudyTime': float(line[2]), 'Failures': int(line[3]),
                   'Health': int(line[4]), 'Absences': int(line[5]), 'G1': int(line[6]), 'G2': int(line[7]), 'G3': int(line[8])}
        student_age_dictionary[int(line[1])] += [element]

    file.close()  # student_age_dictionary shows an output return student_age_dictionary
    return student_age_dictionary


# Function 4


def student_failures_dictionary(file_name: str) -> dict:
    """Return a dictionary that uses the students' failures as the key and the 
    other elements of the list as values.

    Preconditions: filename should be a .csv file

    """

    student_failures_dictionary = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [
    ], 8: [], 9: [], 10: []}  # assigns dictionary and states range of students' failures

    file = open(file_name)
    # this skips the first line of the file which is thr row containing headers (keys)
    next(file)

    for line in file:  # iterates through the lines
        # places values as items in the list while removing each comma
        line = line.strip("\n").split(",")

        element = {'School': str(line[0]), 'Age': int(line[1]), 'StudyTime': float(line[2]), 'Health': int(line[4]), 'Absences': int(line[5]), 'G1': int(line[6]),
                   'G2': int(line[7]), 'G3': int(line[8])}  # elements that can be used for each list excluding the failures column

        student_failures_dictionary[int(line[3])] += [element]

    file.close()  # student_failures_dictionary shows as an output
    return student_failures_dictionary


# Load Data function


def load_data(file_name: str, dict_type: str) -> dict:
    '''This function checks the parameters when it is called, first, the file name and second, a string based on how a dictionary should be displayed out of certain factors like School name initials, Health, Age or Failures. After valid parameters are called, the function returns a dictionary based on the dictioary type as a key that was provided as a second parameter to the function. If the dict_type does not have a valid string as it intended, the function will print a message of Inwalid Key and return an empty string.
    '''
    empty_dict = {}
    if dict_type == 'School':
        return student_school_dictionary(file_name)

    elif dict_type == 'Health':
        return student_health_dictionary(file_name)

    elif dict_type == 'Age':
        return student_age_dictionary(file_name)

    elif dict_type == 'Failures':
        return student_failures_dictionary(file_name)

    else:
        print('Invalid Key')
        return empty_dict


# Add average function


def add_average(dict_final: dict) -> dict:
    '''This function calculates the average of 3 grades of different students from a particular dictionary with different keys and adds them to that dictionary and returns an updated version of that dictionary
    '''

    for key in dict_final.keys():
        for j in dict_final[key]:
            G1 = j.get('G1')
            G2 = j.get('G2')
            G3 = j.get('G3')
            G_avg = round((int(G1) + int(G2) + int(G3)) / 3)
            j['G_Avg'] = G_avg
    return(dict_final)


# All function calls
student_school_dictionary('student-mat.csv')
student_health_dictionary('student-mat.csv')
student_age_dictionary('student-mat.csv')
student_failures_dictionary('student-mat.csv')

load_data('student-mat.csv', 'School')
load_data('student-mat.csv', 'Age')
load_data('student-mat.csv', 'Health')
load_data('student-mat.csv', 'Failures')


add_average(student_school_dictionary('student-mat.csv'))
add_average(student_health_dictionary('student-mat.csv'))
add_average(student_age_dictionary('student-mat.csv'))
add_average(student_failures_dictionary('student-mat.csv'))


def check_equal_keys() -> None:
    '''The function checks if the expected keys from the dictionaries of lab 3 match the list of actual keys or not. Based on this, the function counts the number of expected and actual list of keys and returns the total number of passed and failed cases after all cases are tested
    '''
    total_tests = 0
    count1 = 0
    count2 = 0
    actual_school = ['GP', 'MB', 'CF', 'BD', 'MS']
    actual_age = [15, 16, 17, 18, 19, 20, 21, 22]
    actual_health = [1, 2, 3, 4, 5]
    actual_failures = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    if list(load_data('student-mat.csv', 'School').keys()) == actual_school:
        count1 += 1
        total_tests += 1
    else:
        count2 += 1
        total_tests += 1
    if list(load_data('student-mat.csv', 'Age').keys()) == actual_age:
        count1 += 1
        total_tests += 1
    else:
        count2 += 1
        total_tests += 1
    if list(load_data('student-mat.csv', 'Health').keys()) == actual_health:
        count1 += 1
        total_tests += 1
    else:
        count2 += 1
        total_tests += 1
    if list(load_data('student-mat.csv', 'Failures').keys()) == actual_failures:
        count1 += 1
        total_tests += 1
    else:
        count2 += 1
        total_tests += 1

    print("\n")
    print("Total number of tests for TEST 1 = ", total_tests)
    print("Number of Tests Passed = {}. \nNumber of Tests Failed = {}.".format(
        count1, count2))


check_equal_keys()


def check_equal_size(file_name: dict) -> bool:
    """ examines if given dictionary has correct number of keys in total. 
    if they are equal, the code will display test passed, following with; number
    of test passed, True.
    """
    count = 0  # assigns 0 to count vaulue to define count
    for key in file_name.keys():  # for given parameter, goes through every key in the dictionary
        count += len(file_name.get(key))
        # adds up every key in the dictionary to the initialized count value
    if count == 395:  # if count = actual value, it will print statement below
        result = True
    elif count != 395:  # if count != actual value, it will print statement below
        result = False
    else:  # if file is in wrong type, it will print statement below
        result = False
    return result


control = [check_equal_size(student_school_dictionary('student-mat.csv')), check_equal_size(student_health_dictionary('student-mat.csv')),
           check_equal_size(student_age_dictionary('student-mat.csv')), check_equal_size(student_failures_dictionary('student-mat.csv'))]

passed_tests = 0
failed_tests = 0
total_tests = 0
for i in control:  # for every function in the load_data, check if they passed or failed. than displays the numbers related.
    if i == True:
        passed_tests += 1
        total_tests += 1
    else:
        failed_tests += 1
        total_tests += 1
print("\n")
print("Total number of tests for TEST 2 = ", total_tests)
print("Number of passed tests = ", passed_tests)
print("Number of failed tests = ", failed_tests)


def check_equal_entries() -> bool:
    """
    This function checks the number of student entries to make sure they are in the correct format/order for all 4 dictionaries.

    Preconditions: Individual student + the value(in key:value pair) we want to test is already loaded into the test.

    example:
    >>>check_equal_entries(T063_M1_load_data.load_data('student-mat.csv', 'School'), "School")
    True


    """
    values1 = load_data('student-mat.csv', 'School')['GP'][0]
    values2 = load_data('student-mat.csv', 'Age')[15][0]
    values3 = load_data('student-mat.csv', 'Health')[1][0]
    values4 = load_data('student-mat.csv', 'Failures')[0][0]

    if values1 == {'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6}:
        return True
    else:
        return False

    if values2 == {' School': 'GP', 'StudyTime': 2.0, 'Failures': 3, 'Health': 3, 'Absences': 10, 'G1': 7, 'G2': 8, 'G3': 10}:
        return True
    else:
        return False

    if values3 == {' School': 'GP', 'Age': 17, 'StudyTime': 2.0, 'Failures': 0, 'Absences': 6, 'G1': 6, 'G2': 5, 'G3': 6}:
        return True
    else:
        return False

    if values4 == {' School': 'GP', 'Age': 18, 'StudyTime': 2.0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6}:
        return True
    else:
        return False


check = [check_equal_entries(), check_equal_entries(),
         check_equal_entries(), check_equal_entries()]

passed = check.count(True)
failed = check.count(False)

print("\n")
print(
    f"Total Number of tests for TEST 3 = {passed + failed}  \nNumber of tests passed= {passed} \nNumber of tests failed = {failed}")
check_equal_entries()


def check_equal_add_average(student_school_dictionary: dict, student_health_dictionary: dict, student_age_dictionary: dict, student_failures_dictionary: dict, add_average: dict) -> None:
    """
    This function checks if the number of students in all four dictionaries is correct 
    checks if G_Avg calculation is correct in all four dictionaries and also checks if G_Avg key is in all four dictionaries.

    Preconditions: None

    """

    # assigning variables
    total_tests = 0
    Total_passed = 0
    Total_failed = 0
    tests_passed = 0
    tests_failed = 0
    # check if G_Avg is in dictionary
    # checks if G_Avg is in School dict
    if "G_Avg" in list(ld.add_average(ld.load_data("student-mat.csv", "School")).values())[0][0]:
        tests_passed += 1
        total_tests += 1
    else:
        tests_failed += 1
        total_tests += 1

    # checks if G_Avg is in Health dict
    if "G_Avg" in list(ld.add_average(ld.load_data("student-mat.csv", "Health")).values())[0][0]:
        tests_passed += 1
        total_tests += 1
    else:
        tests_failed += 1
        total_tests += 1

    # checks if G_Avg is in Age dict
    if "G_Avg" in list(ld.add_average(ld.load_data("student-mat.csv", "Age")).values())[0][0]:
        tests_passed += 1
        total_tests += 1
    else:
        tests_failed += 1
        total_tests += 1

    # checks if G_Avg is in Failures in dict
    if "G_Avg" in list(ld.add_average(ld.load_data("student-mat.csv", "Failures")).values())[0][0]:
        tests_passed += 1
        total_tests += 1
    else:
        tests_failed += 1
        total_tests += 1

     # check if G_Avg is correct
    school_actual = list(ld.add_average(ld.load_data(
        "student-mat.csv", "School")).values())[0][0].get("G_Avg")  # gets G_Avg from school dict
    school_expected_G_Avg = round((6 + 6 + 5) / 3, 0)
    if school_actual == school_expected_G_Avg:
        tests_passed += 1
        total_tests += 1
    else:
        tests_failed += 1
        total_tests += 1

    health_actual = list(ld.add_average(ld.load_data(
        "student-mat.csv", "Health")).values())[0][0].get("G_Avg")  # gets G_Avg from health dict
    health_expected_G_Avg = round((6 + 5 + 6) / 3, 0)
    if health_actual == health_expected_G_Avg:
        tests_passed += 1
        total_tests += 1
    else:
        tests_failed += 1
        total_tests += 1

    age_actual = list(ld.add_average(ld.load_data(
        "student-mat.csv", "Age")).values())[0][0].get("G_Avg")  # gets G_Avg from age dict
    age_expected_G_Avg = round((7 + 8 + 10) / 3, 0)
    if age_actual == age_expected_G_Avg:
        tests_passed += 1
        total_tests += 1
    else:
        tests_failed += 1
        total_tests += 1

    failures_actual = list(ld.add_average(ld.load_data(
        "student-mat.csv", "Failures")).values())[0][0].get("G_Avg")  # gets G_Avg from failures dict
    failures_expected_G_Avg = round((5 + 6 + 6) / 3, 0)
    if failures_actual == failures_expected_G_Avg:
        tests_passed += 1
        total_tests += 1
    else:
        tests_failed += 1
        total_tests += 1

    # counts actual number of students
    total_passed1 = 0
    tests_passed1 = 0
    tests_failed1 = 0

    # IN SCHOOL DICT
    actual_count = 0
    school_data = load_data("student-mat.csv", "School")
    for keys in school_data.keys():
        for i in school_data[keys]:
            actual_count += 1

    # counts expected number of students
    expected_count = 0
    in_file = open("student-mat.csv")
    next(in_file)
    for line in in_file:
        expected_count += 1
    in_file.close()
    if expected_count == actual_count:
        tests_passed1 += 1
        total_passed1 += 1
    else:
        tests_failed1 += 1
        total_passed1 += 1

    # IN HEALTH DICT
    actual_count = 0
    health_data = load_data("student-mat.csv", "Health")
    for keys in health_data.keys():
        for i in health_data[keys]:
            actual_count += 1

        # counts expected number of students
    expected_count = 0
    in_file = open("student-mat.csv")
    next(in_file)
    for line in in_file:
        expected_count += 1
    in_file.close()
    if expected_count == actual_count:
        tests_passed1 += 1
        total_passed1 += 1
    else:
        tests_failed1 += 1
        total_passed1 += 1

     # IN AGE DICT
    actual_count = 0
    age_data = load_data("student-mat.csv", "Age")
    for keys in age_data.keys():
        for i in age_data[keys]:
            actual_count += 1

        # counts expected number of students
    expected_count = 0
    in_file = open("student-mat.csv")
    next(in_file)
    for line in in_file:
        expected_count += 1
    in_file.close()
    if expected_count == actual_count:
        tests_passed1 += 1
        total_passed1 += 1
    else:
        tests_failed1 += 1
        total_passed1 += 1

     # IN FAILURES DICT
    actual_count = 0
    failures_data = load_data("student-mat.csv", "Failures")
    for keys in failures_data.keys():
        for i in failures_data[keys]:
            actual_count += 1

        # counts expected number of students
    expected_count = 0
    in_file = open("student-mat.csv")
    next(in_file)
    for line in in_file:
        expected_count += 1
    in_file.close()
    if expected_count == actual_count:
        tests_passed1 += 1
        total_passed1 += 1
    else:
        tests_failed1 += 1
        total_passed1 += 1

        return tests_passed1, tests_failed1, total_passed1, total_passed

    print("\n")
    print("Total number of tests for TEST 4 = ", total_tests + total_passed1)
    print("Number of Tests Passed = {}. \nNumber of Tests Failed = {}.".format(tests_passed1
          + tests_passed, tests_failed1 + tests_failed))  # PRINTS OUT TOTAL NUMBER OF TESTS PASSED AND FAILED


check_equal_add_average(student_school_dictionary, student_health_dictionary,
                        student_age_dictionary, student_failures_dictionary, add_average)

