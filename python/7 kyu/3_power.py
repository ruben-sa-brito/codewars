def three_powers(n):
    if n < 3: return False

    mx = len(str(bin(n))[2:])
    power_2 = [2**x for x in range(mx)]
    dif = int((n - 2**(mx-1)))
    
    if dif in power_2 or str(bin(dif))[2:].count('1') == 2 or dif == 0: return True
    return False