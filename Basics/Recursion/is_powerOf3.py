def isPowOF3(n):
    # base case
    if n <= 0:
        return False
    if n == 1:
        return True
    if n % 3 != 0:
        return False
    
    # recursive case
    return isPowOF3(n//3)

print(isPowOF3(9))