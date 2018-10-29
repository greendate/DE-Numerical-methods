import math
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt2
from tkinter import *


x0 = 0
y0 = 1
b = 9
n = 48
l = 0  # left border
r = 48  # right border


def cnt():
    global x0, y0, b, n, l, r
    x0 = int(var_x0.get())
    y0 = int(var_y0.get())
    b = int(var_b.get())
    n = int(var_n.get())
    l = int(var_l.get())
    r = int(var_r.get())
    root.destroy()
    return


def f(x, y):
    return 2 * (math.sqrt(y) + y)


def y(x):
    return (pow(math.e, x) * 2 - 1) * (pow(math.e, x) * 2 - 1)


def exact_solution(x0, y0, b, n):
    h = (b - x0) / n
    x = []
    for i in range(n):
        x.append(x0 + i * h)
    e = []
    for i in range(n):
        e.append(y(x[i]))
    return e


def euler_method(x0, y0, b, n):
    h = (b - x0) / n
    x = []
    for i in range(n):
        x.append(x0 + i * h)
    y = [y0]
    for i in range(1, n):
        y.append(y[i - 1] + h * f(x[i - 1], y[i - 1]))
    return y


def improved_euler_method(x0, y0, b, n):
    h = (b - x0) / n
    x = []
    for i in range(n):
        x.append(x0 + i * h)
    y = [y0]
    for i in range(1, n):
        k1 = f(x[i - 1], y[i - 1])
        k2 = f(x[i - 1] + h, y[i - 1] + h * k1)
        y.append(y[i - 1] + (h / 2) * (k1 + k2))
    return y


def runge_kutta_method(x0, y0, b, n):
    h = (b - x0) / n
    x = []
    for i in range(n):
        x.append(x0 + i * h)
    y = [y0]
    for i in range(1, n):
        k1 = f(x[i - 1], y[i - 1])
        k2 = f(x[i - 1] + h / 2, y[i - 1] + (h / 2) * k1)
        k3 = f(x[i - 1] + h / 2, y[i - 1] + (h / 2) * k2)
        k4 = f(x[i - 1] + h, y[i - 1] + h * k3)
        y.append(y[i - 1] + (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4))
    return y


def compute_error(method1, method2):
    answer = (r - l) * [0]
    for i in range(l, r):
        answer[i - l] = method1[i] - method2[i]
    return answer


def investigate_convergence(error):
    for element in error:
        if round(element) != 0:
            print(" is not convergent.")
            return
    print(" is convergent.")


def plotMethods(exact, euler, improved, runge_kutta):
    line1, = plt.plot(exact)
    line2, = plt.plot(euler)
    line3, = plt.plot(improved)
    line4, = plt.plot(runge_kutta)
    plt.legend([line1, line2, line3, line4],
               ['Exact solution', 'Euler method', 'Improved Euler method', 'Runge-Kutta method'])
    plt.show()


def plotErrors(error1, error2, error3):
    err_line1, = plt.plot(error1)
    err_line2, = plt.plot(error2)
    err_line3, = plt.plot(error3)
    plt2.legend([err_line1, err_line2, err_line3],
                ['Euler method error', 'Improved Euler method error', 'Runge-Kutta method error'])
    plt2.show()


#--------------- graphic user interface ------------#
root = Tk()
root.geometry('450x450+500+300')
root.title('DE Computational practicum')

l1 = Label(root, text="x0: ")
l1.grid(row=0, column=0)
var_x0 = Entry(root)
var_x0.grid(row=0, column=1)

l2 = Label(root, text="y0: ")
l2.grid(row=1, column=0)
var_y0 = Entry(root)
var_y0.grid(row=1, column=1)

l3 = Label(root, text="X: ")
l3.grid(row=2, column=0)
var_b = Entry(root)
var_b.grid(row=2, column=1)

l4 = Label(root, text="N:")
l4.grid(row=3, column=0)
var_n = Entry(root)
var_n.grid(row=3, column=1)

l5 = Label(root, text="Point where you want to start range: ")
l5.grid(row=4, column=0)
var_l = Entry(root)
var_l.grid(row=4, column=1)

l5 = Label(root, text="Point where you want to finish range: ")
l5.grid(row=5, column=0)
var_r = Entry(root)
var_r.grid(row=5, column=1)

button = Button(root, text="Continue", command=cnt)
button.grid(row=6, column=0)
root.mainloop()
#---------------------------------------------------#

exact = exact_solution(x0, y0, b, n)
euler = euler_method(x0, y0, b, n)
improved = improved_euler_method(x0, y0, b, n)
runge_kutta = runge_kutta_method(x0, y0, b, n)

plotMethods(exact, euler, improved, runge_kutta)

error1 = compute_error(exact, euler)
error2 = compute_error(exact, improved)
error3 = compute_error(exact, runge_kutta)

plotErrors(error1, error2, error3)

print("Euler method", end="")
investigate_convergence(error1)
print("Improved Euler method", end="")
investigate_convergence(error2)
print("Runge-Kutta method", end="")
investigate_convergence(error3)
