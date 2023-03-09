eng = set(open('english.txt'))
frog = set(open('french.txt'))

for item in eng & frog:
  print(item.strip())
