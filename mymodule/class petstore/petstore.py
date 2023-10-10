#create a class petstore where you have the details of pets available and
# their details.
# The class will have methods
#-store a new pet details
#- search for a pet
#-sell a pet
#-list all pets
# importing your petstore class,create a petstoremain file,where you will implement a menu driven program 
#for ADmin-who will manage the store and user who will see the pets and buy pets.


class petstore:
    def __init__(self):
        self.pet_details={
            "dabourman":[0.5,16,000],
            "husky":[0.7,32,000],
            "German Shephard":[0.3,23000]
            }
    

    def new_pet_details(self):
        while True:
            breed=input("Enter the breed of the pet or Done:  ").strip().title()
            if breed=="Done":
                break
            else:
                age=float(input("Enter the age of the pet:  "))
                price=int(input("Enter the price of the breed"))
                self.pet_details[breed]=[age,price]

    def search_pet(self):
        search_breed=input("Enter the breed you want to search for:")
        for breed in self.pet_details.keys():
            if breed==search_breed:
                print("YES,the breed is available")
            else:
                pass

    def sell_pet(self):
        for breed in self.pet_details.keys:
            price=self.pet_details[breed][1]
            print("the price of breed",breed,"is",price )

    def print_all_pets(self):
        print(self.pet_details)
pet_store=petstore()
pet_store.new_pet_details()
pet_store.search_pet()
pet_store.sell_pet()
pet_store.print_all_pets()


                
