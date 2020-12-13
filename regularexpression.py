import re
result = re.match("[a-z]+@[a-z]+.[a-z]{3}", 'trupthibhyregowda@gmail.com')
print(result)
result = re.search("[a-z]+", 'trupthibhyregowda@gmail.com')
print(result)
result = re.findall("[a-z]+", 'trupthibhyregowda@gmail.com')
print(result)

