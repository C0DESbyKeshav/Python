import numpy as np
# a = np.array([1, 2, 3, 4, 5])
# print(a)  # print 1D array
# print(a[2])  # print element at index 2
# print(a[1:4])  # print slicing operation
# b = a.reshape(5, 1)  # perform reshaping
# print(b)

# a = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
# print(a)  # print 2D array
# print(a[0, 2])  # print element at index 2
# print(a[0: 2])  # print slicing operation
# b = a.reshape(4, 2)  # perform reshaping
# print(b)

a = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(a)  # print 3D array
print(a[1, 1, 0])  # print element at index
print(a[:1])  # print slicing operation
b = a.reshape(2, 2, 2)  # perform reshaping
print(b)
