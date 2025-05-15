import random

print('===================')
print('Rock Paper Scissors')
print('===================')

print('1) ✊')
print('2) ✋')
print('3) ✌️')
print('4) 🦎')
print('5) 🖖')
player = int(input('Choose a number: '))
computer = random.randint(1, 5)
# computer = 4

if player == 1:
    player = '✊'
elif player == 2:
    player = '✋'
elif player == 3:
    player = '✌️'
elif player == 4:
    player = '🦎'
elif player == 5:
    player ='🖖'
else:
    print('Invalid.')

if computer == 1:
    computer = '✊'
elif computer == 2:
    computer = '✋'
elif computer == 3:
    computer = '✌️'
elif computer == 4:
    computer = '🦎'
elif computer == 5:
    computer ='🖖'

print(f'You chose: {player}')
print(f'CPU chose: {computer}')

if player == '✊' and computer == '✌️' or player == '✋' and computer == '✊' or player == '✌️' and computer == '✋' \
or player == '✊' and computer == '🦎' or player == '🦎' and computer == '🖖' or player == '🖖' and computer == '✌️' \
or player == '✌️' and computer == '🦎' or player == '🦎' and computer == '✋' or player == '✋' and computer == '🖖' \
or player == '🖖' and computer == '✊':
    print('The player won!')
elif computer == '✊' and player == '✌️' or computer == '✋' and player == '✊' or computer == '✌️' and player == '✋' \
or computer == '✊' and player == '🦎' or computer == '🦎' and player == '🖖' or computer == '🖖' and player == '✌️' \
or computer == '✌️' and player == '🦎' or computer == '🦎' and player == '✋' or computer == '✋' and player == '🖖' \
or computer == '🖖' and player == '✊':
    print('The CPU won!')
elif player == '✊' and computer == '✊' or player == '✋' and computer == '✋'or player == '✌️' and computer == '✌️' \
or player == '🦎' and computer == '🦎' or player == '🖖' and computer == '🖖':
    print('It\'s a tie!')

# Hey Mentor, thanks for your time and your feedback. :) 
# Kind regards,
# Staudi