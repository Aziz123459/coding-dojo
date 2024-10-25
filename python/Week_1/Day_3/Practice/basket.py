class Player:
    
    def __init__(self, players_info):
        self.name = players_info['name']
        self.age = players_info['age']
        self.position = players_info['position']
        self.team = players_info['team']
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Position: {self.position}, Team: {self.team}")
        return self









kevin = {
    "name": "Kevin Durant", 
    "age":34, 
    "position": "small forward", 
    "team": "Brooklyn Nets"
}
jason = {
    "name": "Jason Tatum", 
    "age":24, 
    "position": "small forward", 
    "team": "Boston Celtics"
}
kyrie = {
    "name": "Kyrie Irving", 
    "age":32,
    "position": "Point Guard", 
    "team": "Brooklyn Nets"
}
players = [
    {
        "name": "Kevin Durant", 
        "age":34, 
        "position": "small forward", 
        "team": "Brooklyn Nets"
    },
    {
        "name": "Jason Tatum", 
        "age":24, 
        "position": "small forward", 
        "team": "Boston Celtics"
    },
    {
        "name": "Kyrie Irving", 
        "age":32,
        "position": "Point Guard", 
        "team": "Brooklyn Nets"
    },
    {
        "name": "Damian Lillard", 
        "age":33,
        "position": "Point Guard", 
        "team": "Portland Trailblazers"
    },
    {
        "name": "Joel Embiid", 
        "age":32,
        "position": "Power Foward", 
        "team": "Philidelphia 76ers"
    },
    {
        "name": "DeMar DeRozan",
        "age": 32,
        "position": "Shooting Guard",
        "team": "Chicago Bulls"
    }
]
#3 instances of the Player class using the given dictionaries
player_kevin = Player(kevin)
player_jason = Player(jason)
player_kyrie = Player(kyrie)



new_team = []
for i in players: 
    player_inf = Player(i)
    new_team.append(player_inf.display_info())
    print("*"*100)
