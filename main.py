import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, 'Up')

game_is_on = True
game_round = 1
car_manager = CarManager()
while game_is_on:
    game_round += 1
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    #Detect successful crossing
    if player.crossed():
        car_manager.faster()
        scoreboard.level_up()
        player.reset_player()



    #Detect hit by car
    for car in car_manager.cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()

