calculations = int(input())

def leibnitz(calculations):
    divider = 3
    n = 2
    result = 1/1
    while n <= calculations:
        if n % 2 == 0:
            result -= 1/divider
        else:
            result += 1/divider
        divider += 2
        n += 1
    return 4 * result

output = leibnitz(calculations)
print(output)