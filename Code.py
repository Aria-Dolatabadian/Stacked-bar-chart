import matplotlib.pyplot as plt
labels = ['Chr1', 'Chr2', 'Chr3', 'Chr4', 'Chr5']
TM_LRR = [20, 35, 30, 35, 27]
NBS_LRR = [25, 32, 34, 20, 25]
TM_LRR_std = [2, 3, 4, 1, 2]
NBS_LRR_std = [3, 5, 2, 3, 3]
width = 0.35       # the width of the bars: can also be len(x) sequence
fig, ax = plt.subplots()
ax.bar(labels, TM_LRR, width, yerr=TM_LRR_std, label='TM-LRR')
ax.bar(labels, NBS_LRR, width, yerr=NBS_LRR_std, bottom=TM_LRR,
       label='NBS-LRR')
ax.set_ylabel('Number')
ax.set_title('TM-LRR and NBS-LRR across the chromosomes')
ax.legend()
plt.show()
