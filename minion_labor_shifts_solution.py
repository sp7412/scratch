#!/usr/bin/python

import collections

# Option 1: Create a dictionary {'num','count'}
#           using a list comprehension
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

# Option 3: Create a dictionary   
def answer(data, n):
   stats = {}
   for num in data:
      # stats.get the current count for num
      stats[num] = stats.get(num, 0) + 1
   for num in stats:
      if stats[num] > n:
         # if num occurs more than n
         for i in range(stats[num]):
            # remove all occurences of num from data
            data.remove(num)
   return data


if __name__ == "__main__":

   print answer([5,10,15,10,7], 1)
   print answer([1, 2, 2, 3, 3, 3, 4, 5, 5],1)
   print answer([1, 2, 3],0)
   print answer([1, 2, 3], 6)
