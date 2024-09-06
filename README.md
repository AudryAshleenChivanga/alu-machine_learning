README: Plotting Notes by Audry Ashleen Chivanga
These are my personal notes for understanding basic data visualization using Matplotlib for my school project.

Key Points
What is a Plot?
A visual representation of data used to identify patterns, trends, or relationships.

Types of Plots:

Scatter Plot: Dots show relationships between two variables.
Line Graph: Lines connect data points to display changes over time.
Bar Graph: Bars compare different categories or groups.
Histogram: Shows data distribution across intervals.
Using Matplotlib:

Import the Library:
python
Copy code
import matplotlib.pyplot as plt
Plot Examples:
python
Copy code
plt.plot(x, y)  # Line graph
plt.scatter(x, y)  # Scatter plot
plt.bar(x, y)  # Bar graph
plt.hist(data, bins=10)  # Histogram
plt.show()
Customization:

Add titles, axis labels, and legends to clarify plots.
Adjust scales to improve visualization.

