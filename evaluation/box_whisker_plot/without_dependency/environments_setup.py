import matplotlib.pyplot as plt

plt.figure(figsize=(6, 8), dpi=300)

plt.style.use('default')

# data set
python = [3.49, 3.431, 3.497, 3.655, 3.594, 3.499, 3.541, 3.495, 3.478, 3.518]
nodejs = [3.62, 3.614, 3.556, 3.615, 3.633, 3.628, 3.606, 3.665, 3.626, 3.621]
lua = [3.54, 3.557, 3.568, 3.469, 3.504, 3.545, 3.48, 3.62, 3.577, 3.434]
rscript = [3.74, 3.728, 3.722, 3.745, 3.604, 3.762, 3.671, 3.734, 3.739, 3.744]

patterns = ['/', 'O', '*', '']
color = ['#ffffff', '#bababa', '#000000', '#c1deff']

bp = plt.boxplot([python, nodejs, lua, rscript], labels=['Python', 'NodeJS', 'Lua', 'Rscript'], patch_artist=True,
                 medianprops={'linewidth': 2})

plt.title('Environments setup')
plt.ylabel('Time (seconds)')

for box in bp['boxes']:
    # change outline color
    # box.set(color='#4286f4', linewidth=2)
    # change fill color
    box.set(facecolor=color.pop(0))
    # change hatch
    # box.set(hatch = patterns.pop(0))

plt.savefig('figures/Environments setup.png', dpi=300)

plt.show()