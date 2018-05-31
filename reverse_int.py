def powerOfTen(num):
    if num == 1:
        return True
    elif num < 1:
        return False
    else:
        return powerOfTen(num/10)

def placeCounter(num, count):
    num = abs(num)
    if num <= 1:
        return count
    else:
        return placeCounter(num/10, count + 1)

def reverseInt(x):
    """
    :type x: int
    :rtype: int
    """

    # Overflow check (not really applicable in Python):
    if x > 2**31 - 1:
        return 0
    elif x < (2**31)*(-1):
        return 0

    # Negative check:
    negative = False
    if x < 0:
        negative = True
        x = abs(x)

    # Power of 10 check:
    if powerOfTen(x):
        if negative:
            return -1
        else:
            return 1

    # 1. Find out how many places it has
    places = placeCounter(x, 0)

    if places == 1:
        return x
    elif places == 0:
        return x

    # 2. Assemble array in reverse expanded form
    order = []
    for i in range(places, 0, -1):
        if i == places:
            order.append(x//10**(i-1))
        else:
            temp = x//10**(i-1)
            sub = (x//10**(i))*10
            order.append((temp - sub)*(10**(places-i)))

    # 3. Return sum of array

    rtn = sum(order)

    # Overflow check 2:
    if rtn > 2**31 - 1:
        return 0
    elif rtn < (2**31)*(-1):
        return 0

    if negative:
        return rtn*(-1)
    else:
        return rtn
