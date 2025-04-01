#Check if the robot returns to origin if its starts from north(0,1) and either turns Left or Right based on the instructions provided

def RobotBounded(self,instructions :str)->bool:
    x,y = 0,0
    dx,dy = 0,1
    for moves in instructions:
        if moves == 'G':
            x+=dx
            y+=dy
        elif moves =='L':
            dx,dy = -dy,dx
        elif moves == 'R':
            dx,dy = dy,-dx
        
    return (x == 0  and y ==0) or (dx,dy) != (0,1)