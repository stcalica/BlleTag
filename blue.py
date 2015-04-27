from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
#controller class
class BlueApp(Widget):
	def __init__(self):
		Widget.__init__(self)
		textinput = TextInput(text="Who are you?")
		self.add_widget(textinput)


#actuall app
class BlueTag(App):
    def build(self):
    	textinput = TextInput(text='Hello')
        return BlueApp()


if __name__ == '__main__':
    BlueTag().run()
