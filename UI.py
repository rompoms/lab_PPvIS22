from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.recycleview import RecycleView
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.config import ConfigParser
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.metrics import dp
from datetime import datetime
from kivy.uix.floatlayout import FloatLayout
import os
import ast
import time


class MenuScreen(Screen):
    def __init__(self, **kw):
        super(MenuScreen, self).__init__(**kw)
        Layout = GridLayout(cols = 4, rows =1, row_force_default=True,row_default_height=40)
        layout = FloatLayout(size=(20, 20))
        Layout.add_widget(Button(text='Бой',background_color="red"))

        Layout.add_widget(Button(text='Изменить бойцов'))

        Layout.add_widget(Button(text='Изменить удары'))

        Layout.add_widget(Button(text='Настройки',
                              on_press=lambda x: set_screen('add_food')))

        layout.add_widget(Button(text='Выбрать', size_hint=(.15, .015), pos=(100, 150), ))

        layout.add_widget(Button(text='Выбрать', size_hint=(.15, .015), pos=(580, 150), ))

        self.add_widget(layout)
        self.add_widget(Layout)

        self.txt1 = TextInput(text='', multiline=True, height=dp(40),
                              size_hint_y=None, pos=(280, 200),size_hint=(.3, .5))
        layout.add_widget(self.txt1)

        self.txt2 = TextInput(text='0 ИМЯ1\n1 ИМЯ2\n2 ИМЯ3\n3 ИМЯ4\n4 ИМЯ5', multiline=True, height=dp(40),
                              size_hint_y=None, pos=(550, 200),size_hint=(.2, .4))
        layout.add_widget(self.txt2)

        self.txt3 = TextInput(text='0 ИМЯ1\n1 ИМЯ2\n2 ИМЯ3\n3 ИМЯ4\n4 ИМЯ5', multiline=False, height=dp(40),
                              size_hint_y=None, pos=(90, 200),size_hint=(.2, .4))
        layout.add_widget(self.txt3)





class SortedListFood(Screen):
    def __init__(self, **kw):
        super(SortedListFood, self).__init__(**kw)

    def on_enter(self):  # Будет вызвана в момент открытия экрана

        self.layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
        self.layout.bind(minimum_height=self.layout.setter('height'))
        back_button = Button(text='< Назад в главное меню',
                             on_press=lambda x: set_screen('menu'),
                             size_hint_y=None, height=dp(40))
        self.layout.add_widget(back_button)
        root = RecycleView(size_hint=(1, None), size=(Window.width,
                                                      Window.height))
        root.add_widget(self.layout)
        self.add_widget(root)

        dic_foods = ast.literal_eval(
            App.get_running_app().config.get('General', 'user_data'))

        for f, d in sorted(dic_foods.items(), key=lambda x: x[1]):
            fd = f.decode('u8') + ' ' + (datetime.fromtimestamp(d).strftime('%Y-%m-%d'))
            btn = Button(text=fd, size_hint_y=None, height=dp(40))
            self.layout.add_widget(btn)

    def on_leave(self):  # Будет вызвана в момент закрытия экрана

        self.layout.clear_widgets()  # очищаем список


class AddFood(Screen):

    def buttonClicked(self, btn1):
        if not self.txt1.text:
            return
        self.app = App.get_running_app()
        self.app.user_data = ast.literal_eval(
            self.app.config.get('General', 'user_data'))
        self.app.user_data[self.txt1.text.encode('u8')] = int(time.time())

        self.app.config.set('General', 'user_data', self.app.user_data)
        self.app.config.write()

        text = "Последнее изменённые характеристики:  " + self.txt1.text
        self.result.text = text
        self.txt1.text = ''

    def __init__(self, **kw):
        super(AddFood, self).__init__(**kw)
        box = BoxLayout(orientation='vertical')
        back_button = Button(text='< Назад в главное меню', on_press=lambda x:
                             set_screen('menu'), size_hint_y=None, height=dp(40))

        box.add_widget(back_button)
        self.txt1 = TextInput(text='Имя:', multiline=True, height=dp(40),
                              size_hint_y=None)
        box.add_widget(self.txt1)
        self.txt2 = TextInput(text='Масса:', multiline=True, height=dp(40),
                              size_hint_y=None)
        box.add_widget(self.txt2)
        self.txt3 = TextInput(text='Сила:', multiline=True, height=dp(40),
                              size_hint_y=None)
        box.add_widget(self.txt3)
        self.txt4 = TextInput(text='Ловкость:', multiline=True, height=dp(40),
                              size_hint_y=None)
        box.add_widget(self.txt4)
        self.txt5 = TextInput(text='Быстрота:', multiline=True, height=dp(40),
                              size_hint_y=None)
        box.add_widget(self.txt5)
        self.txt6 = TextInput(text='Выносливость:', multiline=True, height=dp(40),
                              size_hint_y=None)
        box.add_widget(self.txt6)


        btn1 = Button(text="Изменить характеристики", size_hint_y=None, height=dp(40))
        btn1.bind(on_press=self.buttonClicked)
        box.add_widget(btn1)
        self.result = Label(text='')
        box.add_widget(self.result)
        self.add_widget(box)


def set_screen(name_screen):
    sm.current = name_screen


sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(SortedListFood(name='list_food'))
sm.add_widget(AddFood(name='add_food'))


class FoodOptionsApp(App):
    def __init__(self, **kvargs):
        super(FoodOptionsApp, self).__init__(**kvargs)
        self.config = ConfigParser()

    def build_config(self, config):
        config.adddefaultsection('General')
        config.setdefault('General', 'user_data', '{}')

    def set_value_from_config(self):
        self.config.read(os.path.join(self.directory, '%(appname)s.ini'))
        self.user_data = ast.literal_eval(self.config.get(
            'General', 'user_data'))

    def get_application_config(self):
        return super(FoodOptionsApp, self).get_application_config(
            '{}/%(appname)s.ini'.format(self.directory))

    def build(self):
        return sm


if __name__ == '__main__':
    FoodOptionsApp().run()


