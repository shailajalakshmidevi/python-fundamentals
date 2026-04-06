
## Slicing helps to get the group of elements from the collection

## syntax:

# variable[start_index:end_index + 1:updation]       ## left to right
# variable[start_index:end_index - 1:updation]       ## right to left

## it always includes the starts index and excludes the end index

## updation helps in two cases
##1. it determines the direction
    ##1. if we have +ve updation control gets to knows it should traverse in left to right direct
    ##2. if we have -ve updation control gets to knows it should traverse in right to left direct
##2. it tells about the element to be considered in the output

## The default value for updation is 1
## The default value for start index is 0
## The default value for end_index is length of the collection

## string slicing

string = 'hello everyone'
print(string[0:4+1:1])
print(string[0:5])
print(string[:5])
print(string[6:13+1])
print(string[6:])
print(string[6:11])
print(string[-8:-4+1])
print(string[6:-3])
print(string[::])
print(string[::-1])
print(string[::2])
print(string[::-2])
print(string[4:1-1:-1])                                          ## olle
print(string[-4:7-1:-1])                                       ## yrev
print(string[7:10+1][::-1])

########################################################################

## List and Tuple slicing

list_ = [4.5, ['python', 67, 8.8, ['program'], 6-9j], 'webtech', ('helllo', 'sql'), ('selenium'), ['bangalore', 'mysore', ('Mumbai', )]]
print(list_[1][1])
print(list_[1][1:])
print(list_[1][1:5])
print(list_[1][0][1:5])
print(list_[::-1])
print(list_[2][4:2-1:-1])                                          ## etb
print(list_[2][2:5][::-1])
print(list_[3][0][2:5])
print(list_[4][-4:2-1:-1])
print(list_[4][2:-4+1][::-1])
print(list_[1][-2][0][1:4])
print(list_[-1][0][-4:3-1:-1])
print(list_[-1][0][3:6][::-1])
print(list_[-1][-1][0][1:-2+1])

##########################################################################################

## Dictionary

dict_ = {1:['icecream', 'juice', 'chocolate'], 2:(122, '3456', 8.7, 9000, ['evening']), 4:{5:{6:{7:'345876'}}}}
print(dict_[1][0][1:5])
print(dict_[1][-1][-3:3-1:-1])
print(dict_[1][-1][3:-3+1][::-1])
print(dict_[2][::-2])
print(dict_[2][1][1:3])
print(dict_[2][2:])
print(dict_[2][-1][0][-3:1-1:-1])
print(dict_[2][-1][0][1:-3+1][::-1])
print(dict_[4][5][6][7][1:-2+1])

