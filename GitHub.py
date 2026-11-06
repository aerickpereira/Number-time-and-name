user_input = input('Enter a number: ')

if user_input.isdigit():
    user_input_int = int(user_input)
    even_odd = user_input_int % 2 == 0
    even_odd_text = 'odd'

    if even_odd:
        even_odd_text = 'even'

    print(f'The number {user_input_int} is {even_odd_text}')
else:
     print('You did not enter an integer.')


user_input = input('Enter the time in whole numbers:  ')

try:
    hour = int(user_input)

    if hour >= 0 and hour <= 11:
        print('Good morning!')

    elif hour >= 12 and hour <= 17:
        print('Good afternoon!')

    elif hour >= 18 and hour >= 23:
        print('Good evening!')

    else:
        print('I do not recognize this time.')

except:
    print('Please enter whole numbers only.')


name = input('Enter your first name: ')
name_length = len(name)

if name_length > 1:
    if name_length <= 4:
        print("Your name is short")
    elif name_length >= 5 and name_length <= 6:
        print("Your name is normal")
    else:
        print("Your name is very long")
else:
    print('Please enter something.')