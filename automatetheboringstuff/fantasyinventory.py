#Excercise 1&2 Chapter 5 
import copy 

inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

#Excercise 1 Fantasy Game Inventory
def displayInventory(inventory):
    print('Inventory')
    total_items = 0
    for item,amount in inventory.items():
        total_items += amount
        print("{} {}".format(amount,item))
    print('Total number of items: {}'.format(total_items))

displayInventory(inventory) 

# Excercise 2 List to Dictionary Function for Fantasy Game Inventory
def addToInventory(inventory, loot):
    new_inventory = copy.copy(inventory)
    
    for item in loot:
        if item in new_inventory:
            new_inventory[item] += 1
        new_inventory.setdefault(item,1)
    return new_inventory

print('-' * 40 +  "Adding Loot" + '-' * 40) 
displayInventory(addToInventory(inventory, dragonLoot))
