def fab(n):
    if n < 1:
        return -1
    if n == 1 or n == 2:
        return 1
    else:
        return fab(n-2) + fab(n-1)

        
