"""
This is a sample program to show how to draw using the Python programming
language and the Arcade library.
"""

# Import the "arcade" library
import arcade

# Open up a window.
# From the "arcade" library, use a function called "open_window"
# Set the window title to "Drawing Example"
# Set the dimensions (width and height)
arcade.open_window(600, 600, "Drawing Example")

# Set the background color
arcade.set_background_color(arcade.csscolor.SKY_BLUE)

# Get ready to draw
arcade.start_render()

# Draw a rectangle
# Left of 0, right of 599
# Top of 300, bottom of 0
arcade.draw_lrtb_rectangle_filled(0, 599, 300, 0, arcade.csscolor.BLUE)

# Draw waves
arcade.draw_arc_filled(300, 280, 60, 100, arcade.csscolor.BLUE, 0, 180)
arcade.draw_arc_filled(390, 280, 60, 100, arcade.csscolor.BLUE, 0, 180)
arcade.draw_arc_filled(480, 280, 60, 100, arcade.csscolor.BLUE, 0, 180)
arcade.draw_arc_filled(210, 280, 60, 100, arcade.csscolor.BLUE, 0, 180)
arcade.draw_arc_filled(110, 280, 60, 100, arcade.csscolor.BLUE, 0, 180)

# Draw a boat

arcade.draw_line(300, 320, 300, 450, arcade.color.SIENNA, 6)
arcade.draw_rectangle_filled(300, 320, 200, 60, arcade.csscolor.SIENNA)
arcade.draw_arc_filled(300, 400, 60, 100, arcade.csscolor.WHITE_SMOKE, 0, 180)

# Draw a sun
arcade.draw_circle_filled(500, 550, 40, arcade.color.YELLOW)

# Rays to the left, right, up, and down
arcade.draw_line(500, 550, 400, 550, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 600, 550, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 500, 450, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 500, 650, arcade.color.YELLOW, 3)

# Diagonal rays
arcade.draw_line(500, 550, 550, 600, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 550, 500, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 450, 600, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 450, 500, arcade.color.YELLOW, 3)

# Draw Fish
arcade.draw_ellipse_filled(200, 150, 350, 200, arcade.csscolor.DARK_GREEN)
arcade.draw_arc_filled(300, 340, 150, 350, arcade.csscolor.DARK_GREEN, 90, 180)


#Finish Drawing
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()