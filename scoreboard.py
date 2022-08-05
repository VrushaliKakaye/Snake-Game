from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()  

        self.score =0  
        self.goto(0,280)
        self.penup()
        self.hideturtle()
        self.color("white")
        with open("data.txt") as data:
            self.highscore = int(data.read()) 
        self.update_score()
        

    
    def update_score(self):
        self.clear()
        self.write(f"Score : {self.score} High Score : {self.highscore}" ,align="center")

            


    def increase_score(self):
        
        self.score += 1 
        self.clear() 
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over",align="center")

    def reset(self):
        if self.score > self.highscore:
            self.highscore =self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.highscore}")

        self.score = 0
        self.update_score()





