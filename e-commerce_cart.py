#function to calculate the total price by including discount
def total(my_dict):
    if not my_dict:
        return 0
    elif len(my_dict)<=5:
        total_price=sum(my_dict.values())
        return total_price
        
    else:
         total_price=sum(my_dict.values())
         discount=(10/100)*total_price
         final_price=total_price-discount
         return final_price
#input            
n=int(input())
my_dict={}
for _ in range(n):
    key=input()
    value=int(input())
    my_dict[key]=value
print("Total Price:",total(my_dict))