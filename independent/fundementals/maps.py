
from collections import ChainMap
import collections
dict1={
    'day1':'mon',
    'day2':'tue',
    'day3':'wed'
}
dict2={
    'day4':'thurs',
    'day5':'fri',
    'day6':'sat'
}
mep=collections.ChainMap(dict1,dict2)
print(mep)