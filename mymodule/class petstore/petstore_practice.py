class petstore:
    def __init__(self):
        self.pets={
            "dogs":[],
            "cats":[],
            "rabbits":[],
            "parrots":[]
        }

    def store_new_pet(self,name,age,price,species):
        pet={
            "name":name,
            "age":age,
            "price":price
            }
        self.pets[species].append(pet)

    def search_pet(self,search_name,search_species):
        for species in self.pets:
            if species==search_species:
                for name in self.pets[species]:
                    if self.pets[species][name]==name:
                        print("YES,IT IS AVAILABLE")
                    else:
                        print("Not available")
            else:
                pass


    
        

pet_store=petstore()
pet_store.store_new_pet("Tommy",0.5,16000,"dogs")
pet_store.store_new_pet("Tuffy",0.7,20000,"dogs")
pet_store.store_new_pet("Adam",0.2,15000,"cats")
pet_store.store_new_pet("Stuart",0.9,15000,"cats")
pet_store.store_new_pet("Mitthu",1.0,600,"parrots")
pet_store.store_new_pet("Snoey",0.6,800,"rabbits")
pet_store.search_pet("Tommy","dogs")