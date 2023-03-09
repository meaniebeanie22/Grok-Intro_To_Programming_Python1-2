occurrences = {}
line = input("Enter line: ").split()
while line:
  for i in range(len(line)): 
      if not(line[i] in occurrences):
        occurrences[line[i]] = 1
      else:
        occurrences[line[i]] = occurrences[line[i]] + 1
  line = input("Enter line: ").split()

for word in sorted(occurrences):
  print(word, occurrences[word])
