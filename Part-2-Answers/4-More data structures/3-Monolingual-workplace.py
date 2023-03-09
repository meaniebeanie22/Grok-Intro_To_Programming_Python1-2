line = set((input('Line: ').split())[1:])
filth = set()
good = set()
while line:
  for name in line:
    if name in filth:
      filth.remove(name)
      good.add(name)
    elif not(name in good):
      filth.add(name)
  line = set((input('Line: ').split())[1:])
if filth:
  for nama in filth:
    print(nama, 'is monolingual.')
else:
  print("Everyone is multilingual!")
   
