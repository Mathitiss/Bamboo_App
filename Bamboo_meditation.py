import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.clock import Clock
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
            root.manager.current = 'TimerScreen'
             
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
             
<TimerScreen>:    
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

class CountdownTimer(Widget):
    time_remaining = NumericProperty(60)
    circle = ObjectProperty(None)
    time_label = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(CountdownTimer, self).__init__(**kwargs)
        self._update_circle()
        self._update_time_label()

    def _update_circle(self, *args):
        if self.circle:
            self.canvas.remove(self.circle)
        with self.canvas:
            Color(0.552, 0.843, 0.478, 1)
            self.circle = Line(circle=(self.center_x, self.center_y+10, 150, 0, 360 * (self.time_remaining / 60)), width=3)

    def _update_time_label(self, *args):
        if self.time_label:
            self.remove_widget(self.time_label)
        self.time_label = Label(text=str(int(self.time_remaining)), pos=(self.center_x-50, self.center_y-40),
                                font_size=124, font_name=r'C:\\Users\\egorm\\PycharmProjects\\Bamboo\\font\\ComicNeue-Regular.ttf',
                                color = (0.552, 0.843, 0.478, 1))
        self.add_widget(self.time_label)

    def update(self, dt):
        if self.time_remaining > 0:
            self.time_remaining -= dt
            self._update_circle()
            self._update_time_label()
        else:
            self.time_remaining = 0

class TimerScreen(Screen):
    def __init__(self, **kwargs):
        super(TimerScreen, self).__init__(**kwargs)
        self.timer = None

    def on_enter(self, *args):
        if not self.timer:
            self.timer = CountdownTimer()
            Clock.schedule_interval(self.timer.update, 1.0 / 60.0)
            self.add_widget(self.timer)

    def on_leave(self, *args):
        if self.timer:
            Clock.unschedule(self.timer.update)
            self.remove_widget(self.timer)
            self.timer = None

class Calendar(Screen):
    pass

screen_manager = ScreenManager()
screen_manager.add_widget(Start(name="Start"))
screen_manager.add_widget(TimerScreen(name="TimerScreen"))
screen_manager.add_widget(Calendar(name="Calendar"))

class Bamboo(App):
    def build(self):
        Window.size = (375, 645)
        return screen_manager
    def build_T(self):
        return TimerScreen()

Bamboo_App = Bamboo()
Bamboo_App.run()