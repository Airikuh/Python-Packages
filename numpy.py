# importing library
import numpy
#initialize list
my_list = [[1,2,3],[4,5,6]]
#Create numpy array from list (1.a)
A = numpy.array(my_list)
#print the shape of A (1.b)
print('Shape of array A :', A.shape)
#Reshape 1.c
B = A.reshape(3,2)
#print the shape 1.d
print('Shape of array B :', B.shape)
#1.e
C = B.transpose()
#1.f
print('Shape of array C :', C.shape)
#1.g
D = numpy.concatenate((A, C), axis = 0)
#1.h
print('Shape of array D :', D.shape)
#1.i
print(D)
#1.j
E = numpy.copy(A)
#1.k
E[0, 0] = 10
#1.l
print('Content of A', A)
print('Content of E', E)
