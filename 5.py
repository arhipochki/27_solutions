'''
    Надо подобрать тесты
'''

N = int(input())

MaxDiv7Even = 0
MaxEven = 0
MaxDiv7Odd = 0
MaxOdd = 0
d = 160
P1 = 1
P2 = 1

for i in range(N):
    newItem = int(input())

    if newItem % 2 == 0:
        if newItem % 7 == 0 and newItem % d != MaxEven % d and newItem > MaxDiv7Even:
            if MaxDiv7Even > MaxEven:
                MaxEven = MaxDiv7Even
            MaxDiv7Even = newItem
        else:
            if newItem > MaxEven and newItem % d != MaxDiv7Even:
                MaxEven = newItem
    else:
        if newItem % 7 == 0 and newItem % d != MaxOdd % d and newItem > MaxDiv7Odd:
            if MaxDiv7Odd > MaxOdd:
                MaxOdd = MaxDiv7Odd
            MaxDiv7Odd = newItem
        else:
            if newItem > MaxOdd and newItem % d != MaxDiv7Odd:
                MaxOdd = newItem

    if MaxDiv7Even + MaxEven > P1 + P2:
        P1 = MaxDiv7Even
        P2 = MaxEven
    
    if MaxDiv7Even + MaxOdd > P1 + P2:
        P1 = MaxDiv7Even
        P2 = MaxOdd
    
    if MaxDiv7Even + MaxDiv7Odd > P1 + P2:
        P1 = MaxDiv7Even
        P2 = MaxDiv7Odd
    
    if MaxDiv7Odd + MaxEven > P1 + P2:
        P1 = MaxDiv7Odd
        P2 = MaxEven
    
    if MaxDiv7Odd + MaxOdd > P1 + P2:
        P1 = MaxDiv7Odd
        P2 = MaxOdd
    
    if MaxEven % 7 == 0 or MaxOdd % 7 == 0:
        if MaxEven + MaxOdd > P1 + P2:
            P1 = MaxEven
            P2 = MaxOdd

if P1 % 7 == 0 or P2 % 7 == 0:
    print(P1, P2)
else:
    print(0, 0)