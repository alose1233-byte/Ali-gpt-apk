from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
import requests

class AliGPTApp(App):
    def build(self):
        self.title = "Ali GPT v1.0"
        Window.clearcolor = (0.05, 0.05, 0.1, 1)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        # العنوان
        layout.add_widget(Label(text="🚀 ALI GPT SMART AI", font_size='30sp', color=(0, 1, 1, 1), size_hint_y=0.1))
        
        # الشات
        self.chat_label = Label(text="أهلاً بك! أنا ذكاء علي الاصطناعي..", size_hint_y=None, halign='right', valign='top', text_size=(400, None))
        self.chat_label.bind(texture_size=self.chat_label.setter('size'))
        scroll = ScrollView(size_hint_y=0.7)
        scroll.add_widget(self.chat_label)
        layout.add_widget(scroll)

        # الإدخال
        input_area = BoxLayout(size_hint_y=0.2, spacing=10)
        self.user_input = TextInput(hint_text="اكتب هنا...", multiline=False)
        send_btn = Button(text="إرسال", background_color=(0, 0.7, 1, 1), size_hint_x=0.3)
        send_btn.bind(on_press=self.ask_ai)
        input_area.add_widget(self.user_input)
        input_area.add_widget(send_btn)
        layout.add_widget(input_area)
        return layout

    def ask_ai(self, instance):
        user_text = self.user_input.text
        if not user_text: return
        self.chat_label.text += f"\n\nأنت: {user_text}"
        self.user_input.text = ""
        
        api_key = "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"
        url = "https://api.groq.com/openai/v1/chat/completions"
        headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
        data = {"model": "mixtral-8x7b-32768", "messages": [{"role": "user", "content": user_text}]}
        
        try:
            response = requests.post(url, json=data, headers=headers)
            if response.status_code == 200:
                answer = response.json()['choices'][0]['message']['content']
                self.chat_label.text += f"\n\nAli GPT: {answer}"
            else:
                self.chat_label.text += f"\n\n❌ خطأ بالاتصال"
        except:
            self.chat_label.text += f"\n\n❌ حدث خطأ"

if __name__ == "__main__":
    AliGPTApp().run()
