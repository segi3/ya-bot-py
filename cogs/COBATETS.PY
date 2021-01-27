valid = ['0', 'a']

str1 = 'aab'
str2 = 'aa0a0a0a0a0'

print(all(char in valid for char in str1))