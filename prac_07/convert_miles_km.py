from kivy.app import App
from kivy.lang import Builder

MILES_IN_KM = 1.60934
INVALID_INPUT_SUBSTITUTE = 0


class MilesToKilometresApp(App):

    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_convert(self):
        """Handle conversion of miles to km."""
        result = self.get_valid_input() * MILES_IN_KM
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, change):
        """Handle increment or decrement of input and updates output."""
        result = self.get_valid_input() + change
        self.root.ids.input_number.text = str(result)
        self.handle_convert()

    def get_valid_input(self):
        """Try to get a valid number from the input, otherwise use a substitute value."""
        try:
            value = float(self.root.ids.input_number.text)
            return value
        except ValueError:
            return INVALID_INPUT_SUBSTITUTE


MilesToKilometresApp().run()
