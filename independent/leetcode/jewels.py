
#find number of jewels present in stones
jewels=str(input('jewel charecter/words?'))
jewelsplit=jewels.split()
stones=str(input('stone charecter/words?'))
stonesplit=stones.split()
count=0
for i in range(len(jewelsplit)):
    if jewelsplit[i] in stonesplit:
        count+=1
print(count)