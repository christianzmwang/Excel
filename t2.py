
from openpyxl import load_workbook, Workbook

wb = load_workbook("names.xlsx")
ws = wb['eg']
for i in ws.values:
  print(i)



