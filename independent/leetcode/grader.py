
#find the letter grade for a certain cource.
classes=6
dct={
        'a':90,
        'b':80,
        'c':70,
        'd':60,
        'f':50   
    }
lst=['a','b','c','d','f']
for  i in range(classes):
    import random
    r=random.randint(0,100)
    print(r)
    for i in lst:
        if r>=dct[i]:
            print(i)
            break

classes=6
dct={
       'a':90,
       'b':80,
       'c':70,
       'd':60,
       'f':50  
   }
lst=['a','b','c','d','f']
for  i in range(classes):
   import random
   r=random.randint(0,100)
   print(r)
   for i in lst:
       if r>=dct[i]:
           break
   print(i)
    