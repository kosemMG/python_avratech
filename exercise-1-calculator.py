rate = 3.54
currency = raw_input('Input the currency you want to convert (Dollar or Shekel): ')

if currency != 'Dollar' and currency != 'Shekel':
    print('Please enter correct currency.')
else:
    amount = input('Enter amount: ')
    if currency == 'Dollar':
        print('Convert Dollar to Shekel: ')
        print('%s NIS' % (amount / rate))
    else:
        print('Convert Shekel to Dollar: ')
        print('%s dollars' % (amount * rate))

