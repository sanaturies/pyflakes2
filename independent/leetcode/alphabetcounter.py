
deck={}
s='sana  Murthy hebbal'
li='abcdefghijklmnopqrstuvwxyz'
lic=li.upper()
for i in s:
    if i in li or i in lic:
        deck.update({i:s.count(i)})
print(deck)