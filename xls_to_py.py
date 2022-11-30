import xlrd
import numpy as np
import datetime
book = xlrd.open_workbook("APPL.xls")
sh = book.sheet_by_index(0)

lx = sh.nrows
ly = sh.ncols

data = []


for rx in range(1,lx):
    for ry in range(ly):
        if ry == 0:
            data.append(['%s' % datetime.datetime(*xlrd.xldate_as_tuple(sh.cell_value(rowx=rx, colx=ry), book.datemode))])
            print(data)
        else:
            data[rx - 1].append(sh.cell_value(rowx=rx, colx=ry))

print(data)