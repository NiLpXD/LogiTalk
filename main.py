from customtkinter import*
import threading
import socket
import base64
import io
from PIL import Image
from tkinter import filedialog

class MainWindow(CTk):
    def __init__(self, name = None, client_socket: socket.socket = None):
        super().__init__()
        self.geometry('800x600')
        self.title('Logitalk')

        self.chat_field = CTkScrollableFrame(self)
        self.chat_field.place(x = 0, y = 0)

        self.message_entry = CTkEntry(self, placeholder_text = 'Введіть повідомлення', height = 40)
        self.message_entry.place(x=0,y=0)

        self.send_btn = CTkButton(self, text = '✈', width = 50, height = 40)
        self.send_btn.place(x=0,y=0)

        self.send_img_btn = CTkButton(self, text = '📂', width = 50, height = 40)
        self.send_img_btn.place(x=0,y=0)

        self.file_name = None
        self.image_to_send = CTkLabel(self, text = '')
        self.image_to_send.bind('<Button-1>', self.remove_image)

        self.adaptation()

    def remove_image(self, e=None):
        ...

    def adaptation(self):
        window_width = self.winfo_width()
        window_height = self.winfo_height()
        max_message_entry_width = window_width - (self.send_btn.winfo_width()+self.send_img_btn.winfo_width()) - 10
        self.message_entry.place(y=window_height-self.message_entry.winfo_height())
        self.message_entry.configure(width=max_message_entry_width)
        self.send_img_btn.place(
            x = self.message_entry.winfo_width()+5,
            y = window_height-self.send_img_btn.winfo_height()
        )
        self.send_btn.place(
            x = window_width - self.send_btn.winfo_width(),
            y = window_height-self.send_img_btn.winfo_height()
        )
        self.chat_field.configure(
            width = window_width-20,
            height = window_height-self.message_entry.winfo_height()-10
        )

        if self.file_name:
            self.image_to_send.configure(
                image=CTkImage(
                    Image.open(self.file_name),
                    size=(100,200)
                )
            )
        self.image_to_send.place(
            x=20,
            y= self.message_entry.winfo_y() - 100
        )
        
        self.after(100, self.adaptation)
        self.add_message(message 'Ласкаво просимо до чату!', author = "SYSTEM")

        try:
            sock = socket(AF_INET, SOCK_STREAM)
            sock.connect(('localhost', 8080))

            hello = f"TEXT@{self.username}@[SYSTEM] {self.username} приєднався(лась) до чату!\n"
            sock.send(hello.encode('utf-8'))
            self.sock = sock

            threading.Thread(target = self.recv_message, daemon = True).start()
        except Exception as e:
            print(f'Не вдалося підключитися до сервера: {e}')
            self.sock = None
    def load_main_avatar(self):
        try:
            image_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "user-avatar.png")
            self.user_avatar = self.create_circular_avatar(image_path, size:(60,60))
        except Exception as e:
            print(f'Завантаження головного аватара: {e}')
            self.user_avatar = self.create_circulat_avatar(image_path: None, size: (60,60), initial: 'U')
    def load_chat_avatars(self):
        try:
            user_image_path = os_path.join(os.path.dirname(os.path.abspath(__file__)),"user-avatar.png")
            self.user_avatar_chat = self.create_circular_avatar(user_image_path, size:(40, 40))
        except Exception as e:
            print(f'Помилка завантаження аватара користувача для чату: {e}')
            self.user_avatar_chat = self.create_circular_avatar(image_path: None, size:(40,40), initial: "U")

        try:
            system_image_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "system-avatar.png")
            self.system_avatar_chat = self.create_circular_avatar(image_path: None, size: (40,40), initial: "S")

    @staticmethod
    def create_circular_avatar(image_path, size" {_getlmen_}, initial: str= '?'):
        ...
window = MainWindow()
window.mainloop()