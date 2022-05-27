
#check if the list/str of parentheses are valid
class Solution(object):
    def isValid(self, parentheses):
        dct={
        '(':')',
        '[':']',
        '{':'}',
         ')':'(',
        ']':'[',
        '}':'{'
       
            }
       
        parentheses2=''
        lst=[]
        new=[]
        if len(parentheses)==1:
            return False
        for i in range(1,len(parentheses)+1):
            parentheses2+=parentheses[-i]
        for i in range(len(parentheses2)):
            if parentheses2[i]==dct[parentheses[i]]:
                lst.append(True)
            else:
                lst.append(False)
        if all(lst):
            return True
        else:
            lst=[]
            for i in range(1,len(parentheses),2):
                new.append(parentheses[i-1:i+1])
            for i in range(len(new)):
                for j in range(0,len(new[i]),2):
                    check1=new[i][j]
                    check2=new[i][j+1]
                    dctcheck1=dct.get(check1)
                    dctcheck2=dct.get(check2)
                    if check1==dctcheck2:
                        lst.append(True)
                    elif check2==dctcheck1:
                        lst.append(True)
                    else:
                        lst.append(False)
            if all(lst):
                for i in range(len(lst)):
                       v=new[i]
                       if v==['}','{'] or [']','['] or [')','(']:
                            return False
                       else:
                            return True
            else:
               return False

print(Solution.isValid(Solution,['{','}','(',')']))