#Make dictionary called reps (repeats)
reps = {}
inp = []
tup = tuple()
#take inputs, and lowercase.
#split into a list, and make each bigram a tuple (for loop, index list i and i plus one, repeating one less time than the number of words)
line = input('Line: ')
line = line.lower()
while line:
  inp = line.split()
  #use the two word tuples as keys, and each time we find a bigram:
  #if it is in the dic, increment its value by one
  #else add a new entry with the two word tuple as its key
  for i in range(len(inp) - 1):
    tup = tuple([inp[i], inp[i+1]])
    if tup in reps:
      reps[tup] = reps[tup] + 1
    else:
      reps[tup] = 1
  inp = []
  line = input('Line: ')
  line = line.lower()
for big in reps:
  if reps[big] > 1:
    print(' '.join(big) + ': ' + str(reps[big]))

#print out the dictionary, joining (' '.join() method) the tuples into a str, and then printing out the tuples key
