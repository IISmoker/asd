import xlrd

table = xlrd.open_workbook('./lxml/vremennoe_raspisanie_iti_03_05.09.2020.xlsx', formatting_info=False)
sheet = table.sheet_by_index(0)
group = sheet.row_values(2)[6]
first_lesson = sheet.row_values(4)[6]
qwe = sheet.row_values(3)[6]
print(group)
print(first_lesson)
print(qwe)
