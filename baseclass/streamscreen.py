from kivy.uix.screenmanager import Screen
from kivymd.uix.button import MDRoundFlatButton
from kivymd.uix.label import MDLabel

from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture
from kivy.uix.camera import Camera

from vidgear.gears import NetGear
import cv2

options = {'flag': 0, 'copy': False, 'track': False, 'compression_format': '.jpg',
           'compression_param': [cv2.IMWRITE_JPEG_QUALITY, 60,
                                 cv2.IMWRITE_JPEG_PROGRESSIVE, True,
                                 cv2.IMWRITE_JPEG_OPTIMIZE, True, ]}

client = NetGear(address='192.168.20.33', port='5454', protocol='tcp', pattern=1,
                 receive_mode=True, logging=True, **options)


class KivyStream(Image):
    def __init__(self, fps, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_interval(self.update, 1.0 / fps)

    def update(self, dt):
        frame = client.recv()
        buf1 = cv2.flip(frame, 0)
        buf = buf1.tostring()
        image_texture = Texture.create(
            size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
        image_texture.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
        # display image from the texture
        self.texture = image_texture


class StreamScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.connection = False

        self.without_connection = MDLabel(text="Sin Conexión", font_style="H3",
                                          halign="center")
        self.stream = KivyStream(fps=60)
        self.web_cam = Camera(resolution=(1080, 720), play=False)
        self.camera_button = MDRoundFlatButton(text="Activar Cámara", size_hint=(.5, 1),
                                               on_release=self.camera_button_action)
        self.connect_button = MDRoundFlatButton(text="Conectar", size_hint=(.5, 1),
                                                on_release=self.streaming_connection)

        self.ids.stream_box.add_widget(self.without_connection)
        self.ids.buttons_box.add_widget(self.connect_button)
        self.ids.buttons_box.add_widget(self.camera_button)

    def streaming_connection(self, widget):
        if self.connection:
            self.ids.stream_box.remove_widget(self.stream)
            self.ids.stream_box.add_widget(self.without_connection)
            self.connect_button.text = "Conectar"
            self.connection = False
        else:
            self.ids.stream_box.remove_widget(self.without_connection)
            self.ids.stream_box.add_widget(self.stream)
            self.connect_button.text = "Desconectar"
            self.connection = True

    def camera_button_action(self, widget):
        if self.web_cam.play:
            self.ids.camera_box.clear_widgets()
            self.camera_button.text = "Activar Cámara"
        else:
            self.ids.camera_box.add_widget(self.web_cam)
            self.camera_button.text = "Desactivar Cámara"
        self.web_cam.play = not self.web_cam.play


