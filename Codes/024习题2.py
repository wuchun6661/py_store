def get_digits(n):
    n = int(n)
    result = []
    if n:
        result = get_digits(n//10)
        result.append(n%10)
        return result
    else:
        return result
