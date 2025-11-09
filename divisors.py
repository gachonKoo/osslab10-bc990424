import sys

numbers = int(sys.argv[1])

for i in range(numbers):
  
  if numbers % i == 0:
    print(i,end=" ")

print()
