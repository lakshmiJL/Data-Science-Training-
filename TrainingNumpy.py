import numpy as np
import time

nums = [2,8,4,3,7]
print(nums)
print(type(nums))

nums_arr = np.array(nums)
print(nums_arr)
print(type(nums_arr))

for item in nums:
    print(item*2)

print(nums_arr*2)

"""t1 = time.time()
l1 = [i for i in range(1000000)]
t2=time.time()
print("Time for list", t2-t1)
t1 = time.time()
a1 = np.arange(0,1000000)
t2=time.time()
print("Time for array", t2-t1)"""

#zeros
z1 = np.zeros(5, int)
print(z1)

#ones
o1 = np.ones((5,2))
print(o1)

print(z1.ndim)
print(o1.ndim)

print(z1.shape)
print(o1.shape)

print(z1.size)
print(o1.size)

#range

arr1 = np.arange(10,21,2)
print(arr1)

arr2 = np.linspace(10,21,4)
print(arr2)

#reshape
new = arr1.reshape(3,2)
print(new)
one = new.reshape(6)
print(one)

#permutation
print(np.random.permutation(arr1))
print(np.random.permutation(arr1))
print(np.random.permutation(arr1))

#random numbers
r1 = np.random.randint(1,50,10)
print(r1)
print(np.random.permutation(r1))
n1= np.random.permutation(r1)

r2 = np.random.randint(1,50,(3,4))
print(r2)
print(np.random.permutation(r2))

#sort
print(n1)
print(np.sort(n1))
#print(n1)

#slicing
print(n1[2:7])
print(n1[:7])
print(n1[2:])
print(n1[::2])
print(n1[::-1])

#select indices
print(n1[[1,2,5,8]])

#conditional slicing
print(n1[n1 % 2 == 0])
print(n1[n1>20])

#slicing 2D array
print(r2[0:1, 1:])

def cal(x):
    return 2*x**2 + 3

n = np.arange(1,11)
print(cal(n))
#res = 2*n**2 + 3

x = np.arange(1,5)
y = np.arange(11,15)
print(x+y)
print(x-y)
print(x**y)