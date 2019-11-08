# Author: Darren Ramsook
# Date Created: 6/11/2019


from tkinter import *
from partABackend import triangleAdjacentMaxDynamic
from partBBackend import MissingLetters


def runPartA():
    popupPartA = Tk()
    popupPartA.geometry("400x100")
    popupPartA.title("Results for Part A")
    fileName = partAEntry.get()
    resultA = triangleAdjacentMaxDynamic("Data/"+fileName)
    popupALabel = Label(popupPartA, text="Source of Data: "+fileName)
    popupALabel.pack()
    resultALabel = Label(popupPartA, text="Optimal Value: "+str(resultA))
    resultALabel.pack(pady=10)

    def partAquit():
        popupPartA.destroy()
    popupAButton = Button(popupPartA, text="Close",
                          command=partAquit)
    popupAButton.pack()


def runPartB():
    popupPartB = Tk()
    popupPartB.geometry("700x100")
    popupPartB.title("Results for Part B")
    inputSentence = partBEntry.get()
    sentenceClass = MissingLetters()
    resultB = sentenceClass.GetMissingLetters(inputSentence)
    popupBLabel = Label(popupPartB, text="Input Sentence: '"+inputSentence+"'")
    popupBLabel.pack()
    resultBLabel = Label(
        popupPartB, text="Chars. not found: "+str(resultB))
    resultBLabel.pack(pady=10)

    def partBquit():
        popupPartB.destroy()
    popupBButton = Button(popupPartB, text="Close",
                          command=partBquit)
    popupBButton.pack()


window = Tk()

window.title("Data Analytics Developer Solutions")
window.geometry("600x350")
window.configure(bg="#9DC8C8")


mainLabel = Label(window, text="Exercise #1 Solutions",
                  bg="#9DC8C8", font=(None, 22))
mainLabel.pack(fill=X, pady=(10, 0))

subMainLabel = Label(
    window, text="Results for both Part A & B from Exercise #1 of the Data Analytics Assessment", bg="#9DC8C8", font=(None, 13), relief="ridge")
subMainLabel.pack(fill=X, pady=10)

partALabel = Label(
    window, text="Enter name of .txt file in \"Data\" folder and press the \"Run Part A\" button:", bg="#9DC8C8")
partALabel.pack()

partAEntry = Entry(window)
partAEntry.insert(END, 'triangle.txt')
partAEntry.pack()

partAButton = Button(window, text="Run Part A", command=runPartA,
                     bg="#9DC8C8")
partAButton.pack(pady=10)

sepLabel = Label(window, text=" ", font=(None, 2), bg='#D4DFE6')
sepLabel.pack(fill=X, pady=10)
partBLabel = Label(
    window, text="Enter the desired sentence and press the \"Run Part A\" button:", bg="#9DC8C8")
partBLabel.pack()

partBEntry = Entry(window)
partBEntry.insert(END, "This is a test pangram")
partBEntry.pack()

partBButton = Button(window, text="Run Part B", command=runPartB,
                     bg="#9DC8C8")
partBButton.pack(pady=10)


window.mainloop()
