import tkinter as tk
import threading

pressed = False
line_segments = []
full_line = []


def break_line():
    global line_segments, temp_line
    while True:
        while pressed is True:
            if len(line_segments) > 2:
                w.create_line(line_segments, tag='temp', smooth=1)
                line_segments = [line_segments[2]]
        line_segments = []


t = threading.Thread(target=break_line)
t.start()
lock = threading.Lock()

root = tk.Tk()
width = 1000
height = 1000
w = tk.Canvas(root, width=width, height=height)
w.pack()


def get_mouse(event):
    global line_segments
    line_segments.append((event.x, event.y))
    full_line.append((event.x, event.y))


def draw(a):
    global pressed
    pressed = True


def stop_drawing(a):
    global pressed, line_segments, full_line, temp_line
    pressed = False
    w.create_line(full_line, smooth=1)
    w.delete('temp')
    full_line = []


root.bind('<ButtonPress-1>', draw)
root.bind('<ButtonRelease-1>', stop_drawing)
root.bind('<B1-Motion>', get_mouse)
tk.mainloop()