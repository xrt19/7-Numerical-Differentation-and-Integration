# -*- coding: utf-8 -*-
"""tmp11.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aM2_8RPDPlkkmEUMZmdc9pBENfozNQtV
"""

import numpy as np

print("Trapezoid Rule\n")

def f(x):
  return (np.sin(x) ** 2) + np.sin(x) + 2

# source: https://datagy.io/python-pi/
pi_value = np.pi

start = -1 * pi_value
end = 2 * pi_value
points = 27

# Define width
width = (end - start) / (points - 1)

# Divide into several parts
x = np.linspace(start, end, points)
y = f(x)

# Trapezoid Rule
tinggi_trapezoid = width
area_trapezoid = (y[0] + 2 * np.sum(y[1:points - 1]) + y[points-1]) * tinggi_trapezoid * 1/2
print(f"Trapezoid Area: {area_trapezoid}")