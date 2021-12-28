import kivy
# import main
from kivy.app import App  
       
# this restrict the kivy version i.e   
# below this kivy version you cannot   
# use the app or software   
kivy.require('1.9.0')  
  
# to  use this must have to import it
from kivy.uix.tabbedpanel import TabbedPanel
  
# Floatlayout allows us to place the elements
# relatively based on the current window
# size and height especially in mobiles
from kivy.uix.floatlayout import FloatLayout
  
# Create Tabbed class 
class Tab(TabbedPanel):
    pass
   
# create App class
class TabbedPanelApp(App):
    def build(self):
        return Tab()
  
# run the App
if __name__ == '__main__':
    TabbedPanelApp().run()