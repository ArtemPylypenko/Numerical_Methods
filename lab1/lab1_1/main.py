import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**3 - x + 0.2

def dechotomia(a, b, f, epsilon = 1e-6):
    left = a
    right = b
    step_counter = 0
    while abs(right - left) > epsilon:
        step_counter += 1

        m = (left + right) / 2
        if f(m) * f(right) > 0:
            right = m
        else:
            left = m

        print(f'step: {step_counter}, left: {left}, right: {right}, delta: {right - left}')

    x_star = (left + right) / 2
    return x_star

def relaxation(a, b, f, epsilon = 1e-6):
    dx = 1e-8
    xs = np.linspace(a, b, 100000)
    ys = f(xs)
    ys_right = f(xs + dx)
    der = (ys_right - ys) / dx

    M1 = np.max(der)
    m1 = np.min(der)

    t = 2/(M1+m1)

    xn = (a+b)/2
    der_x = (f(xn+dx)-f(xn-dx))/(2*dx)

    if(der_x > 0):
        next = xn - t*f(xn)
    else:
        next = xn - t*f(xn)

    while(abs(next - xn) > epsilon):
        xn = next
        der_x = (f(xn+dx)-f(xn-dx))/(2*dx)

        if(der_x>0):
            next = xn - t*f(xn)
        else:
            next = xn + t*f(xn)

    return next

def newton(a,b,f,epsilon = 1e-6):
    dx = 1e-8
    x0=(a+b)/2
    next = x0 - f(x0)/((f(x0+dx)-f(x0))/dx)
    while(abs(next - x0)>epsilon):
        x0=next
        next = x0 - f(x0)/((f(x0+dx)-f(x0))/dx)
    return next



