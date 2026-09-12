def isPowerOfTwo(n):
    # base case
    if n <= 0:
        return False
    if n == 1:
        return True
    if n % 2 != 0:
        return False
    
    # recursive  case
    return isPowerOfTwo(n // 2)

print(isPowerOfTwo(4))