import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.graphics import Color, Line
from kivy.properties import NumericProperty, ObjectProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout

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
            root.manager.current = 'MeditationScreen'
             
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
       
<MeditationScreen>:    
    canvas:
        Color:
            rgba: 255, 255, 255, 255
        Rectangle:
            size: self.size
            
    Label:
        Image:
            source: r'C:\\Users\\egorm\\PycharmProjects\\Bamboo\\Images\\bamboo_green_2.png'
            size_hint: None, None
            size: 400, 400
            x: 150
            y: 450
            
    Label:
        Image:
            source: r'C:\\Users\\egorm\\PycharmProjects\\Bamboo\\Images\\bamboo_green_2.png'
            size_hint: None, None
            size: 400, 400
            x: -220
            y: -210
                                     
<Calendar>:
    canvas:
        Color:
            rgba: 255, 255, 255, 255
        Rectangle:
            size: self.size
""")

class ImageButton(Button):
    def __init__(self, **kwargs):
        super(ImageButton, self).__init__(**kwargs)
        self.size_hint = (None, None)
        self.size = (35, 56)
        self.x = 315
        self.y = 15
        self.background_normal = 'Images/Clock_small.png'
        self.background_down = 'Images/Clock_small.png'

class Start(Screen):
    def __init__(self, **kwargs):
        super(Start, self).__init__(**kwargs)
        layout = FloatLayout()
        button = ImageButton()
        button.bind(on_release=self.notific)
        layout.add_widget(button)
        self.add_widget(layout)

    def notific(self, instance):
        grid_layout = GridLayout(cols=1, padding=10)
        for time in ['10:00', '15:00', '20:00', '25:00', '30:00']:
            time_button = Button(text=time, background_color=(0.552, 0.843, 0.478, 1))
            time_button.bind(on_release=lambda btn: popup.dismiss())
            grid_layout.add_widget(time_button)

        popup = Popup(title='Set Your Time', content=grid_layout, size_hint=(None, None), size=(300, 300))
        popup.open()

class CountdownTimer(Widget):
    time_remaining = NumericProperty(600)
    circle = ObjectProperty(None)
    time_label = ObjectProperty(None)

    def __init__(self, manager, **kwargs):
        super(CountdownTimer, self).__init__(**kwargs)
        self.manager = manager
        self._update_circle()
        self._update_time_label()

        layout = FloatLayout()
        button = Button(
            text='SURRENDER',
            font_size=32,
            size_hint=(None, None),
            size=(200, 60),
            pos=(self.center_x+40, self.center_y+50),
            color=(0.552, 0.843, 0.478, 1),
            background_color=(0, 0, 0, 0),
            font_name=r'C:\\Users\\egorm\\PycharmProjects\\Bamboo\\font\\ComicNeue-Regular.ttf'
        )
        layout.add_widget(button)
        button.bind(on_release=self.notification)
        self.add_widget(layout)

    def _update_circle(self, *args):
        if self.circle:
            self.canvas.remove(self.circle)
        with self.canvas:
            Color(0.552, 0.843, 0.478, 1)
            self.circle = Line(circle=(self.center_x+140, self.center_y+300, 150, 0, 360 * (self.time_remaining / 10)), width=3)

    def _update_time_label(self, *args):
        if self.time_label:
            self.remove_widget(self.time_label)
        self.time_label = Label(text=str(int(self.time_remaining)), pos=(self.center_x+90, self.center_y+250),
                                font_size=100, font_name=r'C:\\Users\\egorm\\PycharmProjects\\Bamboo\\font\\ComicNeue-Bold.ttf',
                                color = (0.552, 0.843, 0.478, 1))
        self.add_widget(self.time_label)

    def notification(self, button):
        layout = GridLayout(cols=1, padding=10)
        popup_label = Label(text='Are you sure you want to give up?')
        finish_button = Button(text='Yes... Give up', background_color=(0.552, 0.843, 0.478, 1))
        close_button = Button(text='No! Continue', background_color=(0.552, 0.843, 0.478, 1))

        layout.add_widget(popup_label)
        layout.add_widget(finish_button)
        layout.add_widget(close_button)

        popup = Popup(title='SURRENDER!?', content=layout, size_hint=(None, None), size=(300, 200))
        finish_button.bind(on_press=self.go_to_second_screen, on_release=popup.dismiss)
        close_button.bind(on_release=popup.dismiss)
        popup.open()

    '''                                             # MAYBE IN FUTURE UPDATES
    def timeout_notif(self, button):
        layout = GridLayout(cols=1, padding=10)
        popup_label_ok = Label(text='Congratulation')
        ok_button = Button(text='OK', background_color=(0.552, 0.843, 0.478, 1))

        layout.add_widget(popup_label_ok)
        layout.add_widget(ok_button)

        popup_ok = Popup(title='You did it!', content=layout, size_hint=(None, None), size=(300, 200))
        ok_button.bind(on_press=self.go_to_second_screen, on_release=popup_ok.dismiss)
        popup_ok.open()
    '''

    def update(self, dt):
        if self.time_remaining > 0:
            self.time_remaining -= 1
            minutes = self.time_remaining // 60
            seconds = self.time_remaining % 60
            self.time_label.text = f'{minutes:02d}:{seconds:02d}'
        else:
            self.time_remaining = 0
            self.go_to_second_screen()

    def go_to_second_screen(self, *args):
        screen_manager.transition = SlideTransition(direction='right', duration=1)
        screen_manager.current = 'Start'

class MeditationScreen(Screen):
    def __init__(self, **kwargs):
        super(MeditationScreen, self).__init__(**kwargs)
        self.timer = None

    def on_enter(self, *args):
        if not self.timer:
            self.timer = CountdownTimer(self)
            Clock.schedule_interval(self.timer.update, 1.0)
            self.add_widget(self.timer)

    def on_leave(self, *args):
        if self.timer:
            Clock.unschedule(self.timer.update)
            self.remove_widget(self.timer)
            self.timer = None

class Calendar(Screen):
    pass

screen_manager=ScreenManager()
screen_manager.add_widget(Start(name="Start"))
screen_manager.add_widget(MeditationScreen(name="MeditationScreen"))
screen_manager.add_widget(Calendar(name="Calendar"))

class Bamboo(App):
    def build(self):
        Window.size = (375, 645)
        screen_manager.current = 'Start'
        return screen_manager
    def build_T(self):
        return MeditationScreen()

Bamboo_App=Bamboo()
Bamboo_App.run()

'''
- TODO:
1. Create a new screen or notification for time setting.  10, 15, 20, 25, 30 (min)
2. Create a new screen for meditation days counting.
'''