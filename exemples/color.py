from pratik.color import Color

# =-= =-= =-= =< How Init Color >= =-= =-= =-= #

color = Color(1.0, 0.0, 0.0)
print("color = Color(1.0, 0.0, 0.0) | color:", color)
color = Color.by_hsv(0.33, 1.0, 1.0)
print("color = Color.by_hsv(0.33, 1.0, 1.0) | color:", color)
color = Color.by_hsl(0.66, 1.0, 0.5)
print("color = Color.by_hsl(0.66, 1.0, 0.5) | color:", color)
color = Color.by_rgb255(255, 0, 255)
print("color = Color.by_rgb255(255, 0, 255) | color:", color)
color = Color.by_hexadecimal("#FF0000")
print("color = Color.by_hexadecimal('#FF0000') | color:", color)

# =-= =-= =-= =< Concatenating the Color >= =-= =-= =-= #

print("(str):", str(Color(1.0, 0.5, 0)))
print("(int):", int(Color.by_hexadecimal("#00FF00")))

# =-= =-= =-= =< Color Properties >= =-= =-= =-= #

gray = Color(0.5, 0.5, 0.5)
dark_gray = Color(0.1, 0.1, 0.1)  # dark gray
red = Color(1.0, 0.0, 0.0)  # red
green = Color(0.0, 1.0, 0.0)  # green
blue = Color(0.0, 0.0, 1.0)  # blue
orange = Color(1.0, 0.5, 0.0)
white = Color(1.0, 1.0, 1.0)  # white
color = Color(0.8, 0.5, 0.4)  # warm

print("Color is warm:", color)
print("Red in 255 scale:", color.red255)
print("Hexadecimal:", color.hexadecimal)
print("Max:", color.max)  # (Red is strongest)
print("Min:", color.min)  # (Blue is weakest)

print("Grey range:", gray.range)  # no color, just gray

print("Warm range:", color.range)  # 0.8 - 0.4 = 0.4 → moderately vivid

print("Orange range:", orange.range)  # 1.0 - 0.0 = 1.0 → vivid

print("The biggest value:", color.value)
print("The lightness", color.lightness)  # (0.8 + 0.4)/2 = 0.6 → medium lightness

print("Dark grey lightness", dark_gray.lightness)  # 0.1 → dark

print("Red hue", color.hue)

print("Green hue", color.hue)

print("Vlue hue", color.hue)

print("Red saturation:", red.saturation_value)  # full color
print("Color saturation:", color.saturation_value)
print("White saturation:", white.saturation_value)  # no color

print("Color saturation lightness:", color.saturation_lightness)  # quite saturated
print("Grey saturation lightness:", gray.saturation_lightness)

print("Color HSL:", tuple(round(v, 10) for v in color.hsl))
print("Red HSL:", red.hsl)