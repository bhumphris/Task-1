from datetime import datetime
today = datetime.time()
time = datetime.now()

print "today is" , today.strftime('%A, %B %d, %Y') + "  " + time.__format__('%I:%M:%S %p')
print "========"
print "1. Returning customer"
print "2. New customer"
print "3. Guest"
option = 0

while option < 1 or option > 3:
    option = (int(raw_input("Choose a customer type, enter 1, 2, or 3: \n")))
    if option == 1:
        print "You selected Returning Customer. \n"
    elif option == 2:
        print "You selected New Customer. \n"
    elif option == 3:
        print 'You selected Guest.'
    else:
        print ValueError('Please select 1 for Returning Customer, 2 for New Customer, or 3 for Guest.')
