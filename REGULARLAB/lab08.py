class stack:
    def __init__(self):
        self.items=[]
    def push(self,item):
        self.items.append(item)
    def pop(self):
        if self.items==[]:
            return None
        else:
            return self.items.pop()
    def print(self):
        print("STACK:",self.items)
    def length(self):
        return len(self.items)
    def top_item(self):
        return self.items[-1]
    def is_empty(self):
        if len(self.items)==0:
            return False
        else:
            return True
        
push_pop=stack()
        
while True:
    print("Menu Driven Program")
    print("*"*50)
    print("*"*50)
    print("1. Push item in a list")
    print("2. Pop item in a list")
    print("3. The list is")
    print("4. Length of the list is")
    print("5. check if the list is empty")

    choice=int(input("Enter your choice"))

    if choice==1:
        item=input("enter the item")
        push_pop.push(item)
    elif choice==2:
        pop=push_pop.pop()
    elif choice==3:
        push_pop.print()
    elif choice==4:
        print(push_pop.length())
    elif choice==5:
        push_pop.is_empty()
    else:
        print("Exit")     