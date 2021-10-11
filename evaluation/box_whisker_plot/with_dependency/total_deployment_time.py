import matplotlib.pyplot as plt

plt.figure(figsize=(6, 8), dpi=300)

plt.style.use('default')

# data set
python_without_dependency = [196.048,
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
python_with_dependency = [288.416,
                          263.582,
                          338.196,
                          279.046,
                          275.146,
                          290.462,
                          269.955,
                          271.682,
                          266.816,
                          274.198
                          ]

patterns = ['/', '']
color = ['#ffffff', '#bababa']

bp = plt.boxplot([python_without_dependency, python_with_dependency],
                 labels=['Python w/o dependency ', 'Python w/ dependency'], patch_artist=True,
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