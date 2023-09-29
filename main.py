from selectionsort import *

def main():
    # set up the local variables to store list and first
    names = ['Emma', 'Brian', 'Evelyn', 'Frank', 'Alex', 'Felecia', 'Carl']
    scores = [99, 85, 64, 78, 95, 50, 88]
    first = 0
    # display original unsorted list input by user
    print("ORIGINAL LISTS")
    print("Names      Scores")
    for i in range(7):
        print(names[i],'     ', scores[i],'\n', end="")
    
    # call sort method
    sort(names, scores, first)
    # sort(scores, names, first)

    print()

    # display sorted list
    print("ORIGINAL LISTS")
    print("Names      Scores")
    for i in range(7):
        print(names[i],'    ', scores[i],'\n', end="")





if __name__ == "__main__":
    main()