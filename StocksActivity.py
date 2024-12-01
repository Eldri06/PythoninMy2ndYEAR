
itemnum = int(input("Enter number of items: "))
itemname = []
itemStockLv1 = []
itemLowStockThreshold = []

inventory = []
for i in range(itemnum):
    print("\nEnter detail for the item: ")
    input1 = (input("Name: "))
    input2 = (input("Stock Level: "))
    input3 = (input("Low Stock Threshold: "))
    itemname.append(input1)
    itemStockLv1.append(input2)
    itemLowStockThreshold.append(input3)
    
print("\n Inventory Status")
for i in range(len(itemnum)):
    status = ''
    if itemStockLv1[i] == 0:
        status = "Out of Stock"
    elif itemStockLv1[i] <=10:
        status = "Low Stock"
    else:
        status = "No Stock"
    print(f"{itemname[i]}:{status}({itemStockLv1[i]} units)")
    
print("\nInventory Summary")
for i in range(len(itemname)):
    outofStock = 0
    lowStock = 0
    inStock = 0
    status = ''
    
    if itemStockLv1[i] == 0:
        outofStock += 1
        status = "Out of Stock"
        print(f"{status}:{outofStock}")
    elif itemStockLv1[i] <= 10:
        lowStock += 1
        status = "Low Stock"
        print(f"{status}:{lowStock}")
    else:
        inStock += 1
        status = "In Stock"
        print(f"{status}:{inStock}")
        
    
    
    

        

         



