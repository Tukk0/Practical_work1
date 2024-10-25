from function import regex_has_a_special_prefix as checker

input = input().split(" ")
regex = input[0]
letter = input[1]
k = int(input[2])
Answer = checker(regex, letter, k)
print(Answer[0])