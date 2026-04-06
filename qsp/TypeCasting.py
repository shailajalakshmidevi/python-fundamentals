
## It helps convert one type of data into another type based on our requriment

## syntax:  dest_var = dest_type(Source_var)

## Integer

Integer = 100
Float = float(Integer)
print(Float)
print(complex(Integer))
print(complex(Integer, 89))
print(bool(Integer))
print(bool(0))
print(str(Integer))
print(type(str(Integer)))
# print(list(Integer))
# print(tuple(Integer))
# print(set(Integer))
# print(dict(Integer))

## Float

Float = 9.7
print(int(Float))
print(complex(Float))
print(complex(Float, 6))
print(bool(Float))
print(bool(0.0))
print(str(Float))
print(type(str(Float)))
# print(list(Float))
# print(tuple(Float))
# print(set(Float))
# print(dict(Float))

## Complex

Complex = 3+89j
print(Complex)
# print(int(Complex))
# print(float(Complex))
print(bool(Complex))
print(bool(0j))
print(str(Complex))
print(type(str(Complex)))
# print(list(Complex))
# print(tuple(Complex))
# print(set(Complex))
# print(dict(Complex))

## Boolean

a = True
b = False
print(int(a), int(b))
print(float(a), float(b))
print(complex(a), complex(b))
print(complex(a, 3), complex(b,6.7))
print(str(a), str(b))
print(type(str(a)), type(str(b)))
# print(list(a), list(b))
# print(tuple(a), tuple(b))
# print(set(a), set(b))
# print(dict(a), dict(b))

## String

string = 'hello14$%5'
# print(int(string))
# print(float(string))
# print(complex(string))
print(bool(string))
print(bool(''))
print(list(string))
print(tuple(string))
print(set(string))
# print(dict(string))

string = '12343234'
print(int(string))
print(float(string))
print(complex(string))
print(bool(string))
print(bool(''))
print(list(string))
print(tuple(string))
print(set(string))
# print(dict(string))

## list

list_ = [23, 'hai', 6.7, 9-9j]
# print(int(list_))
# print(float(list_))
# print(complex(list_))
print(bool(list_))
print(bool([]))
print(str(list_))
print(tuple(list_))
print(set(list_))
# print(dict(list_))


list_ = ['ab', [1,2], (11,22)]    ## we can convert the list to dict only when each element of the list is of length 2
print(dict(list_))

## tuple
## set

## dict

dict_ = {'a': 'b', 1: 2, 11: 22}
# print(int(dict_))
# print(float(dict_))
# print(complex(dict_))
print(bool(dict_))
print(bool({}))
print(str(dict_))
print(list(dict_))
print(list(dict_.values()))
print(list(dict_.items()))
print(tuple(dict_))
print(tuple(dict_.values()))
print(tuple(dict_.items()))
print(set(dict_))
print(set(dict_.values()))
print(set(dict_.items()))
