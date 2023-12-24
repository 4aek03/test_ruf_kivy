from kivy.app import App

from kivy.graphics import Rectangle
from kivy.graphics.texture import Texture

from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.clock import Clock

from kivy.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import Screen

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout

from inst import *






# ------------------------------------------------------------------  1 экран  ------------------------------------------------------------------
class Screen1(Screen):
    def __init__(self, name='1_screen'):
        super().__init__(name=name)

        # ---------------------------------  сам разбирайсяю. это задний фон  ---------------------------------
        self.texture = Texture.create(size=(2, 2), colorfmt='rgb')
        p1_color = [100, 149, 237]
        p2_color = [106, 90, 205]
        p3_color = [106, 90, 205]
        p4_color = [100, 149, 237]
        p = p1_color + p2_color + p3_color + p4_color
        buf = bytes(p)
        self.texture.blit_buffer(buf, colorfmt='rgb')
        with self.canvas:
            self.rect = Rectangle(pos=self.pos, size=self.size, texture=self.texture)

        self.bind(size=self.update_rect)
        self.bind(pos=self.update_rect)
    def update_rect(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos


        # ---------------------------------главный текс---------------------------------
        txt = Label(text = txt_instruction)
        altxt = AnchorLayout(size_hint=[.1, .1], pos_hint={'center_x': 0.5, 'center_y': 0.7})  # это параметры текста о приложении
        altxt.add_widget(txt)
        self.add_widget(altxt)


        # ---------------------------------ввод текста---------------------------------
        ti = TextInput()
        alti = AnchorLayout(size_hint=[.3, .04], pos_hint={'center_x': 0.6, 'center_y': 0.3} )  # это параметры ввода текста
        alti.add_widget(ti)
        self.add_widget(alti)

        ti1 = TextInput()
        alti1 = AnchorLayout(size_hint=[.3, .04], pos_hint={'center_x': 0.6, 'center_y': 0.2})  # это параметры ввода текста 1 (нижнего)
        alti1.add_widget(ti1)
        self.add_widget(alti1)


        # ---------------------------------текст к вводу текста---------------------------------
        txt1 = Label(text = 'Введите имя:')
        altx1 = AnchorLayout(size_hint=[.3, .04], pos_hint={'center_x': 0.3, 'center_y': 0.3} )   # это параметры текста для ввода текста
        altx1.add_widget(txt1)
        self.add_widget(altx1)

        txt2 = Label(text = 'Введите возраст:')
        altx2 = AnchorLayout(size_hint=[.3, .04], pos_hint={'center_x': 0.3, 'center_y': 0.2} )   # это параметры текста для ввода текста 1 (нижнего)
        altx2.add_widget(txt2)
        self.add_widget(altx2)


    # ---------------------------------кнопка начать---------------------------------
        btn1 = Button(text="начать")
        albtn1 = AnchorLayout(size_hint=[.2, .1], pos_hint={'center_x': 0.5, 'center_y': 0.1})
        albtn1.add_widget( btn1)
        btn1.on_press = self.next
        self.add_widget(albtn1)

    def next(self):
        self.manager.transition.direction = 'left'
        self.manager.current = "2_screen"




# ------------------------------------------------------------------  2 экран  ------------------------------------------------------------------
class Screen2(Screen):
    def __init__(self, name='2_screen'):
        super().__init__(name=name)

        # ---------------------------------  сам разбирайся. это задний фон  ---------------------------------
        self.texture = Texture.create(size=(2, 2), colorfmt='rgb')
        p1_color = [100, 149, 237]
        p2_color = [106, 90, 205]
        p3_color = [106, 90, 205]
        p4_color = [100, 149, 237]
        p = p1_color + p2_color + p3_color + p4_color
        buf = bytes(p)
        self.texture.blit_buffer(buf, colorfmt='rgb')
        with self.canvas:
            self.rect = Rectangle(pos=self.pos, size=self.size, texture=self.texture)

        self.bind(size=self.update_rect)
        self.bind(pos=self.update_rect)


    def todo(self, dt):
        Clock.schedule_interval(todo, 0.5)
        return False


    def update_rect(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos


        # ---------------------------------test таймер---------------------------------
        txt = Label(text = txt_test1)
        altxt = AnchorLayout(size_hint=[.1, .1],pos_hint={'center_x': 0.5, 'center_y': 0.9})  # это параметры текста о приложении
        altxt.add_widget(txt)
        self.add_widget(altxt)

        # ---------------------------------главный текс---------------------------------
        txt = Label(text = txt_test1)
        altxt = AnchorLayout(size_hint=[.1, .1],pos_hint={'center_x': 0.5, 'center_y': 0.7})  # это параметры текста о приложении
        altxt.add_widget(txt)
        self.add_widget(altxt)


        # ---------------------------------ввод текста---------------------------------
        ti = TextInput()
        alti = AnchorLayout(size_hint=[.3, .04], pos_hint={'center_x': 0.6, 'center_y': 0.2} )  # это параметры ввода текста
        alti.add_widget(ti)
        self.add_widget(alti)


        # ---------------------------------текст к вводу текста---------------------------------
        txt2 = Label(text = 'Введите результат:')
        altx2 = AnchorLayout(size_hint=[.3, .04], pos_hint={'center_x': 0.3, 'center_y': 0.2} )   # это параметры текста для ввода текста 1 (нижнего)
        altx2.add_widget(txt2)
        self.add_widget(altx2)


        # ---------------------------------кнопка продолжить---------------------------------
        btn1 = Button(text="продолжить")
        albtn1 = AnchorLayout(size_hint=[.2, .1], pos_hint={'center_x': 0.5, 'center_y': 0.1})
        albtn1.add_widget(btn1)
        btn1.on_press = self.next
        self.add_widget(albtn1)

    def next(self):
        self.manager.transition.direction = 'left'
        self.manager.current = "3_screen"




# ------------------------------------------------------------------  3 экран  ------------------------------------------------------------------
class Screen3(Screen):
    def __init__(self, name='3_screen'):
        super().__init__(name=name)

        # ---------------------------------  сам разбирайся. это задний фон  ---------------------------------
        self.texture = Texture.create(size=(2, 2), colorfmt='rgb')
        p1_color = [100, 149, 237]
        p2_color = [106, 90, 205]
        p3_color = [106, 90, 205]
        p4_color = [100, 149, 237]
        p = p1_color + p2_color + p3_color + p4_color
        buf = bytes(p)
        self.texture.blit_buffer(buf, colorfmt='rgb')
        with self.canvas:
            self.rect = Rectangle(pos=self.pos, size=self.size, texture=self.texture)

        self.bind(size=self.update_rect)
        self.bind(pos=self.update_rect)

    def update_rect(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos


        # ---------------------------------главный текс---------------------------------
        txt = Label(text=txt_test2)
        altxt = AnchorLayout(size_hint=[.1, .1],
                             pos_hint={'center_x': 0.5, 'center_y': 0.7})  # это параметры текста о приложении
        altxt.add_widget(txt)
        self.add_widget(altxt)


        # ---------------------------------кнопка продолжить---------------------------------
        btn1 = Button(text="продолжить")
        albtn1 = AnchorLayout(size_hint=[.2, .1], pos_hint={'center_x': 0.5, 'center_y': 0.1})
        albtn1.add_widget(btn1)
        btn1.on_press = self.next
        self.add_widget(albtn1)

    def next(self):
        self.manager.transition.direction = 'left'
        self.manager.current = "4_screen"




# ------------------------------------------------------------------  4 экран  ------------------------------------------------------------------
class Screen4(Screen):
    def __init__(self, name='4_screen'):
        super().__init__(name=name)

        # ---------------------------------  сам разбирайсяю. это задний фон  ---------------------------------
        self.texture = Texture.create(size=(2, 2), colorfmt='rgb')
        p1_color = [100, 149, 237]
        p2_color = [106, 90, 205]
        p3_color = [106, 90, 205]
        p4_color = [100, 149, 237]
        p = p1_color + p2_color + p3_color + p4_color
        buf = bytes(p)
        self.texture.blit_buffer(buf, colorfmt='rgb')
        with self.canvas:
            self.rect = Rectangle(pos=self.pos, size=self.size, texture=self.texture)

        self.bind(size=self.update_rect)
        self.bind(pos=self.update_rect)

    def update_rect(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos


        # ---------------------------------главный текс---------------------------------
        txt = Label(text=txt_test3)
        altxt = AnchorLayout(size_hint=[.1, .1],
                             pos_hint={'center_x': 0.5, 'center_y': 0.7})  # это параметры текста о приложении
        altxt.add_widget(txt)
        self.add_widget(altxt)


        # ---------------------------------ввод текста---------------------------------
        ti = TextInput()
        alti = AnchorLayout(size_hint=[.3, .04],
                            pos_hint={'center_x': 0.6, 'center_y': 0.3})  # это параметры ввода текста
        alti.add_widget(ti)
        self.add_widget(alti)

        ti1 = TextInput()
        alti1 = AnchorLayout(size_hint=[.3, .04],
                             pos_hint={'center_x': 0.6, 'center_y': 0.2})  # это параметры ввода текста 1 (нижнего)
        alti1.add_widget(ti1)
        self.add_widget(alti1)


        # ---------------------------------текст к вводу текста---------------------------------
        txt1 = Label(text='Результат:')
        altx1 = AnchorLayout(size_hint=[.3, .04],
                             pos_hint={'center_x': 0.3, 'center_y': 0.3})  # это параметры текста для ввода текста
        altx1.add_widget(txt1)
        self.add_widget(altx1)

        txt2 = Label(text='Результат после отдыха:')
        altx2 = AnchorLayout(size_hint=[.3, .04], pos_hint={'center_x': 0.3,'center_y': 0.2})  # это параметры текста для ввода текста 1 (нижнего)
        altx2.add_widget(txt2)
        self.add_widget(altx2)


        # ---------------------------------кнопка завершить---------------------------------
        btn1 = Button(text="завершить")
        albtn1 = AnchorLayout(size_hint=[.2, .1], pos_hint={'center_x': 0.5, 'center_y': 0.1})
        albtn1.add_widget(btn1)
        btn1.on_press = self.next
        self.add_widget(albtn1)

    def next(self):
        self.manager.transition.direction = 'left'
        self.manager.current = "5_screen"





# ------------------------------------------------------------------  5 экран  ------------------------------------------------------------------
class Screen5(Screen):
    def __init__(self, name='5_screen'):
        super().__init__(name=name)

        # ---------------------------------  сам разбирайсяю. это задний фон  ---------------------------------
        self.texture = Texture.create(size=(2, 2), colorfmt='rgb')
        p1_color = [100, 149, 237]
        p2_color = [106, 90, 205]
        p3_color = [106, 90, 205]
        p4_color = [100, 149, 237]
        p = p1_color + p2_color + p3_color + p4_color
        buf = bytes(p)
        self.texture.blit_buffer(buf, colorfmt='rgb')
        with self.canvas:
            self.rect = Rectangle(pos=self.pos, size=self.size, texture=self.texture)

        self.bind(size=self.update_rect)
        self.bind(pos=self.update_rect)

    def update_rect(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos

        # ---------------------------------главный текс---------------------------------
        txt = Label(text=txt_sits)
        altxt = AnchorLayout(size_hint=[.1, .1],
                             pos_hint={'center_x': 0.5, 'center_y': 0.7})  # это параметры текста о приложении
        altxt.add_widget(txt)
        self.add_widget(altxt)




class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Screen1())
        sm.add_widget(Screen2())
        sm.add_widget(Screen3())
        sm.add_widget(Screen4())
        sm.add_widget(Screen5())
        return sm
app = MyApp()
app.run()