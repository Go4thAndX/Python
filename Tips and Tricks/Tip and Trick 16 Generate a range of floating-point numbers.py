# Tip and Trick 16: Generate a range of floating-point numbers
# 
# The Python range() works only with integers. It doesn’t support the float type, i.e., we cannot use floating-point/decimal value in any of its arguments.

# For example, If you use range() with float step argument, you will get a TypeError 'float' object cannot be interpreted as an integer.

# for i in range(0, 1, 0.1):
#     print(i)
# # Output TypeError: 'float' object cannot be interpreted as an integer

# Goals of this article –

# Use NumPy’s arange() and linspace() functions to use decimal numbers in a start, stop and step argument to produce a range of floating-point numbers.
# Use Python generator to produce a range of float numbers without using any library or module.
# Table of contents
# Range of floats using NumPy’s arange()
# Use float number only in step argument
# Reverse float range
# Range for negative float numbers
# Range of floats using numpy.linspace()
# Range of floats using generator and yield
# Positive float number sequence using a generator
# Negative float numbers sequence using a generator
# Range of floats using a list comprehension
# Range of floats using a itertools
# Next Steps
# Range of floats using NumPy’s arange()
# The NumPy library has various numeric and mathematical functions to operate on multi-dimensional arrays and matrices.


# NumPy has the arange() function to get the range of floating-point numbers. It has the same syntax and functionality as a Python built-in range() function. Also, it allows us to use floating-point numbers in the start, stop and step arguments.

# Syntax of np.arange() function

# np.arange (start, stop, step)
# Time needed: 5 minutes.

# How to generate a range of floats in Python

# Install numpy module
# NumPy doesn’t come with default Python installation. You can install it using pip install numpy.

# Import numpy module
# Import numpy module using the import numpy as np statement.

# Use numpy.arange()
# Pass float numbers to its start, stop, and step argument. For example, np.arange(0.5, 6.5, 1.5) will return the sequence of floating-point numbers starting from 0.5 up to 6.5.Get a range of float numbers

# Example

# import numpy as np

# # range for floats with np.arange()
# for i in np.arange(0, 4.5, 0.5):
#     print(i, end=', ')
# # Output 0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0,

# # Example 2
# for i in np.arange(5.5, 15.5, 2.5):
#     print(i, end=' ')
# # Output 5.5, 8.0, 10.5, 13.0,
#  Run

# Note: As you can see in the output, We got decimal numbers starting from 0.0 to 4.0. If you notice, np.arange() didn’t include 4.5 in its result because it but never includes the stop number in its result. It stops before taking the last step.

# Also, see: Python range() and for loop exercise.

# Use float number only in step argument
# Let see how to use a floating-point step along with a start and stop integers in np.arange() to generate floating-point numbers of a specific interval. In this example, the step value is 2.5.

# import numpy as np

# # float step
# for i in np.arange(1, 10, 2.5):
#     print(i, end=', ')
# # Output 1.0, 3.5, 6.0, 8.5
#  Run

# Reverse float range
# Use the reversed() function to display the sequence of float numbers produced by a np.arange() by descending order.

# import numpy as np

# # reverse range of floats
# for i in reversed(np.arange(5.5, 30.5, 5.5)):
#     print(i, end=', ')
# # Output 27.5, 22.0, 16.5, 11.0, 5.5, 
#  Run
# Range for negative float numbers
# let’s see how to use all negative float numbers in np.arange().

# import numpy as np

# # Negative range of float numbers
# for i in np.arange(-2.5, -20.5, -2.5):
#     print(i, end=', ')
# # Output -2.5, -5.0, -7.5, -10.0, -12.5, -15.0, -17.5, -20.0,
#  Run
# Range of floats using numpy.linspace()
# Let’s see how to use a np.linspace() to get a range of float numbers.


# The numpy.linspace() returns number spaces evenly w.r.t interval. Similar to arange, but instead of step, it uses a sample number.

# We need to define the start point and an endpoint of an interval, and then specify the total number of samples you want within that interval (including the start and the endpoint). The numpy.linspace function will return a sequence of evenly spaced values on that interval

# Syntax

# np.linspace(start, stop, num, endpoint)
# Parameters

# start: The starting position of the range, by default, starts with 0 if not specified.
# stop: The end of the interval range.
# num: The number of samples to generate, default is 50. It cannot be negative, i.e., The Total numbers you want in the output range.
# endpoint: Set it to False if you don’t’ want to include the stop value in the result.
# Example

# import numpy as np

# # Float range using np.linspace()
# # from 2.5 to 12.5
# # num = total float numbers in the output
# for i in np.linspace(2.5, 12.5, num=5):
#     print(i, end=', ')
# # Output 2.5, 5.0, 7.5, 10.0, 12.5,
# print('')

# # endpoint=False to not include stop number in the result
# for i in np.linspace(2.5, 12.5, num=5, endpoint=False):
#     print(i, end=', ')
# # Output 2.5, 4.5, 6.5, 8.5, 10.5,
#  Run

# Note: The numpy.linspace() returns number spaces evenly w.r.t interval. We cannot pass custom step value; instead, we can decide how many samples we want spaces evenly w.r.t interval.

# Range of floats using generator and yield
# What to do if you don’t want to use the numpy library just for arange() and linspace() function?

# In this case, you can use Python generators and yield to write a custom function to generate a range of float numbers.

# You can define a generator to replicate the behavior of Python’s built-in function range() in such a way that it can accept floating-point numbers and produces a range of float numbers.

# The following code divided into 2 Sections.


# The custom frange() function.
# Another section tests custom frange() function using the floating-point number with the following approaches.
# Positive float numbers in frange() arguments.
# With negative float numbers in frange() arguments.
# Both negative and positive float step in frange() arguments.
# Now, let see the example.

# def frange(start, stop=None, step=None):
#     # if set start=0.0 and step = 1.0 if not specified
#     start = float(start)
#     if stop == None:
#         stop = start + 0.0
#         start = 0.0
#     if step == None:
#         step = 1.0

#     print("start = ", start, "stop = ", stop, "step = ", step)

#     count = 0
#     while True:
#         temp = float(start + count * step)
#         if step > 0 and temp >= stop:
#             break
#         elif step < 0 and temp <= stop:
#             break
#         yield temp
#         count += 1


# for i in frange(1.5, 5.5, 0.5):
#     print("%g" % i, end=", ")
# print('\n')

# for i in frange(-0.1, -0.5, -0.1):
#     print("%g" % i, end=", ")
# print('\n')

# for num in frange(0.5, 0.1, -0.1):
#     print("%g" % num, end=", ")
# print('\n')

# for num in frange(0, 7.5):
#     print("%g" % num, end=", ")
# print('\n')

# for num in frange(2.5, 7.5):
#     print("%g" % num, end=", ")
# print('\n')
#  Run

# Output:

# start =  1.5 stop =  5.5 step =  0.5
#  1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 

# start =  -0.1 stop =  -0.5 step =  -0.1
# -0.1, -0.2, -0.3, -0.4, 

# start =  0.5 stop =  0.1 step =  -0.1
# 0.5, 0.4, 0.3, 0.2, 

# start =  0.0 stop =  7.5 step =  1.0
# 0, 1, 2, 3, 4, 5, 6, 7, 

# start =  2.5 stop =  7.5 step =  1.0
# 2.5, 3.5, 4.5, 5.5, 6.5,
# Positive float number sequence using a generator

# If you need a range of only positive float-numbers, you can try this code.

# def frange_positve(start, stop=None, step=None):
#     if stop == None:
#         stop = start + 0.0
#         start = 0.0
#     if step == None:
#         step = 1.0
#     print("start = ", start, "stop = ", stop, "step = ", step)

#     count = 0
#     while True:
#         temp = float(start + count * step)
#         if temp >= stop:
#             break
#         yield temp
#         count += 1


# for i in frange_positve(1.5, 10.5, 0.5):
#     print("%g" % i, end=", ")
# # Output 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10,
#  Run

# Negative float numbers sequence using a generator
# If you need a range of only negative float-numbers, you can try this code.

# def frange_negative(start, stop=None, step=None):
#     if stop == None:
#         stop = start + 0.0
#         start = 0.0
#     if step == None:
#         step = 1.0
#     print("start= ", start, "stop= ", stop, "step= ", step)

#     count = 0
#     while True:
#         temp = float(start + count * step)
#         if temp <= stop:
#             break
#         yield temp
#         count += 1


# for i in frange_negative(-0.1, -0.5, -0.1):
#     print("%g" % i, end=", ")
# # Output -0.1, -0.2, -0.3, -0.4,
#  Run
# Output:

# Using Negative float number in range function
# start=  -0.1 stop=  -0.5 step=  -0.1
# -0.1, -0.2, -0.3, -0.4, 

# Range of floats using a list comprehension
# Let’s see how to use list comprehension to generate a range of float numbers from 0.5 to 9.5.

# Here we are using the range function to generate numbers and dividing each number by 10.0 to get a float number.

# # range from 0.5 to 9.5 with step 0.5
# # using list comprehension
# [print(x / 10.0, end=", ") for x in range(5, 100, 5)]

# # output 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9.0, 9.5,
#  Run
# Range of floats using a itertools
# Let’s see how to generate floating-point range using a itertools.

# import itertools

# def seq(start, end, step):
#     assert (step != 0)
#     sample_count = int(abs(end - start) / step)
#     return itertools.islice(itertools.count(start, step), sample_count)

# for i in seq(0, 1, 0.1):
#     print("%g" % i, end=", ")
# # Output 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9,