#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

y0 = np.arange(0, 11) ** 3

mean = [69, 0]
cov = [[15, 8], [8, 15]]
np.random.seed(5)
x1, y1 = np.random.multivariate_normal(mean, cov, 2000).T
y1 += 180

x2 = np.arange(0, 28651, 5730)
r2 = np.log(0.5)
t2 = 5730
y2 = np.exp((r2 / t2) * x2)

x3 = np.arange(0, 21000, 1000)
r3 = np.log(0.5)
t31 = 5730
t32 = 1600
y31 = np.exp((r3 / t31) * x3)
y32 = np.exp((r3 / t32) * x3)

np.random.seed(5)
student_grades = np.random.normal(68, 15, 50)

# Create a figure with a 3x2 grid layout
fig = plt.figure(constrained_layout=True)
fig.suptitle('All in One', fontsize='x-small')  # Title of the whole figure

# Define the grid spec
gs = GridSpec(3, 2, figure=fig)

# Plot 1 - Cubic values
ax1 = fig.add_subplot(gs[0, 0])
ax1.plot(y0, 'r-')
ax1.set_xlim(0, 10)
ax1.set_xticks([0, 2, 4, 6, 8, 10])  # Correct method for setting x-ticks
ax1.set_yticks([0, 500, 1000])  # Correct method for setting y-ticks
ax1.set_xlabel('', fontsize='x-small')
ax1.set_ylabel('', fontsize='x-small')

# Plot 2 - Scatter plot of Height vs Weight
ax2 = fig.add_subplot(gs[0, 1])
ax2.scatter(x1, y1, color='magenta')
ax2.set_xticks([60, 70, 80])  # Correct method for setting x-ticks
ax2.set_title("Men's Height vs Weight", fontsize='x-small')
ax2.set_xlabel('Height (in)', fontsize='x-small')
ax2.set_ylabel('Weight (lbs)', fontsize='x-small')

# Plot 3 - Exponential Decay of C-14
ax3 = fig.add_subplot(gs[1, 0])
ax3.plot(x2, y2)
ax3.set_yscale('log')
ax3.set_xlim(0, 20000)  # Set x-axis limit to 20000 to match the desired tick marks
ax3.set_xticks([0, 10000, 20000])  # Correctly set x-axis ticks to 0, 10000, 20000
ax3.set_title('Exponential Decay of C-14', fontsize='x-small')
ax3.set_xlabel('Time (years)', fontsize='x-small')
ax3.set_ylabel('Fraction remaining', fontsize='x-small')

# Plot 4 - Exponential Decay of Radioactive Elements
ax4 = fig.add_subplot(gs[1, 1])
ax4.plot(x3, y31, 'r--', label='C-14')
ax4.plot(x3, y32, 'g-', label='Ra-226')
ax4.set_xlim(0, 20000)
ax4.set_xticks([0, 5000, 10000, 15000, 20000])  # Correctly set x-axis ticks to match the desired intervals
ax4.set_ylim(0, 1)
ax4.set_yticks([0, 0.5, 1.0])
ax4.set_title('Exponential Decay of Radioactive Elements', fontsize='x-small')
ax4.set_xlabel('Time (years)', fontsize='x-small')
ax4.set_ylabel('Fraction Remaining', fontsize='x-small')
ax4.legend(fontsize='x-small', loc='upper right')

# Plot 5 - Histogram of Student Grades (spanning two columns)
ax5 = fig.add_subplot(gs[2, :])
ax5.hist(student_grades, bins=range(0, 101, 10), edgecolor='black')
ax5.set_xlim(0, 100)
ax5.set_ylim(0, 30)
ax5.set_title('Project A', fontsize='x-small')
ax5.set_xlabel('Grades', fontsize='x-small')
ax5.set_ylabel('Number of Students', fontsize='x-small')
ax5.set_xticks(np.arange(0, 101, 10))  # Set x-axis ticks for grades every 10 units

# Show the plot
plt.show()
