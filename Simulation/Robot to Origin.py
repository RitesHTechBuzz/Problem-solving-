#Check if the robot reaches its origin place i.e R = right , L =left , U = up , D = down

def Robot(self ,moves:str )->bool:
    return (moves.count('U') == moves.count('D')) & (moves.count('R') == moves.count('L'))