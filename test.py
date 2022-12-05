
import openpyxl
from openpyxl import Workbook

wb = openpyxl.load_workbook("DataTYX.xlsx")

wb.create_sheet("jesus")



wb.save("DataTYX.xlsx")