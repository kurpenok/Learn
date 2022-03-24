import numpy as np

array = np.array([1, 2, 3])

print(array)
print(array.dtype)
print(type(array))
print(array.shape)
print(array.nbytes)
print()

print(np.zeros(5))
print(np.ones(5))
print(np.zeros_like(5))
print()

print(np.arange(1, 16, 4))
print(np.arange(1, 10))
print(np.arange(5))
print()

print(np.linspace(1, 15, 4))
print()

a = np.linspace(3, 33, 11)
b = np.linspace(-2, -22, 11)
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(5 * a)
print(10 + b)
print()

print(np.sin(a))
print(np.cos(a))
print(np.log(a))
print(a > b)
print()

c = np.arange(20)
print(np.any(c))
print(np.all(c))
print()

print(np.pi)
print(np.e)
print()

print(b.cumsum())
print()

print(np.sort(a))
print(a)
print()

c = np.hstack((a, b, 5 * b))
print(c)
print()

x1, x2, x3 = np.hsplit(a, [3, 5])
print(x1, x2, x3)
print()

print(np.append(a, [1, 2, 3, 4, 5]))
print(np.insert(1, 2, [-1, -1]))
print(a[::-1])
print(a[0:3])
print()

print(np.ones(3, 3))
print(np.eye(3))
print(np.diag(np.array((1, 2, 3, 4]))))
print()

