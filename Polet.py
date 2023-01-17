from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.dropdown import DropDown


class MainApp(App):
    def build(self):
        layout = GridLayout(cols=1, row_force_default=True, row_default_height=30, spacing=10, padding=20)
        self.lbl = Label(text='Вас приветствует компания ПОЛЕТЕЛИ-ПРИЛЕТЕЛИ!', font_size='20sp')        
        layout.add_widget(self.lbl)
        self.destination = TextInput(text='Куда летим? ')
        layout.add_widget(self.destination)
        dropdown = DropDown()
        for index in range(10):
            btn = Button(text='Value %d' % index, size_hint_y=None, height=44)
            btn.bind(on_release=lambda btn: dropdown.select(btn.text))
            dropdown.add_widget(btn)
            mainbutton = Button(text='Hello', size_hint=(None, None))
            mainbutton.bind(on_release=dropdown.open)
            dropdown.bind(on_select=lambda instance, x: setattr(mainbutton, 'text', x))     
        return layout    


MainApp().run()