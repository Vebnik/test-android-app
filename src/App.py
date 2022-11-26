from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from src.ui.button_stash import buttons


class MyButton(Button):
  pass


class MainWindow(BoxLayout):
  pass


class ButtonsLine(BoxLayout):
  pass


class MainApp(App):

  def build(self):
    layout = MainWindow()

    for btns_symbol in buttons:
      btn_line = ButtonsLine()

      for symbol in btns_symbol:
        btn_line.add_widget(MyButton(text=symbol))

      layout.add_widget(btn_line)

    return layout


  def on_click_btn(self):
    print('On click event')

    