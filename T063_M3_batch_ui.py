#_author_name_ = AYRA MENSAH
#_student_number_ = 101221911




import T063_M1_load_data as ld
from T063_M1_load_data import load_data
from T063_M1_load_data import add_average
from T063_M3_optimization import minimum
from T063_M3_optimization import maximum
from T063_M2_sort_plot import histogram

school = ld.add_average(ld.load_data("student-mat.csv", "School"))
health = ld.add_average(ld.load_data("student-mat.csv", "Health"))
failures = ld.add_average(ld.load_data("student-mat.csv", "Failures"))
age = ld.add_average(ld.load_data("student-mat.csv", "Age"))


def batch_user(filename: str) -> list:

    file = open('batch_file.txt', "r")
    b_list = []
    for line in file:
        lst = line.strip("\n").split(";")
        b_list += [lst]
    print(b_list)
    input("Please enter the name of the file where your commands are stored:")

    for item in b_list:
        if item[0].upper() == "L":
            load_data("student-mat.csv", "Health")
            print("Data loaded")

    for item in b_list:
        if item[0].lower() == 's':
            data_s = sorted(add_average(
                load_data("student-mat.csv", "Health")))
            print("Do you want to display the data?")
            if item[2] in item[1] == 'Y':
                print(data_s)
            else:
                print("<<<you selected not to display>>>")
            print("Data sorted")

    for item in b_list:
        if item[0].lower() == 'b':
            max_value = (
                max(add_average(load_data("student-mat.csv", "School")), "Age"))
            print("The best value for the attribute age is", max_value)
            # print("The best value for the attribute " + attribute +" is " + maximum(ld.add_average(ld.load_data("student-mat.csv", "School")), attribute))

    for item in b_list:
        if item[0].lower() == 'w':
            min_value = (
                minimum(add_average(load_data("student-mat.csv", "School")), "Health"))
            print("The worse value for the attribute Health is", min_value)

    for item in b_list:
        if item[0].lower() == 'h':
            print("<<<Histogram with Study Time will be shown>>>")
            print(histogram(school, 'StudyTime'))


batch_user("batch_file.txt")





