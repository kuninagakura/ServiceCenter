import motherboard
from table import Table

motherboard.createWindow(1200, 800)
motherboard.setXscale(0, 1200)
motherboard.setYscale(0, 800)
motherboard.setPenRadius(0.005)
motherboard.rectangle(600, 400, 600, 400)
motherboard.rectangle(600, 770, 600, 30)
motherboard.line(600, 740, 600, 800)

tablelist = []

table1 = Table(600, 400, 100, 170, 1)
tablelist.append(table1)
table1.draw()
table1.orderInput("Chicken")
table1.draw()
table1.orderReady("Chicken")
table1.draw()
table1.

table2 = Table(900, 500, 100, 140, 2)
table2.draw()


table3 = Table(200, 500, 100, 170, 2)
table3.draw()

print len(table1.ordersleft)
while True:
    motherboard.show()

 
def update():
	for i in tablelist:
		i.update()