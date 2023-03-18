from .constants import *

class Click:
	def __init__(self, clickType, pixelOffset, xCoord, yCoord):
		self.type = CLICK_TYPE
		self.clickType = clickType
		self.pixelOffset = pixelOffset
		self.xCoord = xCoord
		self.yCoord = yCoord

class ClickColor:
	def __init__(self, color, clickType, xCoords, yCoords):
		self.type = COLOR_CLICK_TYPE
		self.color = color
		self.clickType = clickType
		self.xCoordBounds = xCoords
		self.yCoordBounds = yCoords

class ClickImage:
	def __init__(self, clickType, imageLocation, pixelOffset, confidence, grayscale):
		self.type = IMAGE_CLICK_TYPE
		self.clickType = clickType
		self.imageLocation = imageLocation
		self.pixelOffset = pixelOffset
		self.confidence = confidence
		self.grayscale = grayscale

class Delay:
	def __init__(self, delayTime, timeOffset):
		self.type = DELAY_TYPE
		self.delayTime = delayTime #time in ms
		self.timeOffset = timeOffset #range of time in ms offset
	
class Num:
	def __init__(self, value):
		self.type = NUM_TYPE
		self.value = value

class Key:
	def __init__(self, key, action):
		self.type = KEY_TYPE
		self.key = str(key)
		self.action = action

class Text:
	def __init__(self, value):
		self.type = TEXT_TYPE
		self.value = value
