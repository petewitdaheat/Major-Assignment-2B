def sort(names, scores, first: int):
    """Sorts a list of scores from smallest to largest and sorts the
    list of names according to the order defined by the sorted scores

    Args:
        names: list of names
        scores: list of scores
        first (int): the list index at which the sort will begin
    """     
    # initialize loop counter variable named i

    i = len(scores) - first - 1

    # initialize loop counter variable named j to 0
    j = 0

    # initialize variable named big that will be used to store
    # index of the biggest value
    big = 0


    # initialize variable named temp that will be used
    # to swap list values
    temp = 0
    temp_name = ''

    # loop through list as many times as specified by
    # len(scores) and first
    # this loop represents the blue arrow
    while (i > 0):
        # set big equal to first
        big = first

        # set j equal to first + 1
        j = first + 1

        # loop through the list starting with the element at 
        # first + 1 and continue until reach first + i
        # this loop represents the yellow arrow
        while (j <= first + i):
            # if the value in scores[big] is less than 
            # scores[j]
            if(scores[big] < scores[j]):
                # set big equal to j
                big = j
            # increment j by 1
            j += 1
        
        # swap the scores in first + i with the scores in big
        # set temp to value in scores[first + i]
        temp = scores[first + i]
        temp_name = names[first + i]

        # set scores[first + i] to the value in scores[big]
        scores[first + i] = scores[big]
        names[first + i] = names[big]


        # set scores[big] to the value in temp
        scores[big] = temp
        names[big] = temp_name


        # decrement i by 1
        i -= 1

