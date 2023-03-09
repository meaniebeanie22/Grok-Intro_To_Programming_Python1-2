f = open('input.txt')
i = 0

for line in f:
  line = line.lower()
  i = i + 1
  if line.count('a') > 2 and line.count('r') > 1 and line.count('d') > 0 and line.count('v') > 0 and line.count('k') > 0:
    print('Aardvark on line', i)
  