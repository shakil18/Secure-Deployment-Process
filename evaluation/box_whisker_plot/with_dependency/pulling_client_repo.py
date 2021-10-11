import matplotlib.pyplot as plt

plt.figure(figsize=(6, 8), dpi=300)

plt.style.use('default')

# data set
python_without_dependency = [57.238271,
                             56.014924,
                             40.730711,
                             39.773119,
                             39.547287,
                             39.714844,
                             39.805291,
                             39.819293,
                             39.501072,
                             39.808704
                             ]
python_with_dependency = [97.450252,
                          95.614167,
                          166.132218,
                          97.954207,
                          102.860642,
                          114.552138,
                          99.414666,
                          100.758666,
                          97.150315,
                          98.493776
                          ]

patterns = ['/', '']
color = ['#ffffff', '#bababa']

bp = plt.boxplot([python_without_dependency, python_with_dependency],
                 labels=['Python w/o dependency ', 'Python w/ dependency'], patch_artist=True,
                 medianprops={'linewidth': 2})

plt.title('Pulling client repository')
plt.ylabel('Time (seconds)')

for box in bp['boxes']:
    # change outline color
    # box.set(color='#4286f4', linewidth=2)
    # change fill color
    box.set(facecolor=color.pop(0))
    # change hatch
    # box.set(hatch = patterns.pop(0))

plt.savefig('figures/Pulling client repository.png', dpi=300)

plt.show()