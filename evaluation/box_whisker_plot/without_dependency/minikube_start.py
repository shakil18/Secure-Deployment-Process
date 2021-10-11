import matplotlib.pyplot as plt

plt.figure(figsize=(6, 8), dpi=300)

plt.style.use('default')

# data set
python = [113.893,
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
nodejs = [114.874,
          100.516,
          102.704,
          99.348,
          99.411,
          98.609,
          101.282,
          103.345,
          99.484,
          98.941
          ]
lua = [109.68,
       100.398,
       94.685,
       102.064,
       98.681,
       97.364,
       98.356,
       100.463,
       100.425,
       98.705
       ]
rscript = [112.342,
           95.38,
           99.128,
           102.221,
           98.955,
           102.941,
           104.22,
           99.779,
           101.268,
           100.482
           ]

patterns = ['/', 'O', '*', '']
color = ['#ffffff', '#bababa', '#000000', '#c1deff']

bp = plt.boxplot([python, nodejs, lua, rscript], labels=['Python', 'NodeJS', 'Lua', 'Rscript'], patch_artist=True,
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