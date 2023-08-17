from pyfiglet import Figlet

def show_menu():
    print("1- Add product")
    print("2- Edit product")
    print("3- Delete product")
    print("4- Search")
    print("5- Show list")
    print("6- Buy")
    print("7- exit")



f = Figlet(font= "standard")
print(f.renderText("'\Farhan Market/'"))

show_menu()
# !!! ATTENTION !!!
#    CHANGE THE PATH AFTER MOVING THE DATABASE ACCURATLY

Rotation = True

while Rotation :
    myfile = open("D:/famely/farhan/programs/Class Royan/database.txt" , "r")
    data = myfile.read()
    
    PRODUCT = []
    product_list = data.split("\n")
    for i in range (len(product_list)):
        product_info  =product_list[i].split(",")
        mydict = {}
        mydict["id"] = product_info[0]
        mydict["name"] = product_info[1]
        mydict["price"] = product_info[2]
        mydict["count"] = product_info[3]
        PRODUCT.append(mydict)
    
    myfile.close()
#----------------------------------Add---------------------------------------------
    choice = int(input("please chosse a number:"))
    if choice == 1:
        id=input("Please write your product id : ")
        name = input("Please enter your product name : ")
        price = input("Please enter your product price : ")
        count = input("Please enter your product quantity : ")
        myfile = open("D:/famely/farhan/programs/Class Royan/database.txt" , "a")
        myfile.write("\n"+id+","+name+","+price+","+count)
        myfile.close()
        print("Product added!")
    #----------------------------------Edit------------------------------------------
    elif choice == 2:
        print(PRODUCT)
        for x in range(len(PRODUCT)):
            print(PRODUCT[x]["name"])

        name = input("Enter the preffered product name : ")

        for i in range(len(PRODUCT)-1):
            print(i)
            if name == PRODUCT[i]["name"]:
                PRODUCT.pop(i)
        id = input("Enter your product id : ")
        name = input("Enter your product name : ")
        price = input("Enter your product price : ")
        count = input("Enter your product quantity : ")
        mydict = {"id":id,"name":name,"price":price,"count":count}
        PRODUCT.append(mydict)
        data = ""#madebyfarhan
        for y in range(len(PRODUCT)):
            data += PRODUCT[y]["id"] + "," + PRODUCT[y]["name"] + "," + PRODUCT[y]["price"] + "," + PRODUCT[y]["count"] 
            if y != len(PRODUCT)-1:
                #made by farhan
                data += "\n"
        myfile = open("D:/famely/farhan/programs/Class Royan/database.txt" , "w")
        myfile.write(data)
        myfile.close()
        print("Product edited!")
    #------------------------------------Deletion---------------------------------------
    elif choice == 3:
        for x in range(len(PRODUCT)):
            print(PRODUCT[x]["name"])

        name = input("Enter the preffered product name : ")

        for i in range(len(PRODUCT)):
            if name == PRODUCT[i]["name"]:
                #made by farhan
                PRODUCT.pop(i)
        data = ""
        for y in range(len(PRODUCT)):
            data += PRODUCT[y]["id"] + "," + PRODUCT[y]["name"] + "," + PRODUCT[y]["price"] + "," + PRODUCT[y]["count"] + "\n"
        myfile = open("D:/famely/farhan/programs/Class Royan/database.txt" , "w")
        myfile.write(data)
        myfile.close()
        print("Product deleted!")
    #-----------------------------------Search-------------------------------------------
    elif choice == 4:
        name = input("Please enter your product name : ")
        for i in range(len(PRODUCT)):
            if PRODUCT[i]["name"] == name:
                print("Here is your product details :")
                print("Id :",PRODUCT[i]["id"])
                print("Name :",PRODUCT[i]["name"])
                print("Price :",PRODUCT[i]["price"])
                print("Quantity :",PRODUCT[i]["count"])
            else :#made by farhan
                print("Product not found !")
    #----------------------------------List------------------------------------------------
    elif choice == 5:
        print("Here is the list of all the products :")
        print("id/name/price/quantity")
        for i in range(len(PRODUCT)):
            print(PRODUCT[i]["id"],"/",PRODUCT[i]["name"],"/",PRODUCT[i]["price"],"/",PRODUCT[i]["count"])
    #----------------------------------Buy--------------------------------------------------
    elif choice == 6:
       print("List of products in {id/name} order :")
#made by farhan
       for i in range(len(PRODUCT)):#made by farhan
            print(PRODUCT[i]["id"],"/",PRODUCT[i]["name"]) 

       id = input("Enter the id of the bought product : ")
       quan = input("Enter the quantity of the bought product : ")
       for i in range(len(PRODUCT)):
           if id == PRODUCT[i]["id"]:
               count = int(PRODUCT[i]["count"])
               count -=quan
               PRODUCT[i]["count"]=str(count)
       print("Product bought!")
    #-------------------------------Exit-----------------------------------------------
    elif choice ==7:
        Rotation = False
        print("Quitting the program...")



































































        #made by farhan