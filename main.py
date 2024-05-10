from gui import *

def main() :

    '''
    These are the main stipulations
    for the tkinter window and GUI

    :return:
    '''

    window = Tk()
    window.title('Currency Converter')
    window.geometry('300x200')
    window.resizable(False, False)
    GUI(window)

    window.mainloop()

if __name__ == "__main__":

    main()