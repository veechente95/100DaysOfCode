
import colorgram

rgb_colors = []
colors = colorgram.extract("Super_Mario64.jpg", 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

print(rgb_colors)

color_list = [(226, 4, 35), (249, 229, 200), (217, 231, 250), (109, 172, 230), (53, 93, 173), (242, 251, 249), (220, 163, 72), (238, 210, 90), (26, 134, 63), (153, 172, 54), (157, 89, 46), (73, 111, 194), (252, 236, 240), (29, 14, 4), (16, 34, 143), (88, 172, 59), (11, 19, 47), (233, 56, 80), (163, 184, 234), (249, 163, 154), (3, 24, 9), (177, 47, 76), (225, 123, 136), (127, 183, 128), (210, 88, 60), (250, 152, 160), (64, 9, 42), (173, 22, 12), (249, 222, 1), (89, 79, 17)]