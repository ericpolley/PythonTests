import pyglet

# Create the window
window = pyglet.window.Window(900, 600)

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

# Set up the menu movement flag
menu_movement_flag = False


@window.event
def on_draw():
    window.clear()
    for label in main_menu_labels:
        label.draw()
    cursor.draw()


@window.event
def on_key_press(symbol, modifiers):
    global menu_index
    global menu_movement_flag

    if symbol == pyglet.window.key.UP:
        if menu_index > 0:
            menu_index -= 1
        else:
            menu_index = len(main_menu_labels) - 1
        menu_movement_flag = True
    elif symbol == pyglet.window.key.DOWN:
        if menu_index < len(main_menu_labels) - 1:
            menu_index += 1
        else:
            menu_index = 0
        menu_movement_flag = True


def update_cursor(dt):
    global menu_movement_flag

    if menu_movement_flag:
        cursor.y = main_menu_labels[menu_index].y
        menu_movement_flag = False


pyglet.clock.schedule_interval(update_cursor, 1/60.0)

pyglet.app.run()
