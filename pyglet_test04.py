import pyglet

# Create the window
window = pyglet.window.Window(800, 600)

# Create the main menu labels
start_game_label = pyglet.text.Label(
    'Start Game', font_size=36, x=window.width//2, y=window.height//2, anchor_x='center', anchor_y='center')
options_label = pyglet.text.Label('Options', font_size=36, x=window.width //
                                  2, y=window.height//2 - 50, anchor_x='center', anchor_y='center')
exit_label = pyglet.text.Label('Exit', font_size=36, x=window.width //
                               2, y=window.height//2 - 100, anchor_x='center', anchor_y='center')

# Create a list of the main menu labels
main_menu_labels = [start_game_label, options_label, exit_label]

# Set up the cursor
cursor = pyglet.text.Label('>', font_size=36, x=window.width //
                           2 - 50, y=window.height//2, anchor_x='right', anchor_y='center')

# Set up the menu index
menu_index = 0


@window.event
def on_draw():
    window.clear()
    for label in main_menu_labels:
        label.draw()
    cursor.draw()


@window.event
def on_key_press(symbol, modifiers):
    global menu_index

    if symbol == pyglet.window.key.UP:
        menu_index = (menu_index - 1) % len(main_menu_labels)
    elif symbol == pyglet.window.key.DOWN:
        menu_index = (menu_index + 1) % len(main_menu_labels)

    cursor.y = main_menu_labels[menu_index].y


pyglet.app.run()
