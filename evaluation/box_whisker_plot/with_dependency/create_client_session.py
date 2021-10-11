import matplotlib.pyplot as plt

plt.figure(figsize=(6, 8), dpi=300)

plt.style.use('default')

# data set
python_without_dependency = [2.599473,
                             2.622404,
                             2.04666,
                             2.109802,
                             1.685386,
                             2.024917,
                             2.159331,
                             1.792773,
                             1.969871,
                             2.328742
                             ]
python_with_dependency = [2.043263,
                          2.039147,
                          1.818833,
                          1.959377,
                          2.932182,
                          1.924322,
                          2.394007,
                          1.943616,
                          1.768133,
                          1.906955
                          ]

patterns = ['/', '']
color = ['#ffffff', '#bababa']

bp = plt.boxplot([python_without_dependency, python_with_dependency],
                 labels=['Python w/o dependency ', 'Python w/ dependency'], patch_artist=True,
                 medianprops={'linewidth': 2})

plt.title('Creating \'client-session.yaml\'')
plt.ylabel('Time (seconds)')

for box in bp['boxes']:
    # change outline color
    # box.set(color='#4286f4', linewidth=2)
    # change fill color
    box.set(facecolor=color.pop(0))
    # change hatch
    # box.set(hatch = patterns.pop(0))

plt.savefig('figures/Creating client-session.yaml.png', dpi=300)

plt.show()