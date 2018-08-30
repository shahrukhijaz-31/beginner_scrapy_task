import time;
import datetime;

class Comparison:
  # def __init__(self, n, age):
  #   self.name = name
  #   self.age = age

    def list_genderator(self,num,list):
        print("Processing of List Generater by Loop")
        print("Time to enter in function ::  {0}".format(time.strftime("%I:%M:%S")))
        for i in range(num+1):
            list.append(i)
        print("Time to exit in function ::  {0}\n".format(time.strftime("%I:%M:%S")))


    def list_compreshension(self,num,list):
        print("Processing of List Generater by Comprehension")
        print("Time to enter in function ::  {0}".format(time.strftime("%I:%M:%S")))
        list=[x for x in range (1,num+1)]
        print("Time to exit in function ::  {0}\n".format(time.strftime("%I:%M:%S")))


list=[]
list2=[]
obj=Comparison()
obj.list_genderator(100000000,list)


obj.list_compreshension(100000000,list)

print("So we can conclude that list comprehension is more efficient than for loop")
