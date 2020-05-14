import pygal
from die import Die

# Create a new D6.
die = Die()
die_1 = Die()

#Make some rolls, and store results in a list.
results = []
for roll_num in range(1000):
    result = die.roll() + die_1.roll()
    results.append(result)

# Analyze the results.
frequencies = []
max_result = die.num_sides + die_1.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results.
hist = pygal.Bar()

hist.title = "Results of rolling two D6 dice 1000 times."
hist.x_labels = ['1','2','3','4','5','6','7','8','9','10','11','12']
hist.x_title = "Result"
hist.y_title = "Frequency of result"

hist.add('D6 + D6', frequencies)
hist.render_to_file('die_visual.svg')

print(frequencies)