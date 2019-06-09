from django.shortcuts import render
from rest_framework.views import APIView
from util.ResponseBuilder import Response_Builder
import random
import pytz
import json


Resp = Response_Builder()

# Create your views here.

# Definition of "element" class to create the different options from game
class Element:
    name = ''
    win = []
    lost = []

    def name(self):
        return '{}'.format(self.name)


# Definition rock class
class Rock(Element):
    def __init__(self):
        self.name = 'rock'
        self.win = [Scissors, Lizard]
        self.lost = [Paper, Spock]


# Definition paper class
class Paper(Element):
    def __init__(self):
        self.name = 'paper'
        self.win = [Rock, Spock]
        self.lost = [Lizard, Scissors]


# Definition scissors class
class Scissors(Element):
    def __init__(self):
        self.name = 'scissors'
        self.win = [Paper, Lizard]
        self.lost = [Rock, Spock]


# Definition lizard class
class Lizard(Element):
    def __init__(self):
        self.name = 'lizard'
        self.win = [Spock, Paper]
        self.lost = [Rock, Scissors]


# Definition spock class
class Spock(Element):
    def __init__(self):
        self.name = 'spock'
        self.win = [Scissors, Rock]
        self.lost = [Lizard, Paper]


# Function to choose the option random for the computer
def random_computer():
    optionsComputer = ['rock', 'paper', 'scissors', 'lizard', 'spock']
    turnComputer = random.choice(optionsComputer)

    return turnComputer


# Function to compare the options chose between the player and computer
def compare(optionComputer, optionPlayer):

    # Creation of instances for the game's options
    rock = Rock()
    paper = Paper()
    scissors = Scissors()
    lizard = Lizard()
    spock = Spock()

    # Creation of winner
    winner = ''

    # Creation of player and computer
    player = None
    computer = None

    # Options list
    options_list = [rock, paper, scissors, lizard, spock]

    # Assign options for the computer and the player
    for option in options_list:
        if optionPlayer == option.name:
            player = option
        if optionComputer == option.name:
            computer = option

    # Verify tied
    if player == computer:
        winner = 'Tied'
    else:
        for index, c in enumerate(player.win):
            if type(computer) == c:
                winner = 'Player'
        for index, c in enumerate(player.lost):
            if type(computer) == c:
                winner = 'Computer'

    return winner


# Function to create the json type answer
def create_json(optionComputer, answer):
    result = {
        "winner": '',
        "tied": False,
        "iconComputer": ''
    }

    if(answer == 'Tied'):
            result['tied'] = True
    else:
        result['winner'] = answer

    result['iconComputer'] = optionComputer

    return result

# Main Class that receives by method post the player's choice
class play_turn(APIView):

    def dispatch(self, request, *args, **kwargs):
        return super(play_turn, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        try:
            #Assign the player's option
            optionPlayer = request.data['player']

            #Generate the computer's option
            randomComputer = random_computer()

            # Get result
            answer = compare(randomComputer, optionPlayer)

            # Create JSON
            jsonAnswer = create_json(randomComputer, answer)

            return Resp.send_response(_status=200, _msg='OK', _data=jsonAnswer)
        except Exception as e:
            print(e)
            return Resp.send_response(_status=503, _msg='Error')
