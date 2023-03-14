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


#OR

from bokeh.palettes import HighContrast3
from bokeh.plotting import figure, show

fruits = ['Apples', 'Pears', 'Nectarines', 'Plums', 'Grapes', 'Strawberries']
years = ["2015", "2016", "2017"]

data = {'fruits' : fruits,
        '2015'   : [2, 1, 4, 3, 2, 4],
        '2016'   : [5, 3, 4, 2, 4, 6],
        '2017'   : [3, 2, 4, 4, 5, 3]}

p = figure(x_range=fruits, height=250, title="Fruit Counts by Year",
           toolbar_location=None, tools="hover", tooltips="$name @fruits: @$name")

p.vbar_stack(years, x='fruits', width=0.9, color=HighContrast3, source=data,
             legend_label=years)

p.y_range.start = 0
p.x_range.range_padding = 0.1
p.xgrid.grid_line_color = None
p.axis.minor_tick_line_color = None
p.outline_line_color = None
p.legend.location = "top_left"
p.legend.orientation = "horizontal"

show(p)
