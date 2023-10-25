#create a class resturant,that accepts
#itemname and quantity as input
#inside your class you have the item
#and its cost(unit price) as a dictionary
#create a function calculate cost
#that prints the itemname,qty,total cost

class resturant:

    def __init__(self,itemname,qty):
        self.itemname=(itemname)
        self.qty=(qty)
        self.menuitems={
            "Rice":30,
            "Chicken":100,
            "Dal":40,
            "Chapathi":15
        }   
    def totalcost(self):
        print("Total cost of the order")
        print("Item\t",self.itemname)
        print("Quantity\t",self.qty)
        total=self.qty*self.menuitems[self.itemname]
        print("total\t",total)

itemname=input("Enter the item\t")
qty=int(input("enter the quantity\t"))
order=resturant(itemname,qty)
order.totalcost()

    
