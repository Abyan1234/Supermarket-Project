while True:
    total=0
    customerName=input("Name:-")
    while True:
        print("Enter number of Items and qunatity")
        items=int(input("items"))
        quantity=int(input("quantity"))
        total=quantity*items
        repeat=input("Do you want to repeat this process(Y/y/N/n)")
        if repeat=='n' or repeat=='N':
            break
    print(customerName+""+"Bill generated")
    print("Total cost:-",total)
    
    new=input("Go to the next Person")
    if new=='n' or new=='N':
        break


