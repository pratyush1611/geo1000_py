# GEO1000 - Assignment 2
# Authors: Pratyush Kumar & Michiel de Jong
# Studentnumbers: 5359252 & 4376978

def parse(sudoku):
    """takes the sudoku sequence and returns a sturucture of 12 tuples for checking
    does some preliminary checks as well
    calls the validation function within itself if all preliminary checks are fine

    Args:
        sudoku (str): string of sequence of 2*2 sudoku to be checked
    """

    try:  # checks if the string sequence is only numbers
        int(sudoku.strip())
    except: #return None if not int
        #if not all characters are int in the sequence
        print("Input not understood :(")
        return( None)
    
    st = (sudoku)
    
    if len(st)<16: # checks if all numbers of sudoku are present
        #not enough numbers
        print("Input not understood :( \nSudoku invalid; not all numbers present")
        return None

    elif sum([int(_) for _ in list(str(st))]) != 40: #checks if sum of all numbers input for validation equals 40
        print("Input not understood :( \nSudoku invalid , total sum is not 40")  #total sum not 40 for the 2*2 sudoku grid
        return None
    else: # parse sudoku because its fine

        sudoku_raw = [int(num) for num in sudoku]
        places = [] # list of tuples, structure to call validity check
        for i in range(4):
            rows = tuple(sudoku_raw[i*4:i*4+4])
            cols = tuple(sudoku_raw[i::4])
            block_left = sudoku_raw[i*4:i*4+2]
            block_right = sudoku_raw[i*4+2:i*4+4]
            blocks = tuple(block_left + block_right)
            places.extend((rows, cols, blocks))
        return( places )
        

def is_valid(stucture):
    """takes a structure from parse function, runs validity check on the sequence

    Args:
        structure (list of tuples): tuples containing info on rows cols and blocks of the sudoku

    Returns:
        bool : true if sudoku valied else false
    """
    num_correct = 0
    for tup in stucture:
        if sorted(tup) == [1, 2, 3, 4]:
            num_correct += 1
            if num_correct == 12:
                print("This sudoku is *VALID*")
                return True
        else:
            print("This sudoku is *INVALID*")
            return False 

def main():
    """asks user for input and validates sudoku or exits
    """
    sud = input("Please enter the sudoku sequence for validation or enter q to quit\n")
    if sud.lower() != 'q': # if user inputs q or Q for quitting     
        parsed = parse(sud)
        if parsed:
            is_valid( parseed )
        else:
            print(parsed)
    else:
        print("You chose to quit :(")


if __name__ == "__main__":
    main()