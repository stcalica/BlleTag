from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

#controller class
class Form(GridLayout):
	def __init__(self, **kwargs):
		super(Form, self).__init__(**kwargs)
		self.cols = 2
		self.add_widget(Label(text="Store"))
		self.store = TextInput(multiline=False)
		self.add_widget(self.store)
		self.add_widget(Label(text="Item"))
		self.item = TextInput(multiline=False)
		self.add_widget(self.item)
		self.add_widget(Button(text="Broadcast Sale", on_press=self.submit))
		self.add_widget(Button(text="Clear", on_press=self.clear))
	def submit(self, *args):
		print("button pressed")
		
	def clear(self, *args):
		print("clear is pressed")

#actuall app
class BlueTagApp(App):
    def build(self):
        return Form()


if __name__ == '__main__':
    BlueTagApp().run()
