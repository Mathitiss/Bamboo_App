import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.graphics import Color, Line
from kivy.properties import NumericProperty, ObjectProperty

kivy.require('1.9.0')

Builder.load_string("""
<Start>:
    canvas:
        Color:
            rgba: 255, 255, 255, 255
        Rectangle:
            size: self.size
                      
    Label:
        Image:
            source: r'C:\\Users\\egorm\\PycharmProjects\\Bamboo\\Images\\bamboo_green.png'
            size_hint: None, None
            size: 2000, 700
            x: -850
            y: 0
            
    Button:
        background_normal: r'C:\\Users\\egorm\\PycharmProjects\\Bamboo\\Images\\Start_Button.png'
        background_down: r'C:\\Users\\egorm\\PycharmProjects\\Bamboo\\Images\\Start_Button.png'
        size_hint: None, None
        size: 270, 260
        center_x: root.width / 2
        y: 190
        on_press:
            root.manager.transition.direction = 'left'
            root.manager.transition.duration = 1
            root.manager.current = 'Meditation'
             
    Button:
        background_normal: r'C:\\Users\\egorm\\PycharmProjects\\Bamboo\\Images\\calendar_green_1_small.png'
        background_down: r'C:\\Users\\egorm\\PycharmProjects\\Bamboo\\Images\\calendar_green_1_small.png'
        size_hint: None, None
        size: 32, 33
        x: 325
        y: 600
        on_press:
            root.manager.transition.direction = 'down'
            root.manager.transition.duration = 1
            root.manager.current = 'Calendar'
             
<Meditation>:    
    canvas:
        Color:
            rgba: 255, 255, 255, 255
        Rectangle:
            size: self.size     
             
<Calendar>:
    canvas:
        Color:
            rgba: 255, 255, 255, 255
        Rectangle:
            size: self.size
""")

class Start(Screen):
    pass

class Meditation(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.label = Label(text='10', font_size='114', pos=(0, 10), color = (0.552, 0.843, 0.478, 1),
                           font_name=r'C:\\Users\\egorm\\PycharmProjects\\Bamboo\\font\\ComicNeue-Regular.ttf')
        self.add_widget(self.label)

    def on_enter(self, *args):
        self.counter = 10
        self.label.text = str(self.counter)
        self.schedule = Clock.schedule_interval(self.update_timer, 1)

    def on_pre_leave(self, *args):
        self.schedule.cancel()

    def update_timer(self, dt):
        self.counter -= 1
        self.label.text = str(self.counter)
        if self.counter == 0:
            self.manager.current = 'Start'

class Calendar(Screen):
    pass

screen_manager = ScreenManager()
screen_manager.add_widget(Start(name="Start"))
screen_manager.add_widget(Meditation(name="Meditation"))
screen_manager.add_widget(Calendar(name="Calendar"))


class Bamboo(App):
    def build(self):
        Window.size = (375, 645)
        return screen_manager

Bamboo_App = Bamboo()
Bamboo_App.run()