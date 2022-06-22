
from matplotlib import pyplot
from openpyxl import load_workbook

wb = load_workbook('data_analysis_lab.xlsx')            # load file
sheet = wb['Data']                                      # get sheet
val_a = sheet['A'][1:]                                  # without head
val_d = wb['Data']['D'][1:]
val_c = wb['Data']['C'][1:]

def getvalue(x):
    return x.value


years = list(map(getvalue, val_a ))
act_sun = list(map(getvalue, val_d ))
temp = list(map(getvalue, val_c ))


# "a is %d, b is %2d" % (a,b)  pattern format


pyplot.plot(years, act_sun, 'r--')
pyplot.plot(years, temp, 'g-.')
pyplot.show()


