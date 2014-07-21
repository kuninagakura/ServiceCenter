#!/usr/bin/python2.6
import time
import os
import sys
import pygame
import pygame.gfxdraw
import pygame.font
import color
import string

#-----------------------------------------------------------------------
# Define colors so clients need not import the color module.

from color import WHITE
from color import BLACK
from color import RED
from color import GREEN
from color import BLUE
from color import CYAN
from color import MAGENTA
from color import YELLOW
from color import DARK_RED
from color import DARK_GREEN
from color import DARK_BLUE
from color import GRAY
from color import DARK_GRAY
from color import LIGHT_GRAY
from color import ORANGE
from color import VIOLET
from color import PINK
from color import BOOK_BLUE
from color import BOOK_LIGHT_BLUE
from color import BOOK_RED
from color import CUP_RED
from color import CUP_GREEN
from color import CUP_YELLOW

#-----------------------------------------------------------------------
# Default Sizes and Values
_BORDER = 0
_DEFAULT_XMIN = 0.0
_DEFAULT_XMAX = 1.0
_DEFAULT_YMIN = 0.0
_DEFAULT_YMAX = 1.0
_DEFAULT_SIZE = 512
_DEFAULT_PEN_RADIUS = .002
_DEFAULT_PEN_COLOR = color.BLACK

_DEFAULT_FONT_FAMILY = 'Helvetica'
_DEFAULT_FONT_SIZE = 12

_xmin = None
_ymin = None
_xmax = None
_ymax = None

_fontFamily = _DEFAULT_FONT_FAMILY
_fontSize = _DEFAULT_FONT_SIZE

_width = _DEFAULT_SIZE
_height = _DEFAULT_SIZE
_penRadius = None
_penColor = _DEFAULT_PEN_COLOR
_keysTyped = []

#-----------------------------------------------------------------------
def createWindow(w=_DEFAULT_SIZE, h=_DEFAULT_SIZE):
	""" Draw a window"""
	global _surface
	global _width
	global _height
	if (w < 1) or (h < 1):
		raise Exception('width and height must be positive')
	_width = w
	_height = h
	pygame.display.set_caption('Motherboard')

	_surface = pygame.display.set_mode([w, h])
	clear()

def _scaleX(x):
    return _width * (x - _xmin) / (_xmax - _xmin)

def _scaleY(y):
    return _height * (_ymax - y) / (_ymax - _ymin)

def _factorX(w):
    return w * _width / abs(_xmax - _xmin)

def _factorY(h):
    return h * _height / abs(_ymax - _ymin)


#-----------------------------------------------------------------------
# Return color object
def pygameColor(c):
    """
    Convert c, an object of type color.Color, to an equivalent object
    of type pygame.Color.  Return the result.
    """
    r = c.getRed()
    g = c.getGreen()
    b = c.getBlue()
    return pygame.Color(r, g, b)

#-----------------------------------------------------------------------
def setXscale(min=_DEFAULT_XMIN, max=_DEFAULT_XMAX):
	"""
	Set the x-scale of the surface such that the minimum x value is
	min and the maximum x value is max.
	"""
	global _xmin
	global _xmax
	size = max - min
	_xmin = min - _BORDER * size
	_xmax = max + _BORDER * size

def setYscale(min=_DEFAULT_YMIN, max=_DEFAULT_YMAX):
	"""
	Set the y-scale of the surface such that the minimum y value is
	min and the maximum y value is max.
	"""
	global _ymin
	global _ymax
	size = max - min
	_ymin = min - _BORDER * size
	_ymax = max + _BORDER * size

def setPenRadius(r=_DEFAULT_PEN_RADIUS):
	"""
	Set the pen radius to r.
	"""
	global _penRadius
	if r < 0:
		raise Exception('Argument to setPenRadius() must be non-neg')
	_penRadius = r * _DEFAULT_SIZE


def setPenColor(c=_DEFAULT_PEN_COLOR):
	"""
	Set the pen color to c, where c is an object of class color.Color.
	"""
	global _penColor
	_penColor = c



def setFontFamily(f=_DEFAULT_FONT_FAMILY):
	"""
	Set the font family to f (e.g. 'Helvetica' or 'Courier').
	"""
	global _fontFamily
	_fontFamily = f

def setFontSize(s=_DEFAULT_FONT_SIZE):
	"""
	Set the font size to s (e.g. 12 or 16).
	"""
	global _fontSize
	_fontSize = s


#-----------------------------------------------------------------------
def _pixel(x, y):
	"""
	Draw on the surface a pixel at (x, y).
	"""
	xs = _scaleX(x)
	xy = _scaleY(y)

	pygame.gfxdraw.pixel(_surface,
		int(round(xs)),
		int(round(xy)),
		pygameColor(_penColor))

def point(x, y):
	"""
	Draw on the surface a point at (x, y).
	"""
	r = _penRadius
	#If the radius is too small, then simply draw a pixel
	if r <= 1:
		_pixel(x, y)
	else:
		xs = _scaleX(x)
		ys = _scaleY(y)

		pygame.draw.ellipse(_surface,
			pygameColor(_penColor),
			pygame.Rect(
				int(round(xs-_penRadius)),
				int(round(ys-_penRadius)),
				int(round(_penRadius*2)),
				int(round(_penRadius*2))),
			0)


def line(x0, y0, x1, y1):
    """
    Draw on the surface a line from (x0, y0) to (x1, y1).
    """
    x0s = _scaleX(x0)
    y0s = _scaleY(y0)
    x1s = _scaleX(x1)
    y1s = _scaleY(y1)
    lineWidth = _penRadius * 2.0
    if lineWidth == 0: lineWidth = 1
    pygame.draw.line(_surface,
        pygameColor(_penColor),
        (int(round(x0s)), int(round(y0s))),
        (int(round(x1s)), int(round(y1s))),
        int(round(lineWidth)))

    # If the line is thick, then round off the endpoints.
    if lineWidth >= 3:
        point(x0, y0)
        point(x1, y1)

#my code
def rectangle(x, y, w, h):
	"""
	Draw on the surface a rectangle of width w and height h,
	centered on (x, y).
	"""
	ws = _factorX(2*w)
	hs = _factorY(2*h)
	if (ws <= 1) and (hs <= 1):
		_pixel(x, y)
	else:
		xs = _scaleX(x)
		ys = _scaleY(y)
		pygame.draw.rect(_surface, pygameColor(_penColor), pygame.Rect(xs-ws/2, ys-hs/2, ws, hs), int(_penRadius))

#my code
def circle(x, y, r):
	"""
	Draw on the surface a circle of radius r centered on (x, y).
	"""
	ws = _factorX(2*r)
	hs = _factorY(2*r)
	if (ws <= 1) and (hs <= 1):
		_pixel(x, y)
	else:
		xs = _scaleX(x)
		ys = _scaleY(y)
		pygame.draw.ellipse(_surface,
			pygameColor(_penColor),
			pygame.Rect(xs-ws/2, ys-hs/2, ws, hs),
			int(_penRadius))

def filledCircle(x, y, r):
	"""
	Draw on the surface a filled circle of radius r centered on (x, y).
	"""
	ws = _factorX(2*r)
	hs = _factorY(2*r)
	if (ws <= 1) and (hs <= 1):
		_pixel(x, y)
	else:
		xs = _scaleX(x)
		ys = _scaleY(y)
		pygame.draw.ellipse(_surface,
			pygameColor(_penColor),
			pygame.Rect(xs-ws/2, ys-hs/2, ws, hs),
			0)

def filledRectangle(x, y, w, h):
	"""
	Draw on the surface a filled rectangle of width w and height h,
	centered on (x, y).
	"""
	ws = _factorX(2*w)
	hs = _factorY(2*h)
	if (ws <= 1) and (hs <= 1):
		_pixel(x, y)
	else:
		xs = _scaleX(x)
		ys = _scaleY(y)
		pygame.draw.rect(_surface,
			pygameColor(_penColor),
			pygame.Rect(xs-ws/2, ys-hs/2, ws, hs),
			0)

def text(x, y, s):
    """
    Draw on the surface string s centered at (x, y).
    """
    xs = _scaleX(x)
    ys = _scaleY(y)
    font = pygame.font.SysFont(_fontFamily, _fontSize)
    text = font.render(s, 1, pygameColor(_penColor))
    textpos = text.get_rect(center=(int(round(xs)), int(round(ys))))
    _surface.blit(text, textpos)

def clear():
	"""
	Clear the surface
	"""
	_surface.fill(pygameColor(WHITE))

def show():
    """
    Show the surface on the window.
    """
    pygame.display.flip()
    _checkForEvents()


def _checkForEvents():
    """
    Check if any new event has occured (such as a key typed or button
    pressed).  If a key has been typed, then put that key in a queue.
    """
    global _surface
    global buttonBackground
    global _keysTyped
    
    for event in pygame.event.get():
    	if event.type == pygame.QUIT:
            sys.exit()
def sleep(t):
    """
    Sleep for t milliseconds.
    """
    time.sleep(float(t) / 1000.0)
#-inititalize-
pygame.font.init()
