import random

#agregado desde el conocimiento de tuplas
options = ('piedra', 'papel', 'tijera')

user_option = input('piedra, papel o tijera =>')
user_option = user_option.lower()

if not user_option in options:
  print(f'"{user_option.upper()}" no es una opcion valida')

computer_option = random.choice(options)

computer_option = 'piedra'

print('User option =>', user_option)
print('Computer option =>', computer_option)

if user_option == computer_option:
  print('Empate!')
elif user_option == 'piedra':
  if computer_option == 'tijera':
    print('piedra gana a tijera')
    print('user gano')
  else:
    print('papel gana a piedra')
    print('computer gano')
elif user_option == 'papel':
  if computer_option == 'piedra':
      print('papel gana a piedra')
      print('user gano')
  else:
    print('tijera gana a papel')
    print('computer gano')
elif user_option == 'tijera':
  if computer_option == 'papel':
    print('tijera gana a papel')
    print('user gana')
  else:
    print('piedra gana a tijera')
    print('computer gana')