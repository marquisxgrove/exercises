#Python for DevOps - Chapter 1 - Exercises

#Write a Python function that takes a name as an argument and prints that name
def greeting(name):
  print(f"Hello {name}")
  
greeting('Marq')


#Write a Python function that takes a string as an argument and prints whether it is upper-or lowercase
def upper_or_lower(text):
  if text.isupper():
    print(f"{text} is uppercase")
  elif text.islower():
    print(f"{text} is lowercase")
  else:
    print(f"{text} is neither lowercase or uppercase")
    
upper_or_lower("I LOVE PYTHON")
upper_or_lower("i love python")
upper_or_lower("i LovE PytHON")


#Write a list comprehension that results in a list of every letter in the word smogtether capitalized
result = [s.upper() for s in 'smogtether']
print(result)


#Write a generator that alternates between returning Even and Odd
def even_odd():
  n = 2
  while True:
    n += 1
    yield n
    
    
generator = even_odd()

for i in range(10):
  print(next(generator))
