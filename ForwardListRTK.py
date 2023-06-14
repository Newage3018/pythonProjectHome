import pandas as pd # подключение модуля pandas
df = pd.read_excel('forwardList.xlsx')
NumbersList = list(map(str, df['№ телефона'].tolist()))
ForwardsList = list(map(str, df['№ переадресации'].tolist()))
LengthOfList = len(NumbersList)


NumbersListOut = list(map(lambda x: '+7812' + x, NumbersList))
ForwardsListOut = list(map(lambda x: '8107' + x, ForwardsList))

print(NumbersListOut)
print(ForwardsListOut)


MyFile = open('переадпесация.txt', 'w')

for k in range(LengthOfList-1):
    MyFile.writelines(NumbersListOut[k] + ' ' + ForwardsListOut[k] + '\n')

MyFile.close()