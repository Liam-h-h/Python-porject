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
arcade.set_background_color(arcade.color.SUNSET_ORANGE)

# Get ready to draw
arcade.start_render()

# Draw Sun
arcade.draw_arc_filled(300, 340, 180, 180, arcade.color.YELLOW_ORANGE, -180, 180)

# Draw a rectangle
# Left of 0, right of 599
# Top of 300, bottom of 0
arcade.draw_lrtb_rectangle_filled(0, 599, 300, 0, arcade.color.YALE_BLUE)



# Draw a Boat
arcade.draw_arc_filled(250, 250, 155, 60, arcade.csscolor.DARK_RED, 180, 360)
arcade.draw_rectangle_filled(253, 300, 6, 100, arcade.csscolor.BLACK)
arcade.draw_triangle_filled(250,250,180,250,250,350, arcade.csscolor.WHITE)
arcade.draw_triangle_filled(255,250,320,250,255,350, arcade.csscolor.WHITE)



#Finish Drawing
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()