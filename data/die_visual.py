from die import Die
import pygal

"""模拟掷骰子"""
die = Die()
results = []

for roll in range(10000):
    result = die.roll()
    results.append(result)
print(results)

frequencies = []
for val in range(2, die.num_sides + 1):
    frequency = results.count(val)
    frequencies.append(frequency)

print(frequencies)

hist = pygal.Bar()
hist.title = "Results of rolling one D6 10000 times."
hist.x_labels = ["1", "2", "3", "4", "5", "6"]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.add("D6", frequencies)
hist.render_to_file("die_visual.svg")
