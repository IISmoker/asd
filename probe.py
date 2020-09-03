import openpyxl
from openpyxl.reader.excel import load_workbook

wb = load_workbook(
    filename='./lxml/vremennoe_raspisanie_iti_03_05.09.2020.xlsx', data_only=True)

sheet = wb.active

print(sheet['G3'].value)
print(sheet['G4'].value)
