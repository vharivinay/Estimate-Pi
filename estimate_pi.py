'''
Monte Carlo methods, or Monte Carlo experiments, are a broad class of computational algorithms
that rely on repeated random sampling to obtain numerical results. The underlying concept is to
use randomness to solve problems that might be deterministic in principle. They are often used
in physical and mathematical problems and are most useful when it is difficult or impossible to
use other approaches. Monte Carlo methods are mainly used in three problem classes:[1] optimization,
numerical integration, and generating draws from a probability distribution.

Link wiki: https://en.wikipedia.org/wiki/Monte_Carlo_method
Link article: https://medium.com/cantors-paradise/estimating-%CF%80-using-monte-carlo-simulations-3459a84b5ef9

This code is an interactive application that estimates the value of pi
using the unit square unit circle method.

pi = 4 * (number of points in the circle)/(number of points in the square)

Author: Harivinay
Github: github.com/M87K452b
Date: Feb 2021

Note: The animate function is yet to be implemented.
'''

from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

root = Tk()
root.title('Estimate Pi')
root.geometry('900x600')


def make_points():
    num_pts = int(num_points.get())
    data = np.random.random((num_pts, 2))
    return data


def plot_points():
    global data
    data = make_points()
    figure = plt.figure(figsize=(6, 6), dpi=100)
    draw_circle = plt.Circle((0.5135, 0.4945), 0.3855, fill=False)
    figure.add_artist(draw_circle)
    figure.add_subplot(111).scatter(data[:, 0], data[:, 1], s=1)
    chart = FigureCanvasTkAgg(figure, frame_cv)
    chart.get_tk_widget().grid(row=0, column=0)

    plt.grid('off')
    axes = plt.axes()
    axes.set_xlim([0, 1])
    axes.set_ylim([0, 1])


def calc_pi():
    in_circle = 0
    pi = 0
    for i in range(len(data)):
        if np.sqrt(data[i, 0]**2 + data[i, 1]**2) <= 1:
            in_circle = in_circle + 1

    pi = 4 * (in_circle / len(data))

    num_in = 'Points In = ' + str(in_circle)
    num_out = 'Points Out = ' + str(len(data) - in_circle)

    Label(frame_btn, text=num_in, width=25, height=2, font=("Helvetica", 16)).grid(row=5, column=0)
    Label(frame_btn, text=num_out, width=25, height=2, font=("Helvetica", 16)).grid(row=6, column=0)

    pi_text = 'Pi = ' + str(round(pi, 6))
    estimated_pi = Label(frame_btn, text=pi_text, width=25, height=2, font=("Helvetica", 16))
    estimated_pi.grid(row=7, column=0, padx=10, pady=5)


def animate():
    return

frame_cv = LabelFrame(root, padx=1, pady=1)
frame_cv.place(height=598, width=598, x=1, y=1)

figure = plt.figure(figsize=(6, 6), dpi=100)
figure.add_subplot(111)
draw_circle = plt.Circle((0.5135, 0.4945), 0.3855, fill=False)
figure.add_artist(draw_circle)
chart = FigureCanvasTkAgg(figure, frame_cv)
chart.get_tk_widget().grid(row=0, column=0)
plt.grid()
axes = plt.axes()
axes.set_xlim([0, 1])
axes.set_ylim([0, 1])

frame_btn = LabelFrame(root, padx=1, pady=20)
frame_btn.place(height=599, width=298, x=601, y=1)

Label(frame_btn, text='Number of points', font=("Helvetica", 16)).grid(row=0, column=0)

num_points = Scale(frame_btn, from_=0, to=100000, resolution=100, orient=HORIZONTAL, length=185)
num_points.grid(row=1, column=0, padx=10, pady=10)

plot_btn = Button(frame_btn, text='Plot points', width=25, height=5, command=plot_points)
plot_btn.grid(row=2, column=0, padx=10, pady=5)

pi_btn = Button(frame_btn, text='Estimate Pi', width=25, height=5, command=calc_pi)
pi_btn.grid(row=3, column=0, padx=10, pady=5)

animate = Button(frame_btn, text='Animate', width=25, height=5, command=animate, state=DISABLED)
animate.grid(row=4, column=0, padx=5, pady=5)

num_in = 'Points In = 0'
num_out = 'Points Out = 0'
pi = 'Pi = '

Label(frame_btn, text=num_in, width=25, height=2, font=("Helvetica", 16)).grid(row=5, column=0)
Label(frame_btn, text=num_out, width=25, height=2, font=("Helvetica", 16)).grid(row=6, column=0)
Label(frame_btn, text=pi, width=26, height=2, font=("Helvetica", 16)).grid(row=7, column=0)

exit_btn = Button(frame_btn, text='Exit', width=25, height=5, command=root.quit)
exit_btn.grid(row=8, column=0, padx=5, pady=5)

root.mainloop()
