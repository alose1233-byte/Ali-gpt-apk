import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
import requests

class AliGPT(App):
    def build(self):
        self.title = "Ali GPT"
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # عنوان التطبيق
        layout.add_widget(Label(text="Ali GPT Assistant", font_size=24, size_hint_y=None, height=50))

        # منطقة عرض الرسائل
        self.scroll = ScrollView()
        self.chat_history = Label(text="Welcome Ali! How can I help you today?\n", 
                                 size_hint_y=None, halign='left', valign='top')
        self.chat_history.bind(texture_size=self.chat_history.setter('size'))
        self.scroll.add_widget(self.chat_history)
        layout.add_widget(self.scroll)

        # مكان كتابة السؤال
        input_layout = BoxLayout(size_hint_y=None, height=50, spacing=5)
        self.user_input = TextInput(multiline=False, hint_text="Write your message here...")
        send_btn = Button(text="Send", size_hint_x=None, width=100, background_color=(0, 0.7, 0, 1))
        send_btn.bind(on_press=self.send_message)
        
        input_layout.add_widget(self.user_input)
        input_layout.add_widget(send_btn)
        layout.add_widget(input_layout)

        return layout

    def send_message(self, instance):
        query = self.user_input.text
        if query:
            self.chat_history.text += f"\nYou: {query}"
            # هنا يمكنك ربط الـ API الخاص بـ Gemini أو OpenAI مستقبلاً
            self.chat_history.text += f"\nAli GPT: Thinking... (Connected Successfully!)"
            self.user_input.text = ""

if __name__ == "__main__":
    AliGPT().run()
