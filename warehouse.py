"""
    Program: Warehouse management system
    Functionality:
       - Repeated menu
       - Register items to the catalog
            id(auto generated)
            title
            category
            price
            stock
        -Display Catalog
        -Display items with no stock (out of stock)
        -Saving / retrieving data to/ from file
        -Update the stock of an item
            -Show the list items
            -Ask the user to choose an id
            -Ask the user for the new stock value
            -Find the item with selected id
            -Update the stock
            -Save changes
"""
from menu import menu, clear, header
from item import Item
import pickle

#global vars
catalog=[]
last_id=0
data_file= 'warehouse.data'

def save_catalog():
    global data_file
    writer = open(data_file, "wb") #create file(overwrite), open it to write binary
    pickle.dump(catalog, writer)
    writer.close()
    print("**Data Saved!!")
    # print(date_file)

def read_catalog():
    try:
        global data_file
        global last_id
        reader = open(data_file,"rb")
        temp_list= pickle.load(reader)

    for item in temp_list:
        catalog.append(item)

    last = catalog[-1]
    last_id= last.id

    how_many = len(catalog)
    print("**Loaded" + str(how_many)+ "items")
except:
    print("**No file found, db is empty")

#functions
def register_item():
    global last_id
    header(" Register new Item")

    title= input("New item title:    ")
    category = input ("New item category:   ")
    price= float(input ("New item price:   "))
    stock= int(input("New Item stock:    "))

    new_item = Item() #Create instances of a class (objects)
    last_id +=1
    new_item.id=last_id
    new_item.title=title
    new_item.category=category
    new_item.price=price
    new_item.stock=stock

    catalog.append(new_item)
    print("Item created!")

def display_catalog():
    """ clear()
    print("-" *30)
    print("Current Catalog")
    print("-" *30) """
  """   print("there are: "+ str(size) + "items") """
    size= len(catalog)
    header("Current Catalog ("+ str(size) + "items)")

    #print("-" * 70)
     print("|" +'ID'.rjust(2)
        + "|" + 'Title'.ljust(24)
        + "|" + 'Category'.ljust(15)
        + "|" + 'Price'.rjust(10)
        + "|" + 'Stock'.rjust(5)+ "|")
    print("-" * 70)

for item in catalog:
    print("|" + str(item.id).rjust(2)
     + "|" + item.title.ljust(24)
     + "|" + item.category.ljust(15)
     + "|" + str(item.price).rjust(10)
     + "|" + str(item.stock.rjust(5)+ "|")

     print("-"*70)

def display_not_stock():
    size= len(catalog)
    header("Out of stock (" + str(size) + " items)")

    #print("-" *70)
        print("|" +'ID'.rjust(2)
        + "|" + 'Title'.ljust(24)
        + "|" + 'Category'.rjust(15)
        + "|" + 'price'.rjust(10)
        + "|" + 'Stock'.rjust(5)+ "|")
    print("-" * 70)

    for item in catalog:
        if(item.stock==0):
        print("|" + str(item.id).rjust(2)
        + "|" + item.title.ljust(24)
        + "|" + item.category.ljust(15)
        + "|" + str(item.price.rjust(10)
        + "|" + str(item.stock).rjust(5)+ "|")

    print("-" * 70)

def update_stock():
    display_catalog()
    id = int(input("Please select an Id from the list: "))
    #stock = int(input("New stock value: "))
    #find the item with id = id
    found = False
    for item in catalog:
        if(item.id==id):
            found = True
            stock = int(input("New stock value"))
            item.stock = stock
            print('Stock updated!')

if(not found):
    print("Error : Selected Id does not exists, try again")

def calculate_stock_value():
    total= 0.0
    for item in catalog:
        total += (item.price * item.stock)

    print("Total Stock Value $"+ str(total))

#instructions
#start menu

#first load data
read_catalog()
input("Press enter to continue")

opc = ''
while(opc !='x'):
    clear()
    menu()
    print("/n")
    opc= input("please select an option: ..")

    if(opc=='1'):
        register_item()
        save_catalog()
    elif(opc=='2'):
        # read_catalog()
        display_catalog()
    elif(opc=='3'):
        display_no_stock()
    elif(opc=='4'):
        update_stock()
        save_catalog()

    input ("Press enter to continue...")