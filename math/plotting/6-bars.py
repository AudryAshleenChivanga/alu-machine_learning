#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
fruit = np.random.randint(0, 20, (4, 3))

# Data
people = ['Farrah', 'Fred', 'Felicia']
apples = fruit[0]
bananas = fruit[1]
oranges = fruit[2]
peaches = fruit[3]

# Plotting the stacked bar graph
bar_width = 0.5

plt.bar(people, apples, width=bar_width, color='red', label='Apples')
plt.bar(people, bananas, width=bar_width, bottom=apples, color='yellow', label='Bananas')
plt.bar(people, oranges, width=bar_width, bottom=apples + bananas, color='#ff8000', label='Oranges')
plt.bar(people, peaches, width=bar_width, bottom=apples + bananas + oranges, color='#ffe5b4', label='Peaches')

# Labeling and title
plt.ylabel('Quantity of Fruit')
plt.ylim(0, 80)
plt.yticks(np.arange(0, 81, 10))
plt.title('Number of Fruit per Person')

# Adding legend
plt.legend()

# Show the plot
plt.show()
