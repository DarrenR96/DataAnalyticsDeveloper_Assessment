# Darren R.
# 6th/Nov/2019


def triangleAdjacentMax(FileLocation):
    # Function for Part A of Excercise 1

    # Input =   Location of file containing multiple rows of numbers,
    #           separated by white spaces, with the amount of numbers in the first line
    #           being 1, and every subsequent line increasing by 1
    #
    # Output =  The pathway satisifying the maximum binary split based on the index of
    #           the preceeding line (after the first line)

    triangleMaxSum = 0
    currentIndex = 0

    with open(FileLocation) as fp:
        for cnt, line in enumerate(fp):
            currentLine = list(map(int, line.split()))
            if cnt == 0:
                triangleMaxSum += currentLine[currentIndex]
            else:
                probableValues = [currentLine[currentIndex],
                                  currentLine[currentIndex+1]]
                currentIndex = currentLine.index(max(probableValues))
                triangleMaxSum += max(probableValues)
            print(currentIndex)

    return triangleMaxSum
