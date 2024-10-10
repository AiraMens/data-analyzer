#ECOR-1042-Fall 2022 README for LAB 6 PROJECT   Python version 3.10.9  11/12/2022
Ayra Mensah


**Description:**

________________

The contents of an excel file are used to create various dictionaries by the help of different function definitions (student_school_dictionary, etc.) Function calls are placed at the end of each script to access the various functionalities. Building up on the created dictionaries, more functions for sorting the data in the dictionaries, plotting a graph and histogram for data in review, and finding minimum and maximum values are created. A text user interface and a batch user interface included in this project allows user to access specific infromation or a group of information.


This project includes the following files:

-T063_M1_load_data.py
-T063_M2_sort_plot.py
-T063_M3_optimization.py
-student-mat.csv
-T063_M3_batch_ui.py
-T063_M3_text_ui.py
-check_equal.py(auxiliary module)






**Installation:**


_________________

Python 3.7.3 or later must be installed and used to run scripts properly.

The external modules to be installed with the files and libraries needed are:
Numpy, Matplolib, Scipy  - Python Library
typing, string, matplotlib.pyplot- Python modules





**Usage:**


__________

The text-based interactive user interface is shown below:

When the T063_M3_text_ui.py file is properly run(make sure all associated files are in the same directory), the following is displayed:

The available commands are:
   1. L)oad Data
   2. S)ort Data
        'School'    'Age'    'Study Time'    'Failures'     'Health'
        'Absences'    'G1'    'G2'    'G3'    'G_Avg'
   3. H)istogram
        'School'    'Age'    'Study Time'    'Failures'     'Health'
        'Absences'
   4. W)orst _____ for Grades
        'Age'    'Study Time'    'Failures'    'Health'    'Absences'
   5. B)est _____ for Grades
        'Age'    'Study Time'    'Failures'    'Health'    'Absences'
   6. Q)uit

Please type your command: (*user types one of the letters to the left of ) in the options listed above, can be upper or lower case*)

Information specific to option chosen is displayed at each step through simple instructions.
User ends the program by typing Q or q as the input command.

When looking for a batch/group of information, user runs the T063_M3_batch_ui.py file and follows a similar format to the T063_text_ui.py file.







**Credits:**


____________
The authors for each function/module :

-student_school_dictionary = Maulik Khanna
-student_health_dictionary = Tarik Kartal
-student_age_dictionary = Tania Pillay
-student_failures_dictionary = Ayra Mensah
-load_data = Maulik Khanna
-add_average = Ayra Mensah & Maulik Khanna


-check_equal_keys = Maulik Khanna
-check_equal_size = Tarik Kartal
-check_equal_entries = Tarik Kartal, Maulik Khanna & Ayra Mensah
-check_equal_add_average = Ayra Mensah


-student_list = Tarik Kartal
-sort_students_bubble = Maulik Khanna
-sorts_students_selection = Tarik Kartal
-curve_fit = Ayra Mensah
-histogram = Tania Pillay


-f_min = Maulik Khanna
-minimum = Maulik Khanna
-maximum = Tarik Kartal


-T063_M3_text_ui.py = Ayra Mensah
-T063_M3_batch_ui.py = Ayra Mensah





**License:**


____________
Academic Free License v3.0  afl-3.0
