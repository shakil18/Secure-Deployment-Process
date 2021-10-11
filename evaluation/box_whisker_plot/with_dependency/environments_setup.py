import matplotlib.pyplot as plt

plt.figure(figsize=(6, 8), dpi=300)

plt.style.use('default')

# data set
python_without_dependency = [3.49, 3.431, 3.497, 3.655, 3.594, 3.499, 3.541, 3.495, 3.478, 3.518]
python_with_dependency = [3.498,
                          3.538,
                          3.528,
                          3.5,
                          3.438,
                          3.429,
                          3.499,
                          3.496,
                          3.464,
                          3.588
                          ]

patterns = ['/', '']
color = ['#ffffff', '#bababa']

bp = plt.boxplot([python_without_dependency, python_with_dependency],
                 labels=['Python w/o dependency ', 'Python w/ dependency'], patch_artist=True,
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