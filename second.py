#
#
# def remote_control_next():
#     print("yeild 1")
#     yield "a"
#     print("yeild 2")
#     yield "ab"
#     print("yeild 3")
#
# itr=remote_control_next()
#
# print(next(itr))
#
# print ("/////")
#
# print(next(itr))
#
# print ("/////")
#
# print(next(itr))

#
# def func():
#     for i in range(3):
#         yield i
#
# list(func())
#
# for el in func():
#     print(el) # 0
#               # 1

#
# def counter(num):
#     print("Function Starting")
#     for i in range(30):
#         print("going to yield")
#         yield num
#         num+=1
#         print("now we are going to update number")
#
#
# x=counter(4)
# print (next(x))
# print ("/////")
# print (next(x))
# print ("/////")
# print (next(x))
# print ("/////")
# print (next(x))
# print ("/////")
# print (next(x))
# print ("/////")
# print (next(x))
# print ("/////")

import random

def lottery():
    # returns 6 numbers between 1 and 40
    for i in range(6):
        yield random.randint(1, 40)

    # returns a 7th number between 1 and 15
    yield random.randint(1,15)

for random_number in lottery():
       print("And the next number is... %d!" %(random_number))