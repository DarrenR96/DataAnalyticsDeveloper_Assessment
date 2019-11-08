# Darren R.
# 6th/Nov/2019


def triangleAdjacentMaxDynamic(FileLocation):
    # Function for Part A of Excercise 1

    # Input =   Location of file containing multiple rows of numbers,
    #           separated by white spaces, with the amount of numbers in the first line
    #           being 1, and every subsequent line increasing by 1
    #
    # Output =  The pathway satisifying the maximum binary split based on the index of
    #           the preceeding line (after the first line)

    lines = []

    # Read in Text File
    with open(FileLocation, "r") as fp:
        # Remove all formatting characters
        lines = [line.strip() for line in fp.readlines()]

    # Remove whitespaces
    lines = [line.split() for line in lines]
    # Convert from string to numerical
    lines = [list(map(int, line)) for line in lines]

    # Find maximum pathway using Dynamic Prog. approach
    while len(lines) > 1:
        for i in range(0, len(lines[-2])):
            lines[-2][i] = max(lines[-2][i]+lines[-1][i],
                               lines[-2][i]+lines[-1][i+1])
        del lines[-1]
    maxSum = lines[0][0]
    return(maxSum)
