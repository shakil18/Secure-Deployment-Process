import matplotlib.pyplot as plt

plt.figure(figsize=(6, 8), dpi=300)

plt.style.use('default')

# data set
python = [57.238271,
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
nodejs = [44.1414714,
          40.058058,
          41.193678,
          43.165143,
          41.765842,
          42.244289,
          41.616009,
          39.462987,
          39.51865,
          39.637977
          ]
lua = [42.858333,
       39.551231,
       39.424417,
       40.495161,
       39.585148,
       40.218925,
       39.620675,
       40.116705,
       40.175951,
       39.31729
       ]
rscript = [42.980808,
           39.654078,
           39.588758,
           39.324807,
           40.601214,
           41.562873,
           45.618309,
           43.542649,
           51.749646,
           44.080743
           ]

patterns = ['/', 'O', '*', '']
color = ['#ffffff', '#bababa', '#000000', '#c1deff']

bp = plt.boxplot([python, nodejs, lua, rscript], labels=['Python', 'NodeJS', 'Lua', 'Rscript'], patch_artist=True,
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