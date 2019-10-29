from kivy.app import App
from kivy.lang import Builder
from kivy.utils import get_color_from_hex
from kivy.uix.screenmanager import Screen, ScreenManager

from numerical_integ import simpson_method, trapeziodal_rule


class HomeScreen(Screen):
    pass

class SettingsScreen(Screen):
    pass

GUI = Builder.load_file('main.kv')


class MainApp(App):

    def build(self):
        return GUI

    def get_answer(self, values, delta_h):

        change_screen = 1
        self.root.ids['home_screen'].ids['submit'].background_color = get_color_from_hex('#4A4348')
        
        list_of_values = values.split('\n')
        if len(list_of_values) >= 2:
            list_of_values = [eval(x) for x in list_of_values if x != '']
        else:
            change_screen = 0

        if delta_h:
            delta_h = eval(delta_h)
        else:
            change_screen = 0

        if change_screen:
            if len(list_of_values) % 2 == 1:
                answer = str(simpson_method(list_of_values, delta_h))
            else:
                answer = str(trapeziodal_rule(list_of_values, delta_h))

            self.root.ids['results_screen'].ids['answer'].text = answer

            screen_manager = self.root.ids['screen_manager']

            screen_manager.current = 'results_screen'
            screen_manager.transition.direction = 'left'

    def change_screen(self, screen_name):
        self.root.ids['results_screen'].ids['go_back'].background_color = get_color_from_hex('#4A4348')
        screen_manager = self.root.ids['screen_manager']

        screen_manager.current = screen_name
        screen_manager.transition.direction = 'right'


MainApp().run()
