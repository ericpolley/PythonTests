import pyglet

# Create a window
window = pyglet.window.Window()

# Create a label to display the character's position
label = pyglet.text.Label(text="", x=10, y=10)

# Create a character sprite
character_image = pyglet.image.load("pig.png")
character = pyglet.sprite.Sprite(character_image)

# Set the initial position of the character
character.x = 100
character.y = 100

# Set the movement speed of the character
movement_speed = 5

# Define the movement keys
keys = pyglet.window.key.KeyStateHandler()
window.push_handlers(keys)


@window.event
def on_draw():
    # Clear the window
    window.clear()
    # Draw the character
    character.draw()
    # Update and draw the label
    label.text = f"Position: {character.x}, {character.y}"
    label.draw()


def update(dt):
    # Check if the left arrow key is pressed
    if keys[pyglet.window.key.LEFT]:
        character.x -= movement_speed
    # Check if the right arrow key is pressed
    if keys[pyglet.window.key.RIGHT]:
        character.x += movement_speed
    # Check if the up arrow key is pressed
    if keys[pyglet.window.key.UP]:
        character.y += movement_speed
    # Check if the down arrow key is pressed
    if keys[pyglet.window.key.DOWN]:
        character.y -= movement_speed


# Run the game loop at 60 FPS
pyglet.clock.schedule_interval(update, 1/60.0)

# Run the game
pyglet.app.run()
