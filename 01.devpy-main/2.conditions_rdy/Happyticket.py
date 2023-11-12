"""" 6-sign ticket(xyzabc)-all, need to show all happy(x+y+z=a+b+c) """
# To run selected - ALT+E or ALT+SHIFT+E

number = 0
while number <= 99999:
    if number % 10 + number % 100 // 10 + number // 100 % 10 == number // 1000 % 10 + number // 1000 // 100 + number // 10000 % 10:
        print('Happy Ticket', number)
#    else:
#       print('Unhappy Ticket', number)
    number += 1
