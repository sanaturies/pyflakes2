
#Given the array candies and the integer extraCandies, where candies[i] represents the number of candies that the ith kid has.
#For each kid check if there is a way to distribute extraCandies among the kids such that he or she can have the greatest number of candies among them. Notice that multiple kids can have the greatest number of candies.

#attempt one
'''candies=str(input("how many candies does each kid have?"))
candysplit=candies.split(',')
candy=len(candysplit)
candysplitint=[]
tf=[]
biggest=0
for i in range(candy):
    candysplitint.append(int(candysplit[i]))
extra=int(input("how many extra candies are there?"))
kids=[]
for i in range(candy):
    j=candysplitint[i]+extra
    kids.append(j)
for i in range(candy):
    if kids[i]>biggest:
        biggest=kids[i]
for i in range(candy):
    if candysplitint[i]<biggest:
        print(candysplitint[i])'''
# attempt two
candies=str(input("how many candies does each kid have?"))
candysplit=candies.split(',')
candy=len(candysplit)
candysplitint=[]
tf=[]
biggest=0
extra=int(input("how many extra candies are there?"))

for i in range(candy):
    candysplitint.append(int(candysplit[i]))
for i in range (candy):
    if candysplitint[i]>biggest:
        biggest=candysplitint[i]

for i in range(candy):
    candyplusthree=candysplitint[i]+extra
    if candyplusthree>biggest:
        tf.append(True)
    else:
        tf.append(False)
print(tf)