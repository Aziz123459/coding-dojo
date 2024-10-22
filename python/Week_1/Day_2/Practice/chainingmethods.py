class User:
    def __init__(self, first_name,last_name,email,age):
        self.first_name=first_name
        self.last_name=last_name
        self.email=email
        self.age=age
        self.is_rewards_member=False
        self.gold_card_points = 0


    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        print(self.is_rewards_member)
        print(self.gold_card_points)
        return self


    def enroll(self):
        self.is_rewards_member=True
        self.gold_card_points = 200
        return self
    



    def spend_points(self, amount):
        self.gold_card_points=self.gold_card_points -(amount)
        return self














alex=User("alex","miller","alexmiller@gmail.com",15)
monji=User("monji","west","monjiwest@gmail.com",45)
alex.display_info().enroll().spend_points(50).display_info()
monji.enroll().spend_points(80).display_info()













