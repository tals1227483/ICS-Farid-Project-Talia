import kivy  
import os
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.utils import escape_markup
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.image import Image
from kivy.graphics import Rectangle
from kivy.core.window import Window
from kivy.uix.video import Video
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.graphics import Rectangle, Color
from kivy.clock import Clock
from kivy.uix.colorpicker import ColorPicker
from kivy.app import App
from kivy.metrics import dp
from kivy.uix.spinner import Spinner
from kivy.uix.label import Label
from kivy.uix.videoplayer import VideoPlayer
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.popup import Popup
from kivy.uix.carousel import Carousel


class MainMenuScreen(Screen):
    """
    The main menu screen of the application.
    """
    def __init__(self, **kwargs):
        super(MainMenuScreen, self).__init__(**kwargs)
        self.layout = FloatLayout()

        # Set the background color.
        with self.canvas:
            self.rect = Rectangle(size = Window.size, source='resources/blue.png')

        # Create an Image widget for the title.
        title_image = Image(source = 'resources/png.png', allow_stretch = True, keep_ratio = False,
                            size_hint=(None, None), size=(Window.width * 0.5, Window.height * 0.4),
                            pos_hint={'center_x': 0.5, 'center_y': 0.9})

        # Create Image widgets for the side images.
        left_image = Image(source ='resources/collage3.png', allow_stretch = True, keep_ratio = False,
                           size_hint = (None, None), size = (Window.width * 0.2, Window.height),
                           pos_hint = {'x': 0, 'y': 0})
        right_image = Image(source = 'resources/collage1.png', allow_stretch = True, keep_ratio = False,
                            size_hint = (None, None), size = (Window.width * 0.2, Window.height),
                            pos_hint = {'right': 1, 'y': 0})

        button_box = BoxLayout(orientation = 'vertical', spacing = 20, size_hint = (0.3, 0.6),
                               pos_hint = {'center_x': 0.5, 'center_y': 0.5})

        self.g_name = Button(text ='Blood Glucose', font_size = '20sp', size_hint = (1, 0.25),
                             on_release=self.go_to_blood_glucose)
        self.e_name = Button(text ='Eat', font_size = '20sp', size_hint=(1, 0.25), on_release=self.go_to_eat)
        self.h_name = Button(text ='Help', font_size = '20sp', size_hint=(1, 0.25), on_release=self.go_to_help)
        
        # Set button background colors.
        self.g_name.background_normal = ''
        self.g_name.background_color = (1, 0.41, 0.51, 1) 
        self.e_name.background_normal = ''
        self.e_name.background_color = (1, 0.91, 0.31, 1)  
        self.h_name.background_normal = ''
        self.h_name.background_color = (0, 1.5, 0.91, 1)  
        
        button_box.add_widget(self.g_name)
        button_box.add_widget(self.e_name)
        button_box.add_widget(self.h_name)

        self.layout.add_widget(title_image)
        self.layout.add_widget(left_image)
        self.layout.add_widget(right_image)
        self.layout.add_widget(button_box)

        self.add_widget(self.layout)

    def go_to_blood_glucose(self, instance):
        self.manager.current = 'blood_glucose'

    def go_to_eat(self, instance):
        self.manager.current = 'eat'

    def go_to_help(self, instance):
        self.manager.current = 'help'

class NewPage(Screen):
    def __init__(self, question_text='', **kwargs):
        super(NewPage, self).__init__(**kwargs)
        self.question_text = question_text
        self.layout = BoxLayout(orientation = 'vertical', spacing = 10, padding = 10)

class BloodGlucosePage(Screen):
    def __init__(self, **kwargs):
       super(BloodGlucosePage, self).__init__(**kwargs)
       self.layout = GridLayout(cols = 3, spacing = 60, padding = 10)

       back_button = Button(text='Back', size_hint = (0.1, 0.1), background_color = (1, 0.06, 0.8, 1),
                            on_release = self.go_to_main_menu)

       # Set the button color to pastel pink.
       pastel_pink = (1.3, 0.9, 1.7, 1.3)
       back_button.background_color = pastel_pink
       # Adjust the font size of the button.
       back_button.font_size = '16sp'  
        # Position the button in the top left corner.
       back_button.pos_hint = {'top': 1, 'left': 1}  
      
       # Create the header row.
       alarm_table = GridLayout(cols = 3, spacing = 10, padding = 10, size_hint = (1, 0.6))
       alarm_table.bind(minimum_height = alarm_table.setter('height'))
       header_button1 = Button(text = 'Time of day', size_hint = (0.5, 0.4))
       header_button1.background_color = (0.63, 0.88, 0.92, 1)  
       alarm_table.add_widget(header_button1)

       header_button2 = Button(text='Blood Glucose Level', size_hint = (0.5, 0.4))
       header_button2.background_color = (0.63, 0.88, 0.92, 1)  
       alarm_table.add_widget(header_button2)

       header_button3 = Button(text='How are you feeling?', size_hint = (0.5, 0.4))
       header_button3.background_color = (0.63, 0.88, 0.92, 1)  
       alarm_table.add_widget(header_button3)

       # Create the table rows.
       alarm_times = []
       for hour in range(24):
           for minute in range(0, 60, 30):
               time_string = f"{hour:02d}:{minute:02d}"
               alarm_times.append(time_string)

       for _ in range(7):
           spinner = Spinner(text='Select Time', values = alarm_times)
           spinner.background_color = (1, 0.08, 0.58, 1)  
           alarm_table.add_widget(spinner)

           text_input1 = TextInput()
           text_input1.background_color = (0.7, 1, 1, 1)  
           alarm_table.add_widget(text_input1)

           text_input2 = TextInput()
           text_input2.background_color = (0.7, 0.9, 1, 1)  
           alarm_table.add_widget(text_input2)

       self.layout.add_widget(back_button)
       self.layout.add_widget(alarm_table)

       # Set the background image.
       background_image = Image(source='resources/purple.png', 
                                allow_stretch=True, keep_ratio=False)
       self.add_widget(background_image)

       self.add_widget(self.layout)

    def go_to_main_menu(self, instance):
       self.manager.current = 'main_menu'


class EatPage(Screen):
    def __init__(self, **kwargs):
        super(EatPage, self).__init__(**kwargs)
        anchor_layout = AnchorLayout()
        self.layout = FloatLayout()

        # Set the background color.
        with self.canvas:
            self.rect = Rectangle(size=Window.size, source='resources/eat.png')

        # Create the image widget for the title.
        title_image = Image(source='resources/til.png', size_hint = (0.9, 0.2),
                            pos_hint={'center_x': 0.5, 'top': 0.9})
        self.layout.add_widget(title_image)

        # Create the grid layout for the images and buttons.
        image_grid = GridLayout(cols = 2, spacing = [400, 200], size_hint = (0.8, None))

        # Add the images and buttons to the grid layout.
        for i in range(8):
            image_path = f"resources/image{i+1}.png"
            image = Image(source = image_path, size_hint = (None, None), size = (200, 200))
            button = Button(text = f"Click me {i+1}", size_hint = (None, None), 
                            size = (100, 100), background_color = (0, 0.8, 0.5, 1), font_size = 20)
            layout = BoxLayout(orientation = 'horizontal', spacing = 10)
            layout.add_widget(image)
            layout.add_widget(button)
            
            # Create the label widget for displaying the comment.
            comment_label = Label(text = '', size_hint = (None, None), size = (200, 30))
            layout.add_widget(comment_label)
            
            button.bind(on_release = lambda button = button, image = image, comment_label = comment_label: 
                        self.show_comment_popup(button, image, comment_label))
            image_grid.add_widget(layout)

        # Add the image grid layout to the scroll view.
        scroll_view = ScrollView(size_hint = (0.6, 1), pos_hint={'center_x': 0.5, 'center_y': 0.2},
                                 do_scroll = ('x', 'y'))
        scroll_view.add_widget(image_grid)

        self.layout.add_widget(scroll_view)

        # Create the back button.
        back_button = Button(text = 'Back', size_hint = (0.2, 0.1),
                             pos_hint={'x': 0, 'top': 1},
                             background_normal = '',
                             background_color = (0.8, 0.2, 0.2, 1),
                             on_release=self.go_to_main_menu)
        self.layout.add_widget(back_button)

        anchor_layout.add_widget(self.layout)
        self.add_widget(anchor_layout)

    def on_enter(self):
        # Schedule the scroll after the UI has finished updating.
        Clock.schedule_once(self.scroll_to_top)

    def scroll_to_top(self, dt):
        # Scroll to the top of the ScrollView.
        scroll_view = self.layout.children[0]
        scroll_view.scroll_y = 1

    def go_to_main_menu(self, instance):
        self.manager.current = 'main_menu'

    def show_comment_popup(self, button, image, comment_label):
        # Create the popup.
        popup = Popup(title='Enter Comment', size_hint = (0.6, 0.3), auto_dismiss = False)

        # Create the text input box.
        text_input = TextInput(size_hint = (0.8, 0.6), multiline = False)

        # Create the post button.
        post_button = Button(text = 'Post', size_hint = (0.2, 0.4))

        def post_button_callback(instance):
            self.post_comment(text_input.text, button, image, comment_label)
            popup.dismiss()

        post_button.bind(on_release = post_button_callback)

        # Create the layout for the popup content.
        layout = BoxLayout(orientation = 'vertical')
        layout.add_widget(text_input)
        layout.add_widget(post_button)

        popup.content = layout
        popup.open()

    def post_comment(self, comment, button, image, comment_label):
        # Logic for posting the comment and updating the UI.
        # Update the comment label with the posted comment.
        comment_label.text = comment
        comment_label.color = (0, 0, 0, 1)






class HelpPage(Screen):
    def __init__(self, **kwargs):
        super(HelpPage, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation = 'vertical', spacing = 10, padding =10)

        # Set the background color.
        with self.canvas:
            self.rect = Rectangle(size = Window.size, source = 'resources/blue.png')

        back_button = Button(text='Back', size_hint = (0.2, 0.1), pos_hint ={ 'x': 0, 'top': 1},
                             background_normal = '', background_color = (0.8, 0.2, 0.2, 1), on_release = self.go_to_main_menu)
        self.layout.add_widget(back_button)

        post_button = Button(text = 'Post', size_hint = (0.2, 0.1), pos_hint = {'center_x': 0.5},
                             background_normal = '', background_color = (0.3, 0.8, 0.4, 1), on_release = self.post_question)
        self.layout.add_widget(post_button)

        self.help_text_input = TextInput(multiline = True, hint_text = 'Your question goes here')
        self.layout.add_widget(self.help_text_input)

        self.help_scroll_view = ScrollView()
        self.help_box = BoxLayout(orientation = 'vertical', spacing = 10, padding = 10, size_hint_y = None)
        self.help_scroll_view.add_widget(self.help_box)
        self.layout.add_widget(self.help_scroll_view)

        self.add_widget(self.layout)

        # A list to store the posted questions.
        self.posted_questions = []

        # Bind on_enter event to load_questions method.
        self.bind(on_enter = self.load_questions)

    def go_to_main_menu(self, instance):
        self.manager.current = 'main_menu'

    def post_question(self, instance):
        try:
            question = self.help_text_input.text
            self.help_text_input.text = ''  # Clear the text input.

            # Create a new layout for the posted question and input field.
            question_layout = BoxLayout(orientation='vertical', spacing = 10, size_hint = (1, None))

            # Create a new button for the posted question.
            question_button = Button(text = question, size_hint = (1, None), height = dp(50))
            question_button.bind(on_release = lambda btn: self.go_to_new_page(question))

            # Create a new text input for user input.
            text_input = TextInput(multiline = True, hint_text = 'Your input goes here', 
                                   size_hint = (1, None), height = dp(100))

            # Create a new button to post user input.
            post_button = Button(text='Post', size_hint = (0.2, 0.1), pos_hint = {'center_x': 0.5},
                                 background_normal = '', background_color = (0.3, 0.8, 0.4, 1),
                                 on_release = lambda btn: self.post_user_input(question, text_input.text))

            # Add the button, text input, and post button to the question layout.
            question_layout.add_widget(question_button)
            question_layout.add_widget(text_input)
            question_layout.add_widget(post_button)

            # Add the question layout to the help_box.
            self.help_box.add_widget(question_layout)

            self.posted_questions.append(question)
            self.save_questions()

            self.help_scroll_view.scroll_y = 0

        except Exception as e:
            print(f"Error: {str(e)}")

    def go_to_new_page(self, question_text):
        app = App.get_running_app()
        new_screen = NewPage(question_text=question_text)
        app.root.current = 'new_page'
        app.root.transition.direction = 'left'

    def load_questions(self, *args):
        filename = 'posted_questions.txt'
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                self.posted_questions = [line.strip() for line in file]

        # Clear the help_box.
        self.help_box.clear_widgets()

        # Display the loaded questions in the help_box.
        for question in self.posted_questions:
            comment_button = Button(text = question, size_hint = (1, None), height = dp(50))
            comment_button.bind(on_release = lambda btn: self.go_to_new_page(question))
            self.help_box.add_widget(comment_button)

            text_input = TextInput(multiline=True, hint_text='Your input goes here')
            self.help_box.add_widget(text_input)

        self.help_scroll_view.scroll_y = 0

    def save_questions(self):
        filename = 'posted_questions.txt'
        with open(filename, 'w') as file:
            for question in self.posted_questions:
                file.write(question + '\n')

    def post_user_input(self, question, user_input):
        print(f"Posted question: {question}")
        print(f"User input: {user_input}")
        # You can process the posted question and user input here as needed.


class NewPage(Screen):
    def __init__(self, question_text, **kwargs):
        super(NewPage, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation = 'vertical', spacing = 10, padding = 10)

        back_button = Button(text = 'Back', size_hint = (0.2, 0.1), 
                             pos_hint = {'x': 0, 'top': 1},
                             background_normal='', background_color=(0.8, 0.2, 0.2, 1), 
                             on_release=self.go_to_help_page)
        self.layout.add_widget(back_button)

        question_label = Label(text = question_text)
        self.layout.add_widget(question_label)

        self.comment_scroll_view = ScrollView()
        self.comment_box = BoxLayout(orientation = 'vertical', spacing = 10, padding = 10, size_hint_y = None)
        self.comment_scroll_view.add_widget(self.comment_box)
        self.layout.add_widget(self.comment_scroll_view)

        self.comment_input = TextInput(multiline = True, hint_text = 'Your input goes here')
        self.layout.add_widget(self.comment_input)

        post_button = Button(text = 'Post', size_hint = (0.2, 0.1), pos_hint = {'center_x': 0.5},
                             background_normal='', background_color=(0.3, 0.8, 0.4, 1), on_release = self.post_comment)
        self.layout.add_widget(post_button)

        self.add_widget(self.layout)

        # A list to store the posted comments.
        self.posted_comments = []

        # Bind on_enter event to load_comments method.
        self.bind(on_enter=self.load_comments)

    def go_to_help_page(self, instance):
        self.manager.current = 'help_page'

    def post_comment(self, instance):
        comment = self.comment_input.text
        if comment:
            self.comment_input.text = ''  # Clear the text input.

            # Create a new label for the posted comment.
            comment_label = Label(text = comment, size_hint = (1, None), height = dp(50))
            self.comment_box.add_widget(comment_label)

            self.posted_comments.append(comment)
            self.save_comments()

            self.comment_scroll_view.scroll_y = 0

    def load_comments(self, *args):
        filename = 'posted_comments.txt'
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                self.posted_comments = [line.strip() for line in file]

        # Clear the comment_box.
        self.comment_box.clear_widgets()

        # Display the loaded comments in the comment_box.
        for comment in self.posted_comments:
            comment_label = Label(text = comment, size_hint = (1, None), height = dp(50))
            self.comment_box.add_widget(comment_label)

        self.comment_scroll_view.scroll_y = 0

    def save_comments(self):
        filename = 'posted_comments.txt'
        with open(filename, 'w') as file:
            for comment in self.posted_comments:
                file.write(comment + '\n')

    


class HealthyLivingPage(Screen):
    def __init__(self, **kwargs):
        super(HealthyLivingPage, self).__init__(**kwargs)
        self.layout = FloatLayout()

        # Set the background color.
        with self.canvas:
            self.rect = Rectangle(size = Window.size, source = 'resources/pink.png')

        back_button = Button(text='Back', size_hint = (0.2, 0.1), pos_hint={'x': 0, 'top': 1},
                             background_normal = '', background_color = (0.8, 0.2, 0.2, 1), 
                             on_release = self.go_to_main_menu)
        self.layout.add_widget(back_button)

        # Add a video player.
        video_path = 'resources/diabetesvid.mp4'  # Replace with the actual path to your video file.
        video_player = VideoPlayer(source = video_path,
                                   size_hint = (0.8, 0.8), pos_hint = {'center_x': 0.5, 'center_y': 0.5},
                                   state='play')
        self.layout.add_widget(video_player)

        self.add_widget(self.layout)

    def go_to_main_menu(self, instance):
        self.manager.current = 'main_menu'


class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainMenuScreen(name = 'main_menu'))
        sm.add_widget(BloodGlucosePage(name = 'blood_glucose'))
        sm.add_widget(EatPage(name = 'eat'))
        sm.add_widget(HelpPage(name = 'help'))
        return sm


if __name__ == '__main__':
    MyApp().run()
