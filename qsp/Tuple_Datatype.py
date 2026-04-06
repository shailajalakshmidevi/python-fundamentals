
## it is the collection of homogenous or heyrogenous data item enclosed between ()

##synatx:  var = (val1, val2,.....)      or     var = val1, va2,.......

tuple1 = (2,3,4,5)           ## homogenous tuple
tuple2 = (2,4.5, 'hii')      ## hetrogenous tuple
print(type(tuple2))
print(len(tuple1))

print(bool(()))              ## the default value for tuple is () which is internally boolean False

tuple3 = 1,2,'hii', 90-9j, 7.8
print(tuple3)

tuple4 = (10)
print(type(tuple4))
tuple5 = ('hii')
print(type(tuple5))

tuple4 = (10,)
print(type(tuple4))
tuple5 = ('hii',)
print(type(tuple5))

print(dir(tuple5))

## count()

tuple6 = (1,1,1,3,4,3,3)
print(tuple6.count(1))
print(tuple6.count(10))

## index()

tuple6 = (1,1,1,3,4,3,3)
print(tuple6.index(1))
print(tuple6.index(4))

## variable[index] = new_value

tuple6 = (1,1,1,3,4,3,3)
# tuple6[0] = 100                    ## tuples are immutable data type(we can't modify anything in original collection)

####################################################################

tuple7 = (12, 'hello', ['python', 560, 6.6, ['sql', 600, 6.7]], 'webtech', 900)

## difference between list and tuple

## list

## it is mutable in nature
## The boundary of list is []
## we can have single element inside the list
## it is less effcient



## tuple

## it is immutable in nature
## the boundary of tuple is ()
## we can have the single element inside the tuple with comma
## it is more effcient

#############################################################################

## indexing

tuple8 = ('evening', 500, ['python', ('sql'), ('program',), ('program')], 900)
print(tuple8[1])
print(tuple8[2][0][5])
print(tuple8[2][1][0])
print(tuple8[2][2][0][3])
print(tuple8[2][3][3])


