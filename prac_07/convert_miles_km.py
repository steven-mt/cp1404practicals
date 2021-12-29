from kivy.app import App
from kivy.lang import Builder


class MilesToKilometresApp(App):
    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root


MilesToKilometresApp().run()
