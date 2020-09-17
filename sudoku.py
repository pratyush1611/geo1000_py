# GEO1000 - Assignment 2
# Authors: Pratyush Kumar
# Studentnumbers: 5359252

#%%
def parse(sudoku):
    if int(sudoku):
        st = int(sudoku`)
        if len(st)<16:
            #not enough numbers
            print("Sudoku invalid not all numbers present")
            break
        elif sum([int(_) for _ in list(str(st))]) != 40:
            #total sum not 40 for the 2*2 sudoku grid
            print("Sudoku invalid , total sum isnt 40")  
        else:
            # parse sudoku because its fine
            print('This sudoku is Valid so far , now checking for the integrity')
            
            is_valid(st)
    else:
        print("Sudoku invalid")
        
    print('outside the try except' , int(sudoku))
    


def is_valid(stucture):
    
    


def main():
    sud = input("Please enter the sudoku sequence for validation or enter q to quit")
    if sud.lower()!='q':
        is_valid(sud)

if __name__ == "__main__":
    main()
