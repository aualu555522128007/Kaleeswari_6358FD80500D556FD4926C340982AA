# Define the Player class
class Player:
    # Initialize the attributes
    def __init__(self, name):
        self.name = name

    # Define a method to play cricket
    def play(self):
        # Print a generic message
        print(f"The player {self.name} is playing cricket.")

# Define the Batsman class as a subclass of Player
class Batsman(Player):
    # Override the play method
    def play(self):
        # Print a specific message
        print(f"The batsman {self.name} is batting.")

# Define the Bowler class as a subclass of Player
class Bowler(Player):
    # Override the play method
    def play(self):
        # Print a specific message
        print(f"The bowler {self.name} is bowling.")


# Create objects of both the Batsman and Bowler classes
b1 = Batsman("Virat Kohli")
b2 = Bowler("Jasprit Bumrah")

# Call the play method for each object
b1.play() # The batsman Virat Kohli is batting.
b2.play() # The bowler Jasprit Bumrah is bowling.