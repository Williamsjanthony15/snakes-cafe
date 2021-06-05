question = '** What would you like to order? **'
print('$ python snakes_cafe.py')
print('**************************************')
print('**   Welcome to the Snakes Cafe!    **')
print('**   Please see our menu below.     **')
print('**                                  **')
print('** to quit at any time, type "quit" **')
print('**************************************')
print('')
print('Appetizers')
print('----------')
print('Wings')
print('Cookies')
print('Spring Roles')
print('')
print('Entrees')
print('-------')
print('Salmon')
print('Steak')
print('Meat Tornado')
print('A literal Garden')
print('')
print('Desserts')
print('--------')
print('Ice Cream')
print('Cake')
print('Pie')
print('')
print('Drinks')
print('------')
print('Coffee')
print('Tea')
print('Unicorn Tears')
print('')
print('***********************************')
print(question)
print('***********************************')

order = input('> ')
def getOrder(order: str) -> str:
    return f'** {i} order of {order} have been added to your meal **'

  


quit = False
i = 1
while(not quit):
  if order != '':
    print(getOrder(order))
    i += 1
  if input('> ') == 'quit':
    break



