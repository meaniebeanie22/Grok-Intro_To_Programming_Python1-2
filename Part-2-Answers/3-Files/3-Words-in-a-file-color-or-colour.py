f = open('book.txt').read().lower()
word = input('Word to look for: ')

if word in f:
  print(word,'was found in the book.')
else:
  print(word,'was not found in the book.')