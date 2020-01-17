#Импортируем библиотеку
import win32com.client
#Создаем COM объект
Excel = win32com.client.Dispatch("Excel.Application")
#Получаем доступ к активному листу
wb = Excel.Workbooks.Open(u'C:\\python\\script.xlsx')
sheet = wb.ActiveSheet
#Получим значение ячейки A1 активного листа
val = sheet.Cells(1,1).value
print(val)
#Получим значения диапазона A1:A2 активного листа
vals = [r[0].value for r in sheet.Range("A1:A2")]
print(vals)
#Запишем новое значение в ячейку A3 активного листа
sheet.Cells(3,1).value = 'A3Value'
#Сохраним
wb.Save()
#Получаем доступ к листу - Лист2 и диапазону ячеек
sheet2 = wb.Worksheets(u'Лист2').Range('A1:A2')
#Получим значения диапазона A1:A2 Лист2
vals = [r[0].value for r in sheet2]
print(vals)
#Закроем файл
wb.Close()
#Закроем COM объект
Excel.Quit()

 
