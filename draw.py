from display import *

def draw_line(x0, y0, x1, y1, screen, color):
	yD = y1 - y0
	xD = x1 - x0
	if (yD > 0):
		if (yD > xD):
			draw_lineQ2 (x0, y0, x1, y1, screen, color, False, False)
		else:
			draw_lineQ1 (x0, y0, x1, y1, screen, color, False, False)
	else:
		if (abs(yD) > abs(xD)):
			draw_lineQ7 (x0, y0, x1, y1, screen, color)
		else:
			draw_lineQ8 (x0, y0, x1, y1, screen, color)

def draw_lineQ1 (x0, y0, x1, y1, screen, color, flipH, flipV):
	x = x0
	y = y0
	A = y1 - y0
	B = -(x1- x0)
	d = 2 * A + B
	while(x <= x1):
		plot(screen, color, -x if flipV else x, -y if flipH else y)
		if (d > 0):
			y += 1
			d += 2 * B
		x += 1
		d += 2 * A

def draw_lineQ2 (x0, y0, x1, y1, screen, color, flipH, flipV):
	x = x0
	y = y0
	A = y1 - y0
	B = -(x1- x0)
	d = A + 2 * B
	while(y <= y1):
		plot(screen, color, -x if flipV else x, -y if flipH else y)
		if (d < 0):
			x += 1
			d += 2 * A
		y += 1
		d += 2 * B

def draw_lineQ7 (x0, y0, x1, y1, screen, color):
	draw_lineQ2 (x0, -y0, x1, -y1, screen, color, True, False)

def draw_lineQ8 (x0, y0, x1, y1, screen, color):
	draw_lineQ1 (x0, -y0, x1, -y1, screen, color, True, False)