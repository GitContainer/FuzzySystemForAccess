import xlrd
from xlrd import open_workbook, cellname


workbook = xlrd.open_workbook('hospital_data.xlsx')
sheet_names = workbook.sheet_names()
sheet = workbook.sheet_by_name(sheet_names[2])

for row_idx in range(sheet.nrows):
    for col_idx in range(sheet.ncols):
        cell = sheet.cell(row_idx, col_idx)
        print(cell.value, end="\t")
    print()



# arrayofvalues = sheet.col_values(1)
#
# print(arrayofvalues)