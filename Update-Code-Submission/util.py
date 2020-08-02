def isInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

def formatNumber(num):
    if num % 1 == 0:
        return int(num)
    else:
        return num