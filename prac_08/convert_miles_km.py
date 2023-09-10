from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILE_TO_KM = 1.609344


class Convert_miles_km(App):
    output_km = StringProperty()

    def build(self):
        self.title = "Convert miles to km"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self, value):
        miles = self.is_empty(value)
        self.update_result(miles)

    def text_calculate(self, value, change):
        result = self.is_empty(value) + change
        self.root.ids.input_number.text = str(result)

    def is_empty(text):
        try:
            return float(text)
        except ValueError:
            return 0.0

    def update_result(self, miles):
        self.output_km = str(miles * MILE_TO_KM)


Convert_miles_km().run()
