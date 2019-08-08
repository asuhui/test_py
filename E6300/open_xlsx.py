#utf-8
import openpyxl


wb=openpyxl.load_workbook("test.xlsx")
print(wb.sheetnames)
sheet=wb.worksheets[0]
print(sheet)