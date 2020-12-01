f = open('input.txt', 'r')

numbers = list(map(int, map(str.strip, f.readlines())))
i = 0
while i < len(numbers):
    j = i
    while j < len(numbers):
        if numbers[i] + numbers[j] == 2020:
            print(numbers[i], '*', numbers[j], '=', numbers[i] * numbers[j])
        j += 1
    i += 1
