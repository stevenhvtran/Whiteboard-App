import socket

TCP_IP = '118.138.101.97'
TCP_PORT = 50000
BUFFER_SIZE = 1024*4

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

def main():
    import tkinter as tk
    import threading
    import pickle
    global full_line, line_segments, pressed

    pressed = False
    line_segments = []
    full_line = []

    def break_line():
        global line_segments, pressed
        while True:
            while pressed is True:
                if len(line_segments) > 2:
                    w.create_line(line_segments, tag='temp', smooth=1)
                    line_segments = [line_segments[2]]
            line_segments = []

    def draw_msg():
        while True:
            message = s.recv(BUFFER_SIZE)
            if len(message) > 0:
                w.create_line(pickle.loads(message), smooth=1)

    draw_thread = threading.Thread(target=break_line)
    draw_thread.start()
    receive_thread = threading.Thread(target=draw_msg)
    receive_thread.start()


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
        global pressed, line_segments, full_line
        pressed = False
        w.create_line(full_line, smooth=1)
        w.delete('temp')
        s.send(pickle.dumps(full_line))
        full_line = []

    root.bind('<ButtonPress-1>', draw)
    root.bind('<ButtonRelease-1>', stop_drawing)
    root.bind('<B1-Motion>', get_mouse)
    tk.mainloop()


s.send(b'Hello')
reply = s.recv(BUFFER_SIZE).decode()
print(reply)
if reply == 'Handshake successful':
    main()

s.close()
