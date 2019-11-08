# DataAnalyticsDeveloper_Assessment
**READ HERE FIRST**

Collection of solved problems 

Programming Env. = Python 3.6 or higher

## Exercise 1
The front interface is represented graphically using Tkinter, while the backend is in either the partABackend.py or partBBackend.py files.

To run the program, run "python3 main.py" from the terminal. 

Part A functionality is dependent on the data file in the "Exercise1/Data" folder.
Part B functionality is dependent on the string entered in the GUI window.

Below shows a screenshot of the program running.

![](programcap.gif)

### Part A 

The function that does the processing of part A can be found in "Exercise 1/partABackend.py". Below shows the uncommented version of the function.
To view the entire function with comments, inspect the partABackend.py file.
```python
def triangleAdjacentMaxDynamic(FileLocation):
    with open(FileLocation, "r") as fp:
        lines = [line.strip() for line in fp.readlines()]
        lines = [line.split() for line in lines]
        lines = [list(map(int, line)) for line in lines]
        while len(lines) > 1:
            for i in range(0, len(lines[-2])):
                lines[-2][i] = max(lines[-2][i]+lines[-1][i],
                                   lines[-2][i]+lines[-1][i+1])
            del lines[-1]
        maxSum = lines[0][0]
    return(maxSum)
```

### Part B

The public class and inherent public function represent for the processing of part B can be found in "Exercise 1/partBBackend.py". Below shows the uncommented version of the function.
To view the entire function with comments, inspect the partBBackend.py file.
```python
import string
from collections import Counter
class MissingLetters:
    def GetMissingLetters(self, sentence: str):
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
                    'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
                    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        printable = set(string.printable)
        sentence = sentence.lower()
        sentence = list(filter(lambda x: x in printable,
                               sentence.replace(" ", "")))
        nonLetters = list((Counter(alphabet) - Counter(sentence)).elements())
        return nonLetters
```

## Exercise 2

Execrise 2 is contained in the Jupyter Notebook Environment. All details are within the main ".ipynb" file in the "Exercise 2" folder.
