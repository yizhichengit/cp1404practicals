from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

Builder.load_file('dynamic_labels.kv')

class Simple_Labels_App(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ["Yizhi", "Xiaoyu", "Jiaxiang", "Haotian"]

    def build(self):
        self.title = "Simple Labels"
        layout = Builder.load_file('dynamic_labels.kv')
        self.create_labels(layout)
        return layout

    def create_labels(self, layout):
        for name in self.names:
            label = Label(text=name)
            layout.ids.main.add_widget(label)

Simple_Labels_App().run()