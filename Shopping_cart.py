Shopping_cart = ["Laptop Dell","Laptop HP","Laptop Lenovo"]
print(Shopping_cart)
print("A for add\n")
print("R for remove\n")
print("U for update\n")
UserChoice = input("Enter Action : ")
if UserChoice=="A":
    Shopping_cart.append(input())
    print(Shopping_cart)
elif UserChoice=="R":
    Shopping_cart.remove(input())
    print(Shopping_cart)
elif UserChoice=="U":
    index_no = int(input("Enter index: "))
    Shopping_cart[index_no] = input("New Item: ")
    print(Shopping_cart)
