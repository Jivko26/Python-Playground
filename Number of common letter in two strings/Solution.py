string_one = input()
string_two = input()

def func(string_one, string_two):
    common = 0
    common_letters = []
    for i in range(len(string_one)):
        for y in range(len(string_two)):
            if string_one[i] == string_two[y] and string_one[i] not in common_letters:
                common += 1
                common_letters.append(string_one[i])
    return common

result = func(string_one, string_two)
print(result)