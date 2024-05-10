from logic import convert_logic
from tkinter import *

class GUI:

    def __init__(self, window) -> None:

        '''
        This function is the main General User Interface
        that is displayed when someone opens the app.

        :param window: primary tkinter display
        '''

        self.window = window

        custom_font1 = ("Courier New", 22)
        custom_font2 = ("Courier New", 8)
        custom_font3 = ("Verdana", 12)

        curr_list = ['EUR', 'USD', 'JPY', 'CAD', 'AUD', 'CHF', 'BYR', 'ZAR', 'RUB', 'LBP']
        self.curr_name = {
            'EUR': 'Euro(s)              ',
            'USD': 'US Dollar(s)         ',
            'JPY': 'Japan Yen            ',
            'CAD': 'Canadian Dollar(s)   ',
            'AUD': 'Australian Dollars(s)',
            'CHF': 'Swiss Franc(s)       ',
            'BYR': 'Belarus Ruble(s)     ',
            'ZAR': 'South African Rand(s)',
            'RUB': 'Russia Rouble(s)     ',
            'LBP': 'Lebanon Pound(s)     '
        }

        self.instruction = Label(self.window, text='What would you like to Convert?', font=custom_font2)
        self.instruction.pack()

        self.frame_one = Frame(self.window)
        self.clicked_from = StringVar(value='EUR')
        self.clicked_to = StringVar(value='USD')
        self.from_label = Label(self.frame_one, text='From ', font=custom_font1)
        self.from_type = OptionMenu(self.frame_one, self.clicked_from, *curr_list, command=self.curr_change)
        self.to_label = Label(self.frame_one, text=' to ', font=custom_font1)
        self.to_type = OptionMenu(self.frame_one, self.clicked_to, *curr_list, command=self.curr_change)
        self.from_label.pack(side='left')
        self.from_type.pack(side='left')
        self.to_label.pack(side='left')
        self.to_type.pack(side='left')
        self.frame_one.pack(pady=12)

        self.frame_two = Frame(self.window)
        self.from_input = Entry(self.frame_two, width=7)
        self.arrow_label = Label(self.frame_two, text='-->', font=custom_font1)
        self.to_output = Label(self.frame_two, text='[                   ]', font=custom_font3)
        self.from_input.pack(side='left', padx=5)
        self.arrow_label.pack(side='left', padx=10)
        self.to_output.pack(side='left')
        self.frame_two.pack()

        self.frame_three = Frame(self.window)
        self.currency_types = Label(self.window, text=f'{self.curr_name[self.clicked_from.get()]}        {(self.curr_name[self.clicked_to.get()]).strip()}', font=custom_font2)
        self.currency_types.pack()
        self.frame_three.pack(pady=6)

        self.frame_four = Frame(self.window)
        self.submit_button = Button(self.frame_four, text='CONVERT', command=self.convert)
        self.submit_button.pack()
        self.frame_four.pack()

        self.frame_five = Frame(self.window)
        self.error_label = Label(self.frame_five, text='', font=custom_font2)
        self.error_label.pack()
        self.frame_five.pack(pady=4)

    def curr_change(self, *args) -> None:

        '''
        This quick function is used to change the name of the current currency that the
        user has selected. So as the user selects which currency to convert, this function
        will switch to the corresponding name using the curr_name dictionary.

        :param args: used to pass the list of country abbreviations to the function
        :return:
        '''

        self.currency_types.config(text=f"{self.curr_name[self.clicked_from.get()]}        {(self.curr_name[self.clicked_to.get()]).strip()}")

    def convert(self) -> None:

        '''
        This function utilizes the logic from the logic file that
        is imported at the top of the page in order to convert
        currencies based on exchange rates from an API

        :return:
        '''

        amount = self.from_input.get()
        from_curr = self.clicked_from.get()
        to_curr = self.clicked_to.get()

        self.error_label.config(text='')

        try:

            conversion = convert_logic(amount, from_curr, to_curr)

            self.to_output.config(text=f'{conversion:.2f}')

        except ValueError:

            self.error_label.config(text='Incorrect Values Entered: int or float')

        except TypeError:

            self.error_label.config(text='Incorrect Values Entered: no (-) values')

