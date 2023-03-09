cars = {}

line = input("Car: ")
while line:
  if not(line in cars):
    cars[line] = 1
  else:
    cars[line] = cars[line] + 1
  line = input("Car: ")
for car in cars:
  print('Cars that are', car + ':', cars[car])
  
  
