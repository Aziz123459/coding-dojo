class Ninja:
    def __init__(self,first_name,last_name,pet,treats,pet_food):
        self.first_name=first_name
        self.last_name=last_name
        self.pet=pet
        self.treats=treats
        self.pet_food=pet_food
    def walk(self):
        self.pet.play()
        return self
    def feed(self):
        if len(self.pet_food) > 0:
            food = self.pet_food.pop()
            print(f"{self.first_name} {self.last_name} Feeding {self.pet.name} {food}!")
            self.pet.eat()
        else:
            print("no more food")
        return self
    def bathe(self):
        self.pet.noise() 
class Pets:
    def __init__(self,name,type,tricks,noisee):
        self.name=name
        self.type=type
        self.tricks=tricks
        self.health=100
        self.energy=100
        self.noisee=noisee
    def sleep(self):
            self.energy=self.energy+5
            return self
    def eat(self):
        self.energy = self.energy+5
        self.health = self.health+10
        print(f"energy increase : {self.energy} health increase : {self.health}")
        return self
    def play(self):
        self.health=self.health+5
        print(f"after the walk health increase :{self.health}")
        return self
    def noise(self):
        print(self.noisee)

        


treats = ['salami','turky']
pet_food = ['dog food','meat','chicken']

bob = Pets("bob","dog",["sit","stand up"],"aaaaaaaaaaa")

aziz= Ninja("aziz","tounsi", bob,treats,pet_food)

aziz.feed()
aziz.feed()
aziz.feed()
aziz.feed()
aziz.walk()
aziz.bathe()





