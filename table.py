import motherboard
from order import Order
from cupPanel import cupPanel
import time
# def main():
	

class Table:
	#constants
	NUM_ORDERS = 8 

	def __init__(self, x, y, w, h, n):
		self.xpos = x
		self.ypos = y
		self.width = w
		self.height = h
		self.innerheight = h-50
		self.number = n

		self.ordersleft = []
		self.ordersright = []
		self.cupPanel = cupPanel(self.NUM_ORDERS)

		for i in range(self.NUM_ORDERS/2):
			self.ordersleft.append(Order())

		print len(self.ordersleft)
		count = 0.0
		for i in self.ordersleft:

			i.xpos = self.xpos - self.width/2
			i.ypos = self.ypos + 3*self.innerheight/4 - 2*self.innerheight*(count/len(self.ordersleft))
			i.width = self.width/2 
			i.height = self.innerheight/len(self.ordersleft)
			count+= 1

		for i in range(self.NUM_ORDERS/2):
			self.ordersright.append(Order())

		count = 0.0
		for i in self.ordersright:

			i.xpos = self.xpos + self.width/2
			i.ypos = self.ypos + 3*self.innerheight/4 - 2*self.innerheight*(count/len(self.ordersleft))
			i.width = self.width/2 
			i.height = self.innerheight/len(self.ordersright)
			count+= 1
		
		global startTime
		startTime = time.time()

	def setOrder(self, ordernum, ordername):
		if ordernum > self.NUM_ORDERS: return

		if ordernum <= self.NUM_ORDERS/2:
			self.ordersleft[ordernum].name = ordername

		else:
			self.ordersright[ordernum - self.NUM_ORDERS/2].name = ordername

	#Add order to table and set order to not-ready state
	def orderInput(self, ordername):

		for i in self.ordersleft:
			if not i.name: 
				i.name = ordername
				i.color = motherboard.CUP_RED
				return

		for i in self.ordersright:
			if not i.name:
				i.name = ordername
				i.color = motherboard.CUP_RED
				return

	#Set order to ready state
	def orderReady(self, ordername):

		for i in self.ordersleft:
			if i.name == ordername:
				if i.color == motherboard.CUP_RED:
					i.color = motherboard.CUP_GREEN
					return

		for i in self.ordersright:
			if i.name == ordername:
				if i.color == motherboard.CUP_RED:
					i.color = motherboard.CUP_GREEN
					return

	#Clear order from table
	def orderDelivered(self, ordername):
		for i in self.ordersleft:
			if i.name == ordername:
				if i.color == motherboard.CUP_GREEN:
					i.color = motherboard.WHITE
					i.name = ""
					return

		for i in self.ordersright:
			if i.name == ordername:
				if i.color == motherboard.CUP_GREEN:
					i.color = motherboard.WHITE
					i.name = ""
					return


	def draw(self):
		global startTime
		motherboard.setPenRadius(.005)
		motherboard.setPenColor(motherboard.DARK_GRAY)
		motherboard.rectangle(self.xpos, self.ypos, self.width, self.height)
		motherboard.rectangle(self.xpos, self.ypos, self.width, self.innerheight)
		#yellow status
		motherboard.setPenColor(motherboard.CUP_YELLOW)
		motherboard.filledCircle(self.xpos, self.ypos + self.height - (self.height - self.innerheight)/2 , 20)
		motherboard.setPenColor(motherboard.DARK_GRAY)

		#red status
		motherboard.setPenColor(motherboard.CUP_RED)
		motherboard.filledCircle(self.xpos - 2*self.width/3, self.ypos + self.height - (self.height - self.innerheight)/2 , 20)
		motherboard.setPenColor(motherboard.DARK_GRAY)

		#green status
		motherboard.setPenColor(motherboard.CUP_GREEN)
		motherboard.filledCircle(self.xpos + 2*self.width/3, self.ypos + self.height - (self.height - self.innerheight)/2 , 20)
		motherboard.setPenColor(motherboard.DARK_GRAY)

		#outlines of circles
		motherboard.setPenRadius(0.004)
		motherboard.circle(self.xpos, self.ypos + self.height - (self.height - self.innerheight)/2 , 21)
		motherboard.circle(self.xpos + 2*self.width/3, self.ypos + self.height - (self.height - self.innerheight)/2 , 21)
		motherboard.circle(self.xpos - 2*self.width/3, self.ypos + self.height - (self.height - self.innerheight)/2 , 21)

		#add table
)
		
		#draw orders
		for i in self.ordersleft:
			i.draw()

		for i in self.ordersright:
			i.draw()

		#draw cup panel numbers
		motherboard.text(self.xpos, self.ypos + self.height - (self.height - self.innerheight)/2, str(self.cupPanel.num_yellow))
		motherboard.text(self.xpos+ 2*self.width/3, self.ypos + self.height - (self.height - self.innerheight)/2, str(self.cupPanel.num_green))
		motherboard.text(self.xpos- 2*self.width/3, self.ypos + self.height - (self.height - self.innerheight)/2, str(self.cupPanel.num_red))

		motherboard.setFontFamily("Arial")
		motherboard.setFontSize(20)
		motherboard.text(self.xpos, self.ypos, 'Table: ' + str(self.number))
	
	def update(self):

		for i in self.ordersleft:
			i.draw()

		for i in self.ordersright:
			i.draw()

		motherboard.text(self.xpos, self.ypos + self.height - (self.height - self.innerheight)/2, str(self.cupPanel.num_yellow))
		motherboard.text(self.xpos+ 2*self.width/3, self.ypos + self.height - (self.height - self.innerheight)/2, str(self.cupPanel.num_green))
		motherboard.text(self.xpos- 2*self.width/3, self.ypos + self.height - (self.height - self.innerheight)/2, str(self.cupPanel.num_red))

		

		#drawTimer
		#not working
		# curTime = time.time() - startTime
		# motherboard.setPenColor(motherboard.DARK_GRAY)
		# motherboard.text(self.xpos, self.ypos - self.height + (self.height - self.innerheight)/2, str(curTime))
		# time.sleep(100)
		# motherboard.setPenColor(motherboard.WHITE)
		# motherboard.filledRectangle(self.xpos, self.ypos - self.height + (self.height - self.innerheight)/2, self.width -10, 20)



if __name__ == "__main__":
	main()
