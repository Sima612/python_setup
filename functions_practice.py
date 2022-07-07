def hello():
    print('Greetings')

hello()

def pack(arg1, arg2, arg3):
    return [arg1, arg2, arg3]

print(pack('Pack 1', 'Pack 2', 'Pack 3'))

def eat_lunch(list1):
  if len(list1) == 0:
    print('My Lunchbox is empty!')
  for i in range(len(list1)):
    if i == 0:
      print(f'First I eat {list1[0]}')
    else:
      print(f'Next I eat {list1[i]}')

eat_lunch(['candies', 'chocolates'])