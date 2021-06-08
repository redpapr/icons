import numpy

from PIL import Image



width = 800
height = 800

data = numpy.zeros((height, width, 3), dtype=numpy.uint8)

red = [193, 10, 10]
white = [255, 240, 240]
grey = [180, 180, 180]

red_width = 200
padding_left = 30
padding_right = 40
padding_top = 50
padding_bottom = 100

for x in range(0, width):
	for y in range(0, height):
		if x < red_width:
			data[y][x][0] = red[0]
			data[y][x][1] = red[1]
			data[y][x][2] = red[2]
		else:
			x1 = red_width + padding_left
			x2 = width - padding_right
			y1 = padding_top
			y2 = height - padding_bottom
			if x > x1 and x < x2 and y > y1 and y < y2 and (y % 50) > 25:
				data[y][x][0] = grey[0]
				data[y][x][1] = grey[1]
				data[y][x][2] = grey[2]
			else:
				data[y][x][0] = white[0]
				data[y][x][1] = white[1]
				data[y][x][2] = white[2]

img = Image.fromarray(data)
img.save("redpapr.png")


