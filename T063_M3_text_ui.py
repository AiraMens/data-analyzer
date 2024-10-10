#_author_name_ = AYRA MENSAH
#_student_number_ = 101221911

import T063_M1_load_data as ld
import matplotlib.pyplot as plt
from T063_M2_sort_plot import sort_students_selection 
from T063_M2_sort_plot import histogram 
from T063_M2_sort_plot import student_list
from T063_M3_optimization import minimum 
from T063_M3_optimization import maximum
from scipy.optimize import fminbound
from T063_M2_sort_plot import curve_fit

school = ld.add_average(ld.load_data("student-mat.csv", "School"))
health = ld.add_average(ld.load_data("student-mat.csv", "Health"))
failures = ld.add_average(ld.load_data("student-mat.csv", "Failures"))
age = ld.add_average(ld.load_data("student-mat.csv", "Age"))


loaded_file = [] 
loaded_data = []
attri_s = ['School', 'Age', 'Study Time', 'Failures', 'Health', 'Absences', 'G1', 'G2', 'G3', 'G_Avg']



def user_interface():
    """
    User interface displays the user interface and prompts the user to enter any
    command. If a non-valid command is entered the user is prompted again. 
    
    Preconditions: None
    
    Examples
    >>> l
    Please enter the name of the file:
    >>> a
    Invalid command.
    >>> q
    Program has ended.
    """
    
    #displays user interface
    ui_input = input(
    "The available commands are:\n" + 
    "   1. L" + ")" + "oad Data\n" + 
    "   2. S" + ")" + "ort Data\n" +
    "        'School'    'Age'    'Study Time'    'Failures'     'Health'\n" +
    "        'Absences'    'G1'    'G2'    'G3'    'G_Avg'\n" + 
    "   3. H" + ")" + "istogram\n" +    
    "        'School'    'Age'    'Study Time'    'Failures'     'Health'\n" +    
    "        'Absences'\n" + 
    "   4. W" + ")" + "orst _____ for Grades\n" +
    "        'Age'    'Study Time'    'Failures'    'Health'    'Absences'\n"
    "   5. B" + ")" + "est _____ for Grades\n" +
    "        'Age'    'Study Time'    'Failures'    'Health'    'Absences'\n" + 
    "   6. Q" + ")" + "uit\n" + 
    "\nPlease type your command: "
    )
    if ui_input.lower() == "l":
        return "L"
    elif ui_input.lower() == "s":
        return "S"
    elif ui_input.lower() == "h":
        return "H"
    elif ui_input.lower() == "w":
        return "W"  
    elif ui_input.lower() == "b":
        return "B"
    elif ui_input.lower() == "q":
        return "Q"   
    else:
        print("Invalid command")
        return user_interface()
       
    
def sort_attr():
    """
    Sort attribute function sorts the data of the dictionary by any key that the
    user defines. If a non-valid key is entered the user is prompted again. Then 
    asks the user if they would like to display the file.
    
    Preconditions: None
    
    Examples:
    >>> Age
    Data sorted. Do you want to display the data? Y or N:
    >>> age
    Invalid command
    """
    
    #prompts user for the key they want to sort by
    possible_sortattr = ['Age', 'StudyTime', 'Failures', 'Health', 'Absences', 
                         'G1', 'G2', 'G3', 'G_Avg']
    sortattr = input(
    "Please enter the attribute you want to use for sorting:\n" +
    "'School'    'Age'    'StudyTime'    'Failures'     'Health'\n" +
    "'Absences'    'G1'    'G2'    'G3'    'G_Avg'\n: ")    
    
    if sortattr == "School":
        sortattr_input = input("Data sorted. Do you want to display the data? Y or N: ")
        if sortattr_input.lower() == "y":
            print(sort_students_selection(age, sortattr))
    elif sortattr == "Age":
        sortattr_input = input("Data sorted. Do you want to display the data? Y or N: ")
        if sortattr_input.lower() == "y":
            print(sort_students_selection(school, sortattr))
    elif sortattr == "StudyTime":
        sortattr_input = input("Data sorted. Do you want to display the data? Y or N: ")
        if sortattr_input.lower() == "y":
            print(sort_students_selection(age, sortattr))
    elif sortattr == "G1":
        sortattr_input = input("Data sorted. Do you want to display the data? Y or N: ")
        if sortattr_input.lower() == "y":
            print(sort_students_selection(school, sortattr))
    elif sortattr == "Health":
        sortattr_input = input("Data sorted. Do you want to display the data? Y or N: ")
        if sortattr_input.lower() == "y":
            print(sort_students_selection(health, sortattr)) 
    elif sortattr == "Failures":
        sortattr_input = input("Data sorted. Do you want to display the data? Y or N: ")
        if sortattr_input.lower() == "y":
            print(sort_students_selection(failures, sortattr))
    elif sortattr == "G2":
        sortattr_input = input("Data sorted. Do you want to display the data? Y or N: ")
        if sortattr_input.lower() == "y":
            print(sort_students_selection(school, sortattr))
    elif sortattr == "G3":
        sortattr_input = input("Data sorted. Do you want to display the data? Y or N: ")
        if sortattr_input.lower() == "y":
            print(sort_students_selection(school, sortattr))
    elif sortattr == "G_Avg":
        sortattr_input = input("Data sorted. Do you want to display the data? Y or N: ")
        if sortattr_input.lower() == "y":
            print(sort_students_selection(school, sortattr))
    elif sortattr == "Absences":
        sortattr_input = input("Data sorted. Do you want to display the data? Y or N: ")
        if sortattr_input.lower() == "y":
            print(sort_students_selection(age, sortattr))    
    else:
        print("That is not a recognizable command")
        sort_attr()
 
       
def hist_attr():
    """
    Prompts the user to choose an attribute that they wish to be displayed as a 
    histogram. If a non-valid key is entered the user is prompted again. If the 
    data is not loaded yet it will tell the user No such command exists and 
    return to the user interface.   
    
    Preconditions: Data must be loaded.
    
    Examples:
    >>> Schol
    Invalid command.
    >>> Study Time
    displays histogram on Study Time
    """
    
    #prompts user to select which attribute 
    #they want to be displayed as a histogram
    histattr = input(
    "Please enter the attribute you want to use to represent as a histogram:\n" +
    "'School'    'Age'    'Study Time'    'Failures'     'Health'\n" +
    "'Absences'    'G1'    'G2'    'G3'    'G_Avg'\n: ") 
    
    #if a file is not loaded user interface is called
    if "student-mat.csv" not in loaded_file:
        while histattr not in attri_s:
            print("No such command")
            histattr = input(
                "Please enter the attribute you want to use to represent as a histogram:\n" +
                "'School'    'Age'    'Study Time'    'Failures'     'Health'\n" +
                "'Absences'    'G1'    'G2'    'G3'    'G_Avg'\n: ") 
            if histattr in attri_s:        
                print("File not loaded. Please, load a file first.")
                user_interface()            
    else:   
        while histattr not in attri_s:
            print("Invalid command.")
            histattr = input(
                "Please enter the attribute you want to use to represent as a histogram:\n" +
                "'School'    'Age'    'Study Time'    'Failures'     'Health'\n" +
                "'Absences'    'G1'    'G2'    'G3'    'G_Avg'\n: ") 
            if histattr in attri_s:
                if histattr == "Age":
                    print(histogram(age, histattr))
                elif histattr == "School":
                    print(histogram(school, histattr))
                elif histattr == "Health":
                    print(histogram(health, histattr))  
                elif histattr == "Failures":
                    print(histogram(failures, histattr)) 
                elif histattr == "Absences":
                    print(histogram(age, histattr))   
                elif histattr == "G1":
                    print(histogram(age, histattr))   
                elif histattr == "G2":
                    print(histogram(age, histattr))  
                elif histattr == "G3":
                    print(histogram(age, histattr)) 
                elif histattr == "G_Avg":
                    print(histogram(age, histattr))            
                else:
                    print("Invalid command")
      
            
def worst_attr():
    """
    Prompts user to enter an attribute they wish to see the worst value for 
    based on the curve fit graph.  If a non-valid key is entered the user is prompted again. If the 
    data is not loaded yet it will tell the user No such command exists and 
    return to the user interface.   
    
    Preconditions: Data must be loaded.
    
    Examples:
    >>> Health 
    The worst value for attribute Health is 1
    >>> failures
    Invalid command.
    """
    
    #prompts user to select which attribute 
    #they want the worst value to be displayed   
    worstattr = input(
    "Please enter the attribute you want to see the worst:\n" +
    "'Age'    'Study Time'    'Failures'     'Health'    'Absences'\n: ")  
    if "student-mat.csv" not in loaded_file:
        while worstattr not in attri_s:
            print("No such command")
            worstattr = input(
                "Please enter the attribute you want to see the worst:\n" +
                "'Age'    'Study Time'    'Failures'     'Health'    'Absences'\n: ")
            if worstattr in attri_s:
                print("File not loaded. Please, load a file first.")       
    else:
        if worstattr not in attri_s:
            while worstattr not in attri_s:
                print("Invalid command")
                worstattr = input(
                    "Please enter the attribute you want to see the worst:\n" +
                    "'Age'    'Study Time'    'Failures'     'Health'    'Absences'\n: ")  
                if worstattr in attri_s:
                    worst = minimum(ld.add_average(ld.load_data("student-mat.csv", loaded_data)), worstattr)
                    print("The worst value for the attribute " + str(worstattr) + " is " + str(int(worst[0])))
        else:
            worst = minimum(ld.add_average(ld.load_data("student-mat.csv", loaded_data)), worstattr)
            print("The worst value for the attribute " + str(worstattr) + " is " + str(int(worst[0])))            
    
def best_attr():
    """
    Prompts user to enter an attribute they wish to see the worst value for 
    based on the curve fit graph.  If a non-valid key is entered the user is prompted again. If the 
    data is not loaded yet it will tell the user No such command exists and 
    return to the user interface.   
    
    Preconditions: Data must be loaded.
    
    Examples:
    >>> Health 
    The best value for attribute Health is 5
    >>> absences
    Invalid command.
    """
    #prompts user to select which attribute 
    #they want the worst value to be displayed      
    bestattr = input(
    "Please enter the attribute you want to see the worst:\n" +
    "'Age'    'Study Time'    'Failures'     'Health'    'Absences'\n: ") 
    if "student-mat.csv" not in loaded_file:
        while bestattr not in attri_s:
            print("No such command")
            bestattr = input(
                "Please enter the attribute you want to see the worst:\n" +
                "'Age'    'Study Time'    'Failures'     'Health'    'Absences'\n: ")
            if bestattr in attri_s:
                print("File not loaded. Please, load a file first.")    
    else:
        if bestattr not in attri_s:
            while bestattr not in attri_s:
                print("Invalid command")
                bestattr = input(
                    "Please enter the attribute you want to see the worst:\n" +
                    "'Age'    'Study Time'    'Failures'     'Health'    'Absences'\n: ")  
                if bestattr in attri_s:
                    best = maximum(ld.add_average(ld.load_data("student-mat.csv", loaded_data)), bestattr)
                    print("The best value for the attribute " + str(bestattr) + " is " + str(int(best[0])))
        else:
            best = maximum(ld.add_average(ld.load_data("student-mat.csv", loaded_data)), bestattr)
            print("The best value for the attribute " + str(bestattr) + " is " + str(int(best[0])))            
                      
def file_name():
    """
    Prompts the user for the file name they would like to select. If 
    'student-mat.csv' is not inputed the user is prompted again. 
    
    Preconditions: None
    
    Examples:
    >>> students.mat.csv
    Invalid command.
    
    """
    
    #prompts user for filename until correct name is inputed
    
    filename = input("Please enter the name of the file: ")
    while filename != "student-mat.csv":
        print("Invalid command.")
        filename = input("Please enter the name of the file: ")
        if filename == "student-mat.csv":
            continue
    loaded_file.append(filename)
    return filename


def key_attr():
    possible_keyattr = ["School", "Age", "Failures", "Health"]
    keyattr = input("Please enter the attribute to use as a key: ")
        
    while keyattr not in possible_keyattr: 
        print("That is not a recognized key")
        keyattr = input("Please enter the attribute to use as a key: ")
        if keyattr in possible_keyattr:          
            continue 
    
    return keyattr
   
    


def user_options(user_selection: str) -> str:
    if user_selection == "L":
        loaded_data = ld.add_average(ld.load_data(file_name(), key_attr()))
        print("Data loaded") 
        user_options(user_interface())
        return loaded_data
    elif user_selection == "S":
        sort_attr()
        user_options(user_interface())
    elif user_selection == "H":
        hist_attr()
        user_options(user_interface())
    elif user_selection == "W":
        worst_attr()
        user_options(user_interface())
    elif user_selection == "B":
        best_attr()
        user_options(user_interface())
    elif user_selection == "Q":
        print("Program has ended.")
    



if __name__ =="__main__":
    user_options(user_interface())
    
