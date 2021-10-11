import matplotlib.pyplot as plt

plt.figure(figsize=(6, 8), dpi=300)

plt.style.use('default')

# data set
python_without_dependency = [113.893,
                             102.238,
                             101.052,
                             102.847,
                             102.451,
                             101.599,
                             101.38,
                             100.703,
                             103.162,
                             102.853
                             ]
python_with_dependency = [115.341,
                          96.805,
                          97.109,
                          105.75,
                          102.165,
                          102.247,
                          99.99,
                          102.045,
                          95.028,
                          99.655
                          ]

patterns = ['/', '']
color = ['#ffffff', '#bababa']

bp = plt.boxplot([python_without_dependency, python_with_dependency],
                 labels=['Python w/o dependency ', 'Python w/ dependency'], patch_artist=True,
                 medianprops={'linewidth': 2})

plt.title('Minikube loading time')
plt.ylabel('Time (seconds)')

for box in bp['boxes']:
    # change outline color
    # box.set(color='#4286f4', linewidth=2)
    # change fill color
    box.set(facecolor=color.pop(0))
    # change hatch
    # box.set(hatch = patterns.pop(0))

plt.savefig('figures/Minikube loading time.png', dpi=300)

plt.show()