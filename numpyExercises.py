import numpy as np
#a
array=np.empty((10))
array[4] = 1
print('\t a question answer:%s' % array)

#b
array = np.arange(10,50)
print('\t b question answer:%s' % array)

#c
array = array[ : :-1]
print('\t c question answer:%s' % array)

#d
array = np.arange(0,9)
array_matrix = np.reshape(array, (3, 3))
print('\t d question answer:\n%s' % array_matrix)

#e
array = np.array([1,2,0,0,4,0])
result = np.where(array == 0)
print('\t e question answer:\n%s' % result)

#f
array = np.random.rand((30))
result = array.mean()
print('\t f question answer:\n%s' % result)

#g
matrix = np.ones((10,10))
print('\t g question answer:\n%s' )
print("Original matrix:")
print(matrix)
print("1 on the border and 0 inside in the matrix")
matrix[1:-1,1:-1] = 0
print(matrix)

#h
print('\t h question answer:\n' )
x = np.ones((8,8),dtype=int)
print("Checkerboard pattern:")
x[1::2,::2] = 0
x[::2,1::2] = 0
print(x)

#i
x = np.array([(1,0),(0,1)])
result = np.tile(x, (4, 4))
print('\t i question answer:\n %s' % result)

#j
array = np.arange(11)
array[3:8] = np.multiply(array[3:8],-1)
print('\t j question answer:\n %s' % array)

#k
array = np.random.random(10)
array = np.sort(array)
print('\t k question answer:\n %s' % array)

#l. Consider two random array A anb B, check if they are equal
A = np.random.randint(0,2,5)
B = np.random.randint(0,2,5)
equal = np.array_equal(A,B)
print('\t l question answer:\n %s' % equal)

#m. How to convert an integer (32 bits) array into a float (32 bits) in place?
print('\t m question answer:\n ' )
Z = np.arange(10, dtype=np.int32)
print(Z,Z.dtype)
Z = np.float32(Z)
print(Z,Z.dtype)

#n. How to get the diagonal of a dot product?
print('\t n question answer:\n ' )
A = np.arange(9).reshape(3,3)
print(A)
B = A + 1
print(B)
C = np.dot(A,B)
print(C)
D = np.diagonal(C)
print('\t n question answer: original matrix\n%s ' % C,'\n\tdiagonal:%s' % D)


