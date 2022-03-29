from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup


class Root(BoxLayout):
    def limpiaLabel(self):
     if self.ids['user_input'].text != "":
        self.ids['enrique_label'].text = self.ids['user_input'].text
     else:
        aviso =Popup(title='Test popup', content=Label(text='Introduce Texto'),
                      auto_dismiss=False)
        aviso.open()


class MainApp(App):
    pass


if __name__ == '__main__':
    MainApp().run()
