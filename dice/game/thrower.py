import random

# TODO: Define the Thrower class here.

class Thrower:
    """This part is for the person who rolls the die. Will have defined values.
    
    Attributes:
        Dice (list): the list with the numbers rolled, and
        num_throws (number): the number of times the thrower has rolled the dice
        points (num): points earned.
    """

    def __init__(self):
        """This is the class constructor.
        Args:
            self (Thrower): An instance of Thrower.
        """
        self.dice = []
        self.num_throws = 0
        self.points = 0 
        
    def can_throw(self):
        """This method allows whether or not the thrower can roll the die again. if it has one or five or greater than zero it is true, if it is not false. 
        Args: 
            self (Thrower): An instance of Thrower.
        
        Returns:
            boolean: It returns us if the list has a 5 or 1 or 0. if it is not false.
        """
        if 1 in self.dice or 5 in self.dice or self.num_throws == 0:
            return True
        else:
            print('Thank you. Good bye!')
            return False
        

    def get_points(self):
        """This method calculates the points of each die. If a one is rolled, it is 100 points, if it comes out 5, it is 50 points. 
        Args: 
            self (Thrower): An instance of Thrower.
        
        Returns:
            number: how many points your have.
        """
        for i in self.dice:
            if i == 1:
                self.points += 100
            elif i == 5:
                self.points += 50
            else:
                self.points += 0
        
        return self.points
    
        
    def throw_dice(self):
        """Randomly new five dice values and this is passed to a list, and the num_throws method increments. 
        Args: 
            self (Thrower): An instance of Thrower.
        """

        self.dice.clear()

        for _ in range(5):
            random_number = random.randint(1, 7)
            self.dice.append(random_number)
            self.num_throws += 1
