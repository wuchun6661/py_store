def play(n):
    n = int(n)
    if n>1:
        result = play(n-1) + 2
        return result
    else:
        return 10
