
duplicates=str(input('list with duplicates: '))
duplicateSplit=duplicates.split(',')
duplicatedSet={None}
duplicatedList=[]
for i in range(len(duplicateSplit)):
    duplicatedSet.add(duplicateSplit[i])

