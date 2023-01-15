"""
Calls kivy functions to make interactive GUI and displays everything

--- Imports all important and necessary kivy functions

--- Sets different grids
    - One for main UI to show answers at the bottom
    - Second for prompt and user input
    - Third for buttons 

--- When button number 1 is pushed:
    - Initialize Unscramble class object
    - Use object to access functions
    - initialize instance variable to list of unscrambled words
    - Display answer as list under button in main Grid

"""

from unscrambler import Unscrambler
from kivy.app import App 
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout


class myGrid(GridLayout):
    def __init__(self, **kwargs):
        super(myGrid, self).__init__(**kwargs)
        
        # Main Grid columns and rows
        self.cols = 1
        self.row = 2
        
        # Grid to hold promtp and user input
        self.inside = GridLayout()
        self.inside.cols = 2
        
        # Grid to hold buttons 
        self.inside2 = GridLayout()
        self.inside2.cols = 2
        
        self.float = FloatLayout()
        
        # Promp and user input
        self.inside.add_widget(Label(text="Scrambled Word: ", font_size=30))
        self.input = TextInput(multiline = False, font_size=25)
        self.inside.add_widget(self.input)

        self.add_widget(self.inside)

        # Button for unscrambling
        self.unscrambutton = Button(text="Unscramble", font_size=20, size_hint=(1,.5))
        self.unscrambutton.bind(on_press=self.button1)
        self.inside2.add_widget(self.unscrambutton)
        
        # Button to clear widget
        self.newwordbutton = Button(text="Type new word", font_size=20, size_hint=(1, .5))
        self.newwordbutton.bind(on_press=self.button2)
        self.inside2.add_widget(self.newwordbutton)

        self.add_widget(self.inside2)

    # Called to unscramble the word
    def button1(self, instance):
        u = Unscrambler(self.input._get_text())
        u.unscramble = ""
        instance = u.unscramble
        self.answer = Label(text=str(instance), markup=True, font_size=20)
        self.add_widget(self.answer)
    
    # Called to clear the answer shown
    def button2(self, instance):
        self.remove_widget(self.answer)




class MyApp(App):
    def build(self):
        return myGrid()





if __name__ == "__main__":
    MyApp().run()