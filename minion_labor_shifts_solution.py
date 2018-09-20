#!/usr/bin/python

import collections

# Option 1: Create a dictionary {'num','count'}
def answer1(data, n):

   # make a dictionary where the keys are the numbers
   # and values are the occurences
   stats = dict((x,data.count(x)) for x in set(data))
                  
   # only return the numbers that occur <= n times
   return [i for i in data if stats[i] <= n]

# Option 2: Use collections
def answer2(data, n):
   stats = collections.Counter(data)
   return [i for i in data if stats[i] <= n]

if __name__ == "__main__":

   print answer1([5,10,15,10,7], 1)
   print answer1([1, 2, 2, 3, 3, 3, 4, 5, 5],1)
   print answer1([1, 2, 3],0)
   print answer1([1, 2, 3], 6)
