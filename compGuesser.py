from __future__ import annotations
from random import randint as rd

class CompGuesser(object):
    '''
    The computer genetares ramdon numbers untill it matchs to userNumber input.
    Parameters:
    :param: userNumber -> int class level
    :param: compNumber -> int method level
    :param: list_tries -> list method level
    
    $ python compGuesser.py
    >>Type a number between 0 and 999.
    >>3
    >>24 tries has been executed!
    '''
    userNumber: int
    
    def __init__(self) -> None:
        '''
        Initializer of the userInput and validator methods
        '''
        self.list_tries: list[int] = []
        CompGuesser.userInput()
        CompGuesser.validator(self)
        
    @classmethod
    def userInput(cls) -> None:
        '''
        Input to userInput parameter
        '''
        cls.userNumber = int(input("\nType a number between 0 and 999.\n"))
        
    def validator(self) -> None:
        '''
        Initializes the parameter compNumber with -1. 
        It checks if after each interation the random value generated maches to the userInput.
        If it matches break the loop.
        It append the random value generated to the list_tries. 
        It prints the follow string:
        "{len(self.list_tries)} tries has been executed!"
        '''
        self.compNum: int = -1
        while self.compNum != CompGuesser.userNumber:
            self.compNum = rd(0, 999)
            self.list_tries.append(self.compNum)
        print(f"{len(self.list_tries)} tries has been executed!")
        
gm1 = CompGuesser()
