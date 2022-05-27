
# You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest customer has.
# A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.

bankaccounts=int(input('number of accounts'))
banklist=[]
for i in range(bankaccounts):
    bankaccount=input('list of money in each account')
    bankaccountamount=bankaccount.split(',')
    for i in range(len(bankaccountamount)):
        bankaccountamount[i]=int(bankaccountamount[i])
    banklist.append(sum(bankaccountamount))
print(max(banklist))


