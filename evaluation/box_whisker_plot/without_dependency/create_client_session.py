import matplotlib.pyplot as plt

plt.figure(figsize=(6, 8), dpi=300)

plt.style.use('default')

# data set
python = [2.599473,
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
nodejs = [2.613705,
          1.910174,
          2.07998,
          2.432857,
          1.798717,
          1.803249,
          1.746301,
          2.044019,
          1.619959,
          1.984309
          ]
lua = [2.053794,
       1.722626,
       2.141747,
       1.878339,
       1.962409,
       2.026613,
       3.117053,
       1.871906,
       2.066021,
       2.011341
       ]
rscript = [1.688953,
           2.356132,
           2.705457,
           1.620234,
           1.742959,
           2.025301,
           2.576384,
           1.731241,
           1.813245,
           1.836837
           ]

patterns = ['/', 'O', '*', '']
color = ['#ffffff', '#bababa', '#000000', '#c1deff']

bp = plt.boxplot([python, nodejs, lua, rscript], labels=['Python', 'NodeJS', 'Lua', 'Rscript'], patch_artist=True,
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