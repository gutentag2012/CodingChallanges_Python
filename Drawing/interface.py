import time
from ctypes import windll
from tkinter import *


class Interface:
    def __init__(self, title, width, height, background_color, draw_color):
        windll.shcore.SetProcessDpiAwareness(1)

        self.title, self.width, self.height = title, width, height
        self.background_color, self.draw_color = background_color, draw_color
        self.translation_x, self.translation_y = 0, 0
        self.mouse_clicked, self.mouse_hovered = False, False
        self.on_click = None
        self.on_key_press = None
        self.on_mouse_enter, self.on_mouse_leave, self.on_mouse_move = None, None, None

        self.last_frame = time.time()
        self.show_frames = False

        self.root = Tk()
        self.root.title(self.title)
        self.root.geometry(f"{self.width}x{self.height}")
        self.canvas = Canvas(self.root, width=self.width, height=self.height, background=self.background_color)
        self.canvas.pack()

        self.root.bind("<Motion>", self.motion)
        self.root.bind("<Button-1>", self.start_click)
        self.root.bind("<ButtonRelease-1>", self.end_click)
        self.root.bind("<Enter>", self.mouse_enter)
        self.root.bind("<Leave>", self.mouse_leave)

    def key_press(self, event):
        if self.on_key_press:
            self.on_key_press(event.char)

    def motion(self, event):
        if self.on_mouse_move:
            self.on_mouse_move(event.x, event.y)

    def mouse_enter(self, event):
        self.mouse_hovered = True
        if self.on_mouse_enter:
            self.on_mouse_enter()

    def mouse_leave(self, event):
        self.mouse_hovered = False
        if self.on_mouse_leave:
            self.on_mouse_leave()

    def start_click(self, event):
        self.mouse_clicked = True
        if self.on_click:
            self.on_click(event.x, event.y)

    def end_click(self, event):
        self.mouse_clicked = False

    def run(self):
        self.loop()
        self.root.mainloop()

    def loop(self):
        self.canvas.delete("all")

        self.draw()

        if self.show_frames:
            now = time.time()
            frames = 1 / (now - self.last_frame)
            self.last_frame = now
            self.canvas.create_text(self.width - 30, 20, font=("Roboto", 8), fill=self.draw_color,
                                    text=f"{int(round(frames, 4))}")

        self.root.after(1, self.loop)
        pass

    def translate(self, x, y):
        self.translation_x = x
        self.translation_y = y

    def draw(self):
        pass

    def line(self, x, y, x2, y2):
        self.canvas.create_line(
            x + self.translation_x,
            y + self.translation_y,
            x2 + self.translation_x,
            y2 + self.translation_y,
            fill=self.draw_color
        )

    def ellipse(self, x, y, width, height):
        self.canvas.create_oval(
            x - width / 2 + self.translation_x,
            y - height / 2 + self.translation_y,
            x + width / 2 + self.translation_x,
            y + height / 2 + self.translation_y,
            fill=self.draw_color,
            outline=self.draw_color
        )
