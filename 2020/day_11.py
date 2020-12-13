from functools import reduce
from enum import Enum
from copy import deepcopy
import sys
test_seat_layout = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"""

class SeatLayout:

    def __init__(self,seat_layout):
        self.rows = len(seat_layout.splitlines())
        self.cols = len(seat_layout.splitlines()[0])
        self.state= list("".join(seat_layout.splitlines())) 
        self.history = [self.state]

    def _get_neighbours(self, row, col):
        left = max(0,col-1)
        right = min(col+1,self.cols-1)
        top = max(0,row-1)
        bot = min(row+1,self.rows-1)
        neighbours = []
        for row in range(top,bot+1):
            neighbours += self._get_row(row)[left:right+1]
        return neighbours

    def _get_neighbours_in_sight(self, row, col):
        neighbours=0
        # Left
        x = col-1
        while x >= 0 and self.get(row,x) == ".":
            x-=1 
        if x >= 0 and self.get(row,x) == "#": 
            neighbours +=1
        # Right
        x = col+1
        while x < self.cols and self.get(row,x) == ".":
            x+=1
        if x < self.cols and self.get(row,x) == "#" :
            neighbours +=1
        # Top
        x = row-1
        while x >= 0 and self.get(x,col) == ".":
            x-=1 
        if x >= 0 and self.get(x,col) == "#": 
            neighbours +=1
        # Bottom
        x = row+1
        while x < self.rows and self.get(x,col) == ".":
            x+=1
        if x < self.rows and self.get(x,col) == "#":
            neighbours +=1
        # Top,Left
        x = col-1
        y = row-1
        while  x >= 0 and y >= 0 and self.get(y,x) == ".":
            x-=1 
            y-=1
        if x >= 0 and y >= 0 and self.get(y,x) == "#": 
            neighbours +=1
        # Top,Right
        x = col+1
        y = row-1
        while x < self.cols and y >= 0 and self.get(y,x) == ".":
            x+=1 
            y-=1
        if x < self.cols and y >= 0 and self.get(y,x) == "#": 
            neighbours +=1
        # Bot,Left
        x = col-1
        y = row+1
        while x >= 0 and y < self.rows and self.get(y,x) == ".":
            x-=1 
            y+=1
        if x >= 0 and y < self.rows and self.get(y,x) == "#": 
            neighbours +=1
        # Bot,Right
        x = col+1
        y = row+1
        while x < self.cols and y < self.rows and self.get(y,x) == ".":
            x+=1
            y+=1
        if x < self.cols and y < self.rows and self.get(y,x) == "#": 
            neighbours +=1
        return neighbours

    def _get_index(self, row, col):
        assert row < self.rows
        assert col < self.cols
        return row*self.cols+col

    def _get_row(self, row):
        return self.state[self._get_index(row,0): self._get_index(row,self.cols-1)+1]

    def __str__(self):
        lines=[]
        for row in range(self.rows):
            lines.append("".join(self._get_row(row)))
        return "\n".join(lines)
    
    def get(self, row, col):
        return self.state[self._get_index(row,col)]
    
    def turn_1(self):
        changed=False
        new_state = deepcopy(self.state)
        for row in range(self.rows):
            for col in range(self.cols):
                if self.get(row,col) == "L" and self._get_neighbours(row,col).count("#") == 0:
                    new_state[self._get_index(row,col)]="#"
                    changed=True
                elif self.get(row,col) == "#" and self._get_neighbours(row,col).count("#") > 4:
                    new_state[self._get_index(row,col)]="L"
                    changed=True
        if changed:
            self.state=new_state
            self.history.append(new_state)
        return changed

    def turn_2(self):
        changed=False
        new_state = deepcopy(self.state)
        for row in range(self.rows):
            for col in range(self.cols):
                if self.get(row,col) == "L" and self._get_neighbours_in_sight(row,col) == 0:
                    new_state[self._get_index(row,col)]="#"
                    changed=True
                elif self.get(row,col) == "#" and self._get_neighbours_in_sight(row,col) >= 5:
                    new_state[self._get_index(row,col)]="L"
                    changed=True
        if changed:
            self.state=new_state
            self.history.append(new_state)
        return changed

    def stabilize_1(self):
        while self.turn_1():
            continue
    
    def stabilize_2(self):
        while self.turn_2():
            print(sl)
            sys.stdout.flush()


    def get_occupied_seats(self):
        return self.state.count("#")
sl = SeatLayout(test_seat_layout)
sl.stabilize_1()
assert sl.get_occupied_seats() == 37
sl = SeatLayout(test_seat_layout)
sl.stabilize_2()
assert sl.get_occupied_seats() == 26

with open("input_day_11.txt") as f:
    content=f.read()

sl = SeatLayout(content)
sl.stabilize_2()
print(sl)
print(sl.get_occupied_seats())
