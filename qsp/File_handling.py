
## File: It is a container which stores some information/data, based on the extension we get to the type of data stored in the file
## File Handling: It helps to write the data into the file and read the data from the file
## syntax to open the file: with open(file_name/file_path, mode) as var:
## There are 3 types of mode
##1. write mode                 ##2. read mode          ##3. append mode

############################################################################################

## write mode: it helps to write the data into the file

##1. write(): it helps to write the single line of data in the form of string
## syntax:  var.write('data')

with open('file.txt', 'w') as var:
    var.write('Helllo hiiii')

with open('file.txt', 'w') as a:
    a.write('good evening')

## If the file is not present control will create the file and store the data in it
## if the file is already present, it will delete the previous data and store the latest data

##2. writelines(): It helps to write multiple data in to the file in the form of list
## syntax:  var.writelines(['data1', 'data2', ........])

with open('file1.txt', 'w') as b:
    b.writelines(['hello\n', 'hii\n', 'good evening\n', 'how are you???'])

############################################################################################

## read mode: it helps to read the data from the file

##1. read(): it helps to complete data from the file in the form of string
## syntax: var.read()

# with open('file1.txt', 'r') as c:
#     result = c.read()
#     print(result)

##2. readline(): it helps to read single line of data at once
## syntax: var.readline()

# with open('file1.txt', 'r') as c:
#     result = c.readline()
#     result1 = c.readline()
#     print(result, result1)

##3. readlines(): It helps to read complete data from the file in the form of list
## syntax: var.readlines()

# with open('file1.txt', 'r') as c:
#     result = c.readlines()
#     print(result)

###########################################################################################

##3. append mode: it helps to write the data into the file
## the difference between write and append mode is, write mode will override the data whereas the append mode add the data to the file

with open('file.txt', 'a') as d:
    d.write('python is easy')

###########################################################################################

## reading the data using loop

# with open("C:/Users/QSP/Downloads/logfilesample.txt") as a:
#     for line in a:
#         print(line)

# with open("C:/Users/QSP/Downloads/logfilesample.txt") as a:
#     for line in a:
#         print(line.strip())

## get the line number and the line

# with open("C:/Users/QSP/Downloads/logfilesample.txt") as a:
#     for line_no, line in enumerate(a):
#         print(line_no, line.strip())

# with open("C:/Users/QSP/Downloads/logfilesample.txt") as a:
#     for line_no, line in enumerate(a, start = 1):
#         print(line_no, line.strip())

## get the line_no as key and line as value

# with open("C:/Users/QSP/Downloads/logfilesample.txt") as a:
#     dict_ = {}
#     for line_no, line in enumerate(a, start = 1):
#         dict_[line_no] = line
#     print(dict_)

########################################################################################

## reading the data from the file using function

def read_log():
    with open("C:/Users/QSP/Downloads/logfilesample.txt") as a:
        records = []
        for line in a:
            clean_line = line.strip()
            parts = clean_line.split()
            records.append(parts)
        return records
# print(read_log())

## get only the time

def Get_Time():
    res = read_log()
    print(res)
    Get_Time_ = []
    for element in res:
        Get_Time_.append(element[1])
    return Get_Time_
# print(Get_Time())

## Get only unique time without typecasting

def Get_Unique_Time():
    res = Get_Time()
    get_unique_time = []
    for time in res:
        if time not in get_unique_time:
            get_unique_time.append(time)
    return get_unique_time
# print(Get_Unique_Time())

## with typecasting

def Get_Time():
    res = read_log()
    print(res)
    Get_Time_ = []
    for element in res:
        Get_Time_.append(element[1])
    return list(set(Get_Time_))
# print(Get_Time())

## get only messages : WARNING:.....mailslot_create, INFO, Trace
## get only unique message

########################################################################################

## CSV file handling (comma separeted Values)

## write the data into the csv file

# import csv
# with open('file name/file_path', 'w') as var:
#     var1 = csv.writer(var)
#     var1.writerow([data1, data2,...])                            ## it helps to store single row of data
#     var1.writerows([[data1, data2,...], [data1, data2,...], [data1, data2,...]])  ## it helps to store multiple row of data

import csv
with open('file.csv', 'w', newline = '') as a:
    b = csv.writer(a)
    b.writerow(['name', 'age', 'ph_no'])
    b.writerows([['abc', 22, 8765456787], ['xyz', 23, 876545678], ['uvw', 24, 7654345678]])

########################################################################################

## syntax to read the data from the csv file

# import csv
# with open('file_name/filr_path', 'r') as var:
#     var1 = csv.reader(var)
#     print(list(var1))

# with open('file.csv') as a:
#     b = csv.reader(a)
#     print(list(b))

# with open("C:/Users/QSP/Downloads/employees.csv") as a:
#     b = csv.reader(a)
#     print(list(b))

with open("C:/Users/QSP/Downloads/employees.csv") as a:
    b = csv.reader(a)
    for row in b:
        print(row)

## count the number of males and females

# with open("C:/Users/QSP/Downloads/employees.csv") as a:
#     b = csv.reader(a)
#     males, females = 0, 0
#     for row in b:
#         if row[1] == 'male':
#             males += 1
#         elif row[1] == 'female':
#             females += 1
#     print(f'The number of males are {males} and females are {females}')

with open("C:/Users/QSP/Downloads/employees.csv") as a:
    b = csv.reader(a)
    males, females = 0, 0
    b.__next__()
    for row in b:
        if row[1] == 'male':
            males += 1
        else:
            females += 1
    print(f'The number of males are {males} and females are {females}')

## unique department
## total pay









