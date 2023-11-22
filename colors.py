# Define color tuples
Color_Off = (0,0,0)
Color_Full = (255,255,255)

Color_White = (22,16,8)		# This can be even dimmer but the color is good

Color_Red = (30,0,0)
Color_Green = (0,30,0)
Color_Blue = (0,0,30)

Color_Orange = (44,8,0)
Color_Purple = (44,0,8)

Color_Pink = (66,16,15)

def get_alternating_colors(color_list, num_pixels):
    pixels = []
    
    colors = len(color_list)
    current_color = 0
    
    for i in range(num_pixels):
        pixels.append(color_list[current_color % colors])
        current_color += 1
    
    return pixels


def standard_colors(num_pixels):
    return get_alternating_colors([Color_White], num_pixels)


def xmas_colors(num_pixels):
    return get_alternating_colors([Color_Red, Color_Green], num_pixels)


def chaunakah_colors(num_pixels):
    return get_alternating_colors([Color_Blue, Color_Blue, Color_White], num_pixels)


def halloween_colors(num_pixels):
    return get_alternating_colors([Color_Orange, Color_Purple], num_pixels)


def valentines_colors(num_pixels):
    return get_alternating_colors([Color_Pink], num_pixels)


# St. Paddy's Day
# New Year's Eve (ball drop animation of some kind)
# 4th of July, also memorial day
# Cinco de mayo
