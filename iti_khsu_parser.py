from openpyxl import load_workbook
import os

lxml = './lxml'
dir_list = [os.path.join(lxml, name_table) for name_table in os.listdir(lxml)]
if dir_list:
    date_list = [[x, os.path.getctime(x)] for x in dir_list]
    sort_date_list = sorted(date_list, key=lambda x: x[1], reverse=True)
    print(sort_date_list[0][0])
