# GEO1000 - Assignment 2
# Authors: Pratyush Kumar & Michiel de Jong  
# Studentnumbers: 5359252 & 4376978


def wiggle(start, end, moves):
    """computes how many different paths exist to go from the start to the end

    Args:
        start (int): start point
        end (int): end point
        moves (int): number of moves

    Returns:
        int: number of paths
    """
    req_moves = abs(start - end)
    if req_moves > moves:
        print('No moves possible')
        return 0
    elif req_moves == moves:
        return 1
    else:
        right = wiggle(start +1, end, moves -1)
        left = wiggle(start -1, end, moves -1) 
        paths = left + right
        return paths    


if __name__ == "__main__":
    print("running cab.py directly")
    print(wiggle(1, 4, 5))

