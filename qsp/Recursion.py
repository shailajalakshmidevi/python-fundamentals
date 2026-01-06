
## The function which calls by itself is called as recursive function and the processs is calledd as recursion

##1. PRINT NUMBERS FROM N TO 0 USING WHILE LOOP

def Count_Down(n):
    while n >= 0:
        print(f'Counting Down {n}')
        n -= 1
# Count_Down(5)

## PRINT NUMBERS FROM N TO 0 USING FOR LOOP

def CountDown(n):
    for num in range(n, -1, -1):
        print(f'Counting Down {num}')
# CountDown(5)

## PRINT NUMBERS FROM N TO 0 USING RECURSION

def CountDown_(n):
    ## Base_Case
    if n >= 0:
        print(f'Counting Down {n}')
        ## Recursive Case
        CountDown_(n - 1)
# CountDown_(5)

##2. PRINT THE NUMBERS FROM 1 - 5, "START" AND "STOP" USING WHILE LOOP

def Count_Up(start, stop):
    while start <= stop:
        print(f'Counting Up {start}')
        start += 1
# Count_Up(1, 5)

##2. PRINT THE NUMBERS FROM 1 - 5, "START" AND "STOP" USING FOR LOOP

def CountUP_(start, stop):
    for num in range(start, stop + 1):
        print(f'Counting Up {num}')
# CountUP_(1, 5)

##2. PRINT THE NUMBERS FROM 1 - 5, "START" AND "STOP" USING RECURSION

def CountUp(start, stop):
    ## Base Case
    if start <= stop:
        print(f'Counting Up {start}')
        ## Recursive Case
        CountUp(start + 1, stop)
# CountUp(1, 5)

##2. PRINT THE NUMBERS FROM 1 - 5, "START" AND "STOP" USING RECURSION (NESTED FUNCTION)

def Get_Stop_Value(stop):
    def Get_Start_Value(start):
        ## Base Case
        if start <= stop:
            print(f'Counting {start}')
            ## Recursive Case
            Get_Start_Value(start + 1)
    Get_Start_Value(1)
# Get_Stop_Value(5)

##3. PRINT THE EVEN NUMBERS FROM 2 - 10, "START" AND "STOP" USING RECURSION

def Get_Even_Num(start, stop):
    if start <= stop:
        if start % 2 == 0:
            print(f'The Even Number is {start}')
        Get_Even_Num(start + 1, stop)
# Get_Even_Num(2, 10)

##or

def Get_Even_Num_(start, stop):
    if start <= stop:
        print(f'The Even Number is {start}')
        Get_Even_Num(start + 2, stop)
# Get_Even_Num_(2, 10)











