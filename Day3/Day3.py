# Day 3: Perfectly Spherical Houses in a Vacuum

NORTH = '^'
SOUTH = 'v'
EAST = '>'
WEST = '<'

class Position2d:
    def __init__(self, x, y):
        self.xPos = x
        self.yPos = y
    
    def add_step_and_return(self, direction):
        if direction == NORTH:
            self.yPos += 1
        elif direction == SOUTH:
            self.yPos -= 1
        elif direction == EAST:
            self.xPos += 1
        elif direction == WEST:
            self.xPos -= 1
        
        return Position2d(self.xPos, self.yPos)    

class SantaTracker:
    def __init__(self):
        self.num_visited_houses = 1
        self.visited_positions = []
        self.current_position = Position2d(0, 0)
        self.visited_positions.append(Position2d(0, 0))

    def go_and_left_presents(self, santaAtlas):
        santaMap = open(santaAtlas).read()
        
        for direction in santaMap:
            self.go_to_next_house(direction)

    def go_to_next_house(self, direction):      
        newPosition = self.current_position.add_step_and_return(direction)
        if not any((newPosition.xPos == item.xPos) and (newPosition.yPos == item.yPos) for item in self.visited_positions):
            self.visited_positions.append(newPosition)
            self.num_visited_houses += 1

class SantaWithRoboTracker(SantaTracker):
    def __init__(self):
        super(SantaWithRoboTracker, self).__init__()
        self.current_robo_position = Position2d(0, 0)

    def go_and_left_presents(self, santaAtlas):
        santaMap = open(santaAtlas).read()
        
        directionPair = []
        for direction in santaMap:
            directionPair.append(direction)
            if len(directionPair) == 2:
                self.go_to_next_house(directionPair[0], directionPair[1])
                directionPair.clear()
            
    def go_to_next_house(self, firstDirection, secondDirection):
        newPositionSanta = self.current_position.add_step_and_return(firstDirection)
        if not any((newPositionSanta.xPos == item.xPos) and (newPositionSanta.yPos == item.yPos) for item in self.visited_positions):
            self.visited_positions.append(newPositionSanta)
            self.num_visited_houses += 1
        newPositionRobo = self.current_robo_position.add_step_and_return(secondDirection)
        if not any((newPositionRobo.xPos == item.xPos) and (newPositionRobo.yPos == item.yPos) for item in self.visited_positions):
            self.visited_positions.append(newPositionRobo)
            self.num_visited_houses += 1


santa_tracker = SantaTracker()
santa_tracker.go_and_left_presents("input.txt")
print(santa_tracker.num_visited_houses)

santa_tracker_with_robo = SantaWithRoboTracker()
santa_tracker_with_robo.go_and_left_presents("input.txt")
print(santa_tracker_with_robo.num_visited_houses)