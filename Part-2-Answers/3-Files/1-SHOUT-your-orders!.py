f = open('orders.txt')
for line in f:
  print(line.strip().upper())