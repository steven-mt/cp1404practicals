from kivy.app import App
from kivy.lang import Builder

MILES_IN_KM = 1.60934


class MilesToKilometresApp(App):

    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_convert(self, value):
        """Handle conversion of miles to km."""
        result = float(value) * MILES_IN_KM
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, miles, change):
        """Handle increment or decrement of input and updates output."""
        result = float(miles) + change
        self.root.ids.input_number.text = str(result)
        self.handle_convert(self.root.ids.input_number.text)


MilesToKilometresApp().run()
