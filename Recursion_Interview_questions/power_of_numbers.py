############### power of numbers using recursion #############


def power(base,expo):
    assert expo>=0 and int(expo)==expo, "Please enter positive whole numbers only"
    if expo == 0:
        return 1
    if expo== 1:
        return base

    else:
        return base * power(base,expo-1)

print(power(2,4))