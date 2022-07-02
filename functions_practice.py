def hello():
    print('Greetings')

hello()

def pack(arg1, arg2, arg3):
    return [arg1, arg2, arg3]

print(pack('Pack 1', 'Pack 2', 'Pack 3'))


def eat_lunch(list1, list2):
  if list1 == 0:
    print('My Lunchbox is empty!')
  elif list1 != 0:
    print('First I eat ' + list1 + ', and ' + 'next I eat ' + list2 + '!')

eat_lunch('Candies', 'Chocolates')