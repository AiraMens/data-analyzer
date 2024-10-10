# FUNCTION 1

# Name- Maulik Khanna
# Student Number- 101273389

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import fminbound
from T063_M1_load_data import *
from T063_M2_sort_plot import curve_fit


def f_min(x: list, coeffs: list):
    '''This function returns a polyval graph for paramters of coeeficients and minimum and maximum value of x.
    '''
    return np.polyval(coeffs, x)


def minimum(student_dict: dict, student_type: str) -> tuple:
    '''This function returns a tuple based on fminbound function for minimum and maximum value for x as well as using values of coefficients as an argument to call f_min function
    '''
    coeffs, x = curve_fit(student_dict, student_type, 2)
    x_for_y_min = fminbound(f_min, x[0], x[-1], args=(coeffs, ))

    return x_for_y_min, f_min(x_for_y_min, coeffs)


if __name__=="__main__":
    minimum(add_average(student_school_dictionary('student-mat.csv')), 'Health')
    minimum(add_average(student_school_dictionary('student-mat.csv')), 'Failures')
    minimum(add_average(student_school_dictionary('student-mat.csv')), 'StudyTime')
    minimum(add_average(student_age_dictionary('student-mat.csv')), 'Age')
    minimum(add_average(student_age_dictionary('student-mat.csv')), 'Health')
    minimum(add_average(student_age_dictionary('student-mat.csv')), 'Failures')
    minimum(add_average(student_age_dictionary('student-mat.csv')), 'StudyTime')
    minimum(add_average(student_health_dictionary('student-mat.csv')), 'Age')
    minimum(add_average(student_health_dictionary('student-mat.csv')), 'Health')
    minimum(add_average(student_health_dictionary('student-mat.csv')), 'Failures')
    minimum(add_average(student_health_dictionary('student-mat.csv')), 'StudyTime')
    minimum(add_average(student_failures_dictionary('student-mat.csv')), 'Age')
    minimum(add_average(student_failures_dictionary('student-mat.csv')), 'Health')
    minimum(add_average(student_failures_dictionary('student-mat.csv')), 'Failures')
    minimum(add_average(student_failures_dictionary('student-mat.csv')), 'StudyTime')



# FUNCTION 2
# Tarik Kartal
# 101275241
import numpy as np
import scipy.optimize as sp
import T063_M2_sort_plot as M2
import T063_M1_load_data as M1


def maximum(a: dict[list[dict]], atr: str) -> list:
    """This functions takes dict and attribute and returns a tuple of xmax and ymax in second order.
    Preconditions: The coef must be >0
    >>>(maximum(M1.add_average(M1.load_data('student-mat.csv', 'Age')), 'G_Avg'))
    (20, 19.99999)
    (graph displaying the max point)

    """
    # find polynomial using curve fit at 2nd order, name assigned to pol.
    pol = list(M2.curve_fit(a, atr, 2))
    # define a f(x) function inside to use to find the f(x) value
    # negate the return value since we are looking for the max
    def f(x): return -np.polyval(pol, x)
    # declare ranges for each attribute
    range_atr = {'Health': (1, 5), 'StudyTime': (1, 4), 'G_Avg': (0, 20), 'Absences': (
        0, 75), 'Failures': (0, 10), 'Age': (15, 22), 'G1': (0, 20), 'G2': (0, 20), 'G3': (0, 20)}

    # calculate the min using fminbound (passing f, and the range of your atr)
    x = sp.fminbound(f, range_atr[atr][0], range_atr[atr][1])
    # finishing touches (rounding, finding y val)
    y = round(f(x), 5)
    x = round(x)
    # return (negate y since the current y is the min of the negated pol; it will become max)
    return (x, 0 - y)


if __name__ == "__main__":
    maximum(M1.add_average(M1.load_data('student-mat.csv', 'Age')), 'G_Avg')
