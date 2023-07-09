import openpyxl


wb = openpyxl.load_workbook("C:\\work\\CB_VMList.xlsx")

ws = wb.active
print(ws["A1"].value)