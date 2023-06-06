List = [1, 'tt', 'tt', 3, 5, 3, 'tt', 'tt', 'tt']
OutList = []
for element in List:
    if element != 'tt':
        OutList.append(element)
print(OutList) # [1, 3, 5, 3]