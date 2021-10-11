import matplotlib.pyplot as plt

plt.figure(figsize=(6, 8), dpi=300)

plt.style.use('default')

# data set
python = [18.828,
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
nodejs = [18.893,
          18.57,
          18.757,
          18.734,
          18.796,
          18.584,
          18.663,
          18.51,
          18.654,
          18.611
          ]
lua = [18.809,
       18.515,
       18.659,
       18.607,
       18.646,
       18.985,
       18.791,
       18.706,
       18.667,
       18.651
       ]
rscript = [18.549,
           18.502,
           18.801,
           18.651,
           18.928,
           18.498,
           18.901,
           18.678,
           18.676,
           18.696
           ]

patterns = ['/', 'O', '*', '']
color = ['#ffffff', '#bababa', '#000000', '#c1deff']

bp = plt.boxplot([python, nodejs, lua, rscript], labels=['Python', 'NodeJS', 'Lua', 'Rscript'], patch_artist=True,
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