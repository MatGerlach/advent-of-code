import numpy as np
test_input="""F10
N3
F7
R90
F11"""

commands = {
    "N" : (np.array([1,0]),0,0),
    "S" : (np.array([-1,0]),0,0),
    "E" : (np.array([0,1]),0,0),
    "W" : (np.array([0,-1]),0,0),
    "R" : (np.array([0,0]),1,0),
    "L" : (np.array([0,0]),-1,0),
    "F" : (np.array([0,0]),0,1),
}
rotation_matrix=np.array([[0,-1],[1,0]])

def distance_1(command_input):
    position=np.array([0,0])
    direction=np.array([0,1])
    for line in command_input.splitlines():
        command = commands[line[0]]
        value = int(line[1:])
        position+=command[0]*value
        for _ in range((command[1]*value//90)%4):
            direction=np.matmul(rotation_matrix,direction)
        if command[2]!=0:
            position+=direction*value
    return abs(position[0])+abs(position[1])

def distance_2(command_input):
    position=np.array([0,0])
    waypoint=np.array([1,10])
    for line in command_input.splitlines():
        command = commands[line[0]]
        value = int(line[1:])
        waypoint+=command[0]*value
        for _ in range((command[1]*value//90)%4):
            waypoint=np.matmul(rotation_matrix,waypoint)
        if command[2]!=0:
            position+=waypoint*value
    return abs(position[0])+abs(position[1])

assert distance_1(test_input) == 25
assert distance_2(test_input) ==286

with open("input_day_12.txt") as f:
    instructions=f.read()
print(distance_1(instructions))
print(distance_2(instructions))