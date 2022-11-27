from kivy.app import App, Builder
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from src.ui.button_stash import buttons


class MainApp(App):

  results_input = None


  class MyButton(Button):
    pass


  class MainWindow(BoxLayout):
    pass


  class ButtonsLine(BoxLayout):
    pass


  class OutputText(TextInput):
    pass


  def create_btn_field(self, layout):

    self.results_input = self.OutputText()

    layout.add_widget(self.results_input)

    for btns_symbol in buttons:
      btn_line = self.ButtonsLine()

      for symbol in btns_symbol:
        btn_line.add_widget(self.MyButton(text=symbol, on_press=self.on_click_btn))

      layout.add_widget(btn_line)
    
    layout.add_widget(self.MyButton(text='=', on_press=self.calculate))


  def on_click_btn(self, instance):

    if instance.text in ['C']: return self.clear_filed()
    if self.results_input.text in ['Error']: return self.clear_filed()

    self.results_input.text += instance.text


  def clear_filed(self):
    self.results_input.text = ''


  def calculate(self, instance):
    try :
      results = eval(self.results_input.text) or 'Error'
      self.results_input.text = str(results)
    except:
      self.results_input.text = 'Error'

  
  # Build App
  def build(self):
    Builder.load_file('src/ui/main.kv')
    
    layout = self.MainWindow()

    self.create_btn_field(layout)

    return layout
    