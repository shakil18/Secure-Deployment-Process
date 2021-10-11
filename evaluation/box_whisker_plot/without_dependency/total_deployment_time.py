import matplotlib.pyplot as plt

plt.figure(figsize=(6, 8), dpi=300)

plt.style.use('default')

# data set
python = [196.048,
          199.372,
          181.664,
          182.246,
          181.55,
          180.457,
          182.318,
          179.991,
          182.12,
          182.352
          ]
nodejs = [184.142,
          181.374,
          183.999,
          182.594,
          181.01,
          179.392,
          184.332,
          177.988,
          181.737,
          178.245
          ]
lua = [176.941,
       178.736,
       173.991,
       181.828,
       178.24,
       178.837,
       178.894,
       180.319,
       180.234,
       177.383
       ]
rscript = [179.3,
           177.168,
           179.989,
           181.049,
           179.715,
           184.23,
           192.167,
           182.959,
           192.884,
           184.56
           ]

patterns = ['/', 'O', '*', '']
color = ['#ffffff', '#bababa', '#000000', '#c1deff']

bp = plt.boxplot([python, nodejs, lua, rscript], labels=['Python', 'NodeJS', 'Lua', 'Rscript'], patch_artist=True,
                 medianprops={'linewidth': 2})

plt.title('Total deployment time')
plt.ylabel('Time (seconds)')

for box in bp['boxes']:
    # change outline color
    # box.set(color='#4286f4', linewidth=2)
    # change fill color
    box.set(facecolor=color.pop(0))
    # change hatch
    # box.set(hatch = patterns.pop(0))

plt.savefig('figures/Total deployment time.png', dpi=300)

plt.show()