import motherboard

def main():
	#test code
	order = Order()
	order.name = "Food"
	print(order.name)

class Order:
	name = ""
	xpos = 0
	ypos = 0
	width = 0
	height = 0
	color = motherboard.WHITE

	def __init__(self):
		name = ""

	def draw(self):
		motherboard.setPenRadius(.002)
		motherboard.setPenColor(self.color)
		motherboard.filledRectangle(self.xpos, self.ypos, self.width, self.height)
		motherboard.setPenColor(motherboard.DARK_GRAY)
		motherboard.setFontFamily("Arial")
		motherboard.setFontSize(20)
		motherboard.text(self.xpos, self.ypos, self.name)
		motherboard.rectangle(self.xpos, self.ypos, self.width, self.height)


if __name__ == '__main__':
	main()
