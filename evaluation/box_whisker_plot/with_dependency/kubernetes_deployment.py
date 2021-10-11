import matplotlib.pyplot as plt

plt.figure(figsize=(6, 8), dpi=300)

plt.style.use('default')

# data set
python_without_dependency = [18.828,
                             18.595,
                             18.631,
                             18.551,
                             18.596,
                             18.664,
                             18.758,
                             18.562,
                             18.512,
                             18.726
                             ]
python_with_dependency = [18.662,
                          18.591,
                          18.753,
                          18.9,
                          18.628,
                          18.531,
                          18.655,
                          18.592,
                          18.677,
                          18.683]

patterns = ['/', '']
color = ['#ffffff', '#bababa']

bp = plt.boxplot([python_without_dependency, python_with_dependency],
                 labels=['Python w/o dependency ', 'Python w/ dependency'], patch_artist=True,
                 medianprops={'linewidth': 2})

plt.title('Kubernetes deployment')
plt.ylabel('Time (seconds)')

for box in bp['boxes']:
    # change outline color
    # box.set(color='#4286f4', linewidth=2)
    # change fill color
    box.set(facecolor=color.pop(0))
    # change hatch
    # box.set(hatch = patterns.pop(0))

plt.savefig('figures/Kubernetes deployment.png', dpi=300)

plt.show()