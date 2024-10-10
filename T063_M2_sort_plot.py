# Tarik Kartal
# Maulik Khanna
# Ayra Mensah
# Tania Pillay


import numpy as np
import matplotlib.pyplot as plt
from T063_M1_load_data import *

# ===============================================================================================================================================
# ------------------------------------------------FUNCTION 1-------------------------------------------------------------------------------------


def student_list(a: dict[list[dict]]) -> list[dict]:
    """
    Converts a dictionary into a list
    Dictionary must have the format {str:list[dict{str:}]}

    Preconditions: a should be add_average(student_x_dictionary('student-mat.csv')), where x = school, health, age, or failures
    >>>student_list(add_average(student_school_dictionary('student-mat.csv')))
    [{'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6, 'G_Avg': 5.67, 'School': 'GP'}, {...}]
    """
    b = []  # make an empty list

    for key in a:  # go to all the keys in original dictionary
        for student in a[key]:  # go to each student in the list at the key in the dictionary

            # make a list of all keys in a student
            # this way we can check which key is missing

            keylist = list(student.keys())
            # check for the missing key
            new_key = ''

            if 'School' not in keylist:
                new_key = 'School'
            elif 'Health' not in keylist:
                new_key = 'Health'
            elif 'Age' not in keylist:
                new_key = 'Age'
            elif 'Failures' not in keylist:
                new_key = 'Failures'

                # using our new key and the key from original dictionary
                # the original key is the value we use here

            student[new_key] = key
            # add the updated student to our list
            b.append(student)

    return b


# =================================================================================================================================================
# --------------------------------------------FUNCTION 2-------------------------------------------------------------------------------------------


def sort_students_bubble(student_dict: dict, student_type: str) -> list:
    '''The function returns a sorted list of small dictionary in ascending and alphabetical order based on the two paramters: add_average dictionary from load_data file and string variable student_type.

    Parameter: The final result should give a list of small dictionary.

    >>> sort_students_bubble(add_average(student_school_dictionary('student-mat.csv')),'Age')
    [{'Age': 15, 'StudyTime': 2.0, 'Failures': 3, 'Health': 3, 'Absences': 10, 'G1': 7, 'G2': 8, 'G3': 10, 'G_Avg': 8, 'School': 'GP'},
    ...
    {'Age': 22, 'StudyTime': 1.0, 'Failures': 3, 'Health': 1, 'Absences': 16, 'G1': 6, 'G2': 8, 'G3': 8, 'G_Avg': 7, 'School': 'BD'}]

    '''
    final_list = student_list(student_dict)

    swap = True
    while swap:
        swap = False
        for i in range(len(final_list) - 1):
            if final_list[i][student_type] > final_list[i + 1][student_type]:
                aux = final_list[i]
                final_list[i] = final_list[i + 1]
                final_list[i + 1] = aux
                swap = True
    return final_list


# ==============================================================================================================================================
# ------------------------------------------FUNCTION 3------------------------------------------------------------------------------------------


def sort_students_selection(dc: dict[list[dict]], wanted: str) -> list[dict]:
    """This function takes a dict and wanted kind of string as a sortion for input, 
    and converts the dict to list which is sorted by selection. 
    Preconditions: parameter dc must be a dict, and wanted must be string 
    in the list. Parameter wanted is case sensetive. 

    >>>sort_students_selection(add_average(student_age_dictionary('student-mat.csv')), 'G1')
    [{'School': 'BD', 'StudyTime': 2.0, 'Failures': 1, 'Health': 5, 'Absences': 8, 'G1': 3, 'G2': 5, 'G3': 5, 'G_Avg': 4, 'Age': 18},
    ....
    {'School': 'GP', 'StudyTime': 2.0, 'Failures': 0, 'Health': 5, 'Absences': 2, 'G1': 19, 'G2': 18, 'G3': 18, 'G_Avg': 18, 'Age': 15}]

    """
    dc = student_list(dc)  # assigns the original list to parameter dc
    for i in range(len(dc)):  # loops every item on the length list
        min_i = i  # assigns the first index in the i to min_i
        # selection sort process. goes through every index in lenght of the list except i
        for j in range(i + 1, len(dc)):
            if dc[min_i][wanted] > dc[j][wanted]:  # checks if any value is smaller than i
                min_i = j  # if so, j will become min_i
        dc[i], dc[min_i] = dc[min_i], dc[i]  # changes the order in the list
    return dc


# dc = sort_students_selection(add_average(student_school_dictionary('student-mat.csv')), 'Failures)
# for i in dc:
# this process is not mandatory, it makes the list easier to read by showing all dictionaries in new lines.
# print(i)


# ===============================================================================================================================================
# -----------------------------------------------------------FUNCTION 4--------------------------------------------------------------------------


def curve_fit(my_dict: dict, attribute: str, deg: int) -> list:
    """This function creates a scatter graph showing the correlation between an attribute's attr and the overall grade for each level of the attribute.
It returns a list of polynomial coefficients is returned and displays a polynomial degree (deg) line of best fit, with values between 1 and 5.
Also, interpolation is used instead of regression if the polynomial degree supplied is higher than that of the interpolating polynomial, or in other words, if deg is higher than the number of x-values.


    Preconditions: The chosen attribute must have a numerical value ie, float or int.

    >>>curve_fit(add_average(load_data("student-mat.csv", "Age")), "G3", 3)
    [-2.21905426e-03,  8.37561644e-02, -3.19530258e-02,  3.93506769e+00]
    """

    my_list = student_list(my_dict)  # convert my_dict to my_list
    G_Avg = {}  # creates an empty dictionary in which to store attribute inputs as keys and G_Avg as values

    for i in my_list:               # create a new key for every unique value of attribute and assign an empty list as its value
        G_Avg[i[attribute]] = []

    for i in my_list:
        # get the value of 'G_Avg' for each student and add it to whichever list corresponds to that student's attribute value
        G_Avg[i[attribute]] += [i['G_Avg']]
    for key in G_Avg:    # Replace the value to each key with the average of all 'G_Avg' in that list value, only for the lists that are not empty

        if len(G_Avg[key]) != 0:
            G_Avg[key] = round(
                sum(G_Avg[key]) / len(G_Avg[key]), 2)
        else:

            # Delete the key:value pairs that have empty lists
            del G_Avg[i[attribute]]

    # Creating the plots
    fig = plt.figure()
    plt.title(" AVERAGE GRADES")
    plt.xlabel("For: " + attribute)
    plt.ylabel("Avg_grade")
    x, y = list(G_Avg.keys()), list(G_Avg.values())

    swapped = True   # bubble sort by x ascending, and take a 'y' with its 'x' wherever
    while swapped:
        swapped = False
        for i in range(len(x) - 1):
            if x[i] > x[i + 1]:
                a = x[i], y[i]
                x[i], y[i] = x[i + 1], y[i + 1]
                x[i + 1], y[i + 1] = a
                swapped = True

    order = len(x) - 1
    if deg < order:  # if polynomial degree is less than number of data points, do regression
        z = np.polyfit(x, y, deg)

    else:  # else interpolation
        z = np.polyfit(x, y, order)

    # Error and linespace configuration
    x_e = np.linspace(min(x), max(x), 100)
    y_e = np.polyval(z, x_e)
    x, y = np.linspace(min(x), max(x), len(x)), y

    # displaying the plotted grah
    plt.plot(x, y, 'o', x_e, y_e, '-')
    plt.show()
    x.sort()

    x_min, x_max = x[0], x[-1]
    return z, [x_min, x_max]  # return the list of polynomial coefficients


#coeffs, x = z, [x_min, x_max]
#coeffs = z
#x = [x_min, x_max]

# ======================================================================================================================================
# ----------------------------------FUNCTION 5------------------------------------------------------------------------------------------


def histogram(a: dict, b: str):
    """ This fuction will import data from the dictionary and will be
    using the data obtained as values for the x- axis and y- axis.

    """
    students = student_list(a)
    histogram = {}

    for i in students:
        if i[b] not in histogram.keys():
            histogram[i[b]] = 1
        else:
            histogram[i[b]] += 1

    x = histogram.keys()
    y = histogram.values()

    plt.figure()
    plt.bar(x, y)
    plt.title("Histogram: Student Value for  " + b)
    plt.xlabel("Students'  " + b)
    plt.ylabel("Number of students")
    plt.show()


# MAIN SCRIPT WITH FUNCTION CALLS
if __name__ == "__main__":
    list1 = student_list(add_average(
        student_school_dictionary('student-mat.csv')))
    for i in list1:
        print(i)
    list1 = sort_students_bubble(add_average(
        student_failures_dictionary('student-mat.csv')), 'Health')
    for i in list1:
        print(i)
    list1 = sort_students_selection(add_average(
        student_age_dictionary('student-mat.csv')), 'G1')
    for i in list1:
        print(i)

    print(curve_fit(add_average(load_data("student-mat.csv", "Age")), "G3", 3))
    print(histogram(add_average(student_school_dictionary('student-mat.csv')), 'Health'))
