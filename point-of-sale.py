import numpy as np

choice = 1
i = 1
line = []
charge = []
receipt = []

while choice == 1:
    item_id = input('Insert item id: ')
    if item_id.isdigit() == True:
        item_id = int(item_id)
    else: 
        print('Invalid input entered.')
        while item_id.isdigit() == False:
            item_id = input('Insert correct item id: ')
            if item_id.isdigit() == True:
                item_id = int(item_id)
                break

    quantity = input('Insert quantity: ')

    if quantity.isdigit() == True:
        quantity = int(quantity)
    else: 
        print('Invalid input entered.')
        while quantity.isdigit() == False:
            quantity = input('Insert correct quantity id: ')
            if quantity.isdigit() == True:
                quantity = int(quantity)
                break

    price = input('Insert price: ')
    price = float(price)
    
    # Adding the price(s)
    if i == 1:
        charge.append(quantity*price) # total price
        charge.append(quantity*price)
    elif i ==2:
        charge.append(charge[0] + quantity*price)
    elif i > 2:
        charge[i-(i-1)] = charge[1] + quantity*price

    choice = input('Do you want to add another item? Press [1] if yes or [2] to print receipt: ')
    if choice.isdigit() == True:
        choice = int(choice)
    else: 
        print('Invalid choice entered.')
        while choice.isdigit() == False:
            choice = input('Insert correct item id: ')
            if choice.isdigit() == True:
                choice = int(choice)
                break

    charge_product = quantity*price
    receipt_temp = [item_id, quantity, price, charge_product]
    receipt.append(receipt_temp)

    price_product = '{:8.2f}'.format(price) 
    charge_product = '{:11.2f}'.format(charge_product)
    item_id = '{:6d}'.format(item_id)
    quantity = '{:9d}'.format(quantity)
    line.append(item_id + quantity + price_product + charge_product)
    i += 1

    if choice == 2:
        break

# receipt

print('\n'+'This purchase:')
print(' '*2+'Item','Quantity',' '*3+'Price',' '*3+'Charged')

print('-'*(37))

for n in range(1,i):    
    print(line[n-1],'\n')

print('Your total is $','{:.2f}'.format(charge[1]),'.')
print('Thank you for your business! Have a nice day.')