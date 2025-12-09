item_names = ["apple", "bread", "milk", "eggs"]
item_prices = [1.0, 2.50, 3.00, 4.50]
item_stock = [100, 20, 50, 4]

while True:
    steps= input("Enter 'view inventory' to view optons or 'purchase items' to buy items or 'restock items' to restock them or 'exit' to quit: ").lower()
    if steps=="exit":
        break
    elif steps=="purchase items":
        item = input("Enter item name: ").lower()
        quant = int(input("Enter quantity: "))
        if item in item_names:
            index = item_names.index(item)
            if item_stock[index] >= quant:
                total_price = item_prices[index] * quant
                item_stock[index] -= quant
                print("Purchased", quant, item, "for Rs.", total_price)
            else:
                print("Low Stock")
        else:
            print("Item not found in inventory.")
    elif steps=="view inventory":
        print("Available items:")
        for i in range(len(item_names)):
            print(f"{item_names[i].title()}: Price Rs.{item_prices[i]}, Stock {item_stock[i]}")
    elif steps=="restock items":
        item = input("Enter item name to restock: ").lower()
        quant = int(input("Enter quantity to add: "))
        if item in item_names:
            index = item_names.index(item)
            item_stock[index] += quant
            print("Restocked", quant, "of", item, ". New stock:", item_stock[index])
        else:
            item_names.append(item)
            price = float(input("Enter price for the new item: "))
            item_prices.append(price)
            item_stock.append(quant)
            print("Added new item", item, "with price Rs.", price, "and stock", quant)
    else:
        print("Invalid option. Please try again.")