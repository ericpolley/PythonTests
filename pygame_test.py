from tkinter import *
import pyglet

# create a window

window = pyglet.window.Window()
# create a label
label = pyglet.text.Label('Hello, World!',
                          font_name='Times New Roman',
                          font_size=36,
                          x=window.width//2, y=window.height//2,
                          anchor_x='center', anchor_y='center')

# create a drawing function


@window.event
def on_draw():
    window.clear()
    label.draw()


# run the game loop
pyglet.app.run()
