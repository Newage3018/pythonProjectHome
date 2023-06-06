import pandas as pd # подключение модуля pandas
"""
Встроенная в Python функция map() используется для применения функции к каждому элементу итерируемого объекта
(например, списка или словаря) и возврата нового итератора для получения результатов.
Функция map() возвращает объект map (итератор), который мы можем использовать в других частях нашей программы.
Также мы можем передать объект map в функцию list() или другой тип последовательности для создания
итерируемого объекта.
"""
df = pd.read_excel('msan.xlsx', sheet_name='Порты')  # чиитаем из excel файла  'msan.xlsxэ из листа 'Порты'
#  в кадр данных (DataFrame - сущность библиотеки pandas - объект данных)
NumbersList = list(map(str, df['№ телефона'].tolist())) #  сразу хоим получить список состоящий ТОЛЬКО из строк
print(NumbersList)

#  GoodNumbers = []
OutNumbers = []
'''
for TelNumber in NumbersList:
    if TelNumber != 'nan' and TelNumber != 'резервные гнёзда' and TelNumber != 'Не используется в линии':
        GoodNumbers.append(TelNumber)
print(GoodNumbers)
'''
for TelNumber in NumbersList:
    if TelNumber[0] == '8' and TelNumber[3] != '0':
        OutNumbers.append(TelNumber)
print(OutNumbers)



'''
for TelNumber in GoodNumbers:
    if TelNumber[3] != '0':
        OutNumbers.append(TelNumber)
print(OutNumbers)
'''


MyFile = open('smku.txt', 'w')
OutNumbers = map(lambda x: '+7'+x + '\n', OutNumbers)
MyFile.writelines(OutNumbers)
MyFile.close()


