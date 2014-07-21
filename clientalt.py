import motherboard
from order import Order
from table import Table

motherboard.createWindow(1200, 800)
motherboard.setXscale(0, 1200)
motherboard.setYscale(0, 800)

motherboard.setPenRadius(0.005)
motherboard.setPenColor(motherboard.DARK_GRAY)

#frame
motherboard.rectangle(600, 400, 600, 400)
motherboard.rectangle(600, 770, 600, 30)
motherboard.line(600, 740, 600, 800)





#-------------------------------------------------------------------
# Large Rectangle
#
#-------------------------------------------------------------------

#large
largeTable = Table(600, 400, 100, 170, 1)
largeX = 600
largeY = 400
motherboard.rectangle(largeX, largeY, 100, 170)
motherboard.rectangle(largeX, largeY, 100, 120)
#center line
motherboard.setPenRadius(0.002)
motherboard.line(largeX, largeY+120, largeX, largeY-118)
#rows
motherboard.line(largeX-100, largeY, largeX+98, largeY)
motherboard.line(largeX-100, largeY-60, largeX+98, largeY-60)
motherboard.line(largeX-100, largeY+60, largeX+98, largeY+60)


#-------------------------------------------------------------------
# Small Rectangle
#
#-------------------------------------------------------------------

#small
smallX = 900
smallY = 550
motherboard.setPenRadius(0.005)
motherboard.rectangle(smallX, smallY, 100, 140)
motherboard.rectangle(smallX, smallY, 100, 100)
#center line
motherboard.setPenRadius(0.002)
motherboard.line(smallX, smallY+100, smallX, smallY-98)
#rows
motherboard.line(smallX-100, smallY, smallX+100, smallY)
motherboard.line(smallX-100, smallY-50, smallX+98, smallY-50)
motherboard.line(smallX-100, smallY+50, smallX+98, smallY+50)


#-------------------------------------------------------------------
# Circle Table
#
#-------------------------------------------------------------------

#circle
circleX = 200
circleY = 260
motherboard.setPenRadius(0.005)
motherboard.circle(circleX, circleY, 182)
motherboard.rectangle(circleX, circleY, 100, 150)
motherboard.rectangle(circleX, circleY, 100, 110)
#center line
motherboard.setPenRadius(0.002)
motherboard.line(circleX, circleY+110, circleX, circleY-108)
#rows
motherboard.line(circleX-100, circleY, circleX+98, circleY)
motherboard.line(circleX-100, circleY-55, circleX+98, circleY-55)
motherboard.line(circleX-100, circleY+55, circleX+98, circleY+55)

#-------------------------------------------------------------------
# Cup panel for the large rectangle
#
#-------------------------------------------------------------------

#large cup panel
largecupX = largeX
largecupY = largeY + 145
motherboard.setPenRadius(0.005)
motherboard.setPenColor(motherboard.DARK_GRAY)
motherboard.rectangle(largecupX, largecupY, 100, 25)

#yellow status
motherboard.setPenColor(motherboard.CUP_YELLOW)
motherboard.filledCircle(largecupX, largecupY, 20)
motherboard.setPenColor(motherboard.DARK_GRAY)

#red status
motherboard.setPenColor(motherboard.CUP_RED)
motherboard.filledCircle(largecupX-60, largecupY, 20)
motherboard.setPenColor(motherboard.DARK_GRAY)

#green status
motherboard.setPenColor(motherboard.CUP_GREEN)
motherboard.filledCircle(largecupX+60, largecupY, 20)
motherboard.setPenColor(motherboard.DARK_GRAY)

#outlines of circles
motherboard.setPenRadius(0.004)
motherboard.circle(largecupX, largecupY, 21)
motherboard.circle(largecupX+60, largecupY, 21)
motherboard.circle(largecupX-60, largecupY, 21)

#Statuses
motherboard.setFontFamily("Arial")
motherboard.setFontSize(20)
yellowStatus = "1"
redStatus = "3"
greenStatus = "2"
motherboard.text(largecupX, largecupY, yellowStatus)
motherboard.text(largecupX+60, largecupY, greenStatus)
motherboard.text(largecupX-60, largecupY, redStatus)

#-------------------------------------------------------------------
# Cup panel for the circle
#
#-------------------------------------------------------------------

#circle cup panel
circlecupX = circleX
circlecupY = circleY + 130
motherboard.setPenRadius(0.005)
motherboard.setPenColor(motherboard.DARK_GRAY)
motherboard.rectangle(circlecupX, circlecupY, 100, 21)

#yellow status
motherboard.setPenColor(motherboard.CUP_YELLOW)
motherboard.filledCircle(circlecupX, circlecupY, 17)
motherboard.setPenColor(motherboard.DARK_GRAY)

#red status
motherboard.setPenColor(motherboard.CUP_RED)
motherboard.filledCircle(circlecupX-60, circlecupY, 17)
motherboard.setPenColor(motherboard.DARK_GRAY)

#green status
motherboard.setPenColor(motherboard.CUP_GREEN)
motherboard.filledCircle(circlecupX+60, circlecupY, 17)
motherboard.setPenColor(motherboard.DARK_GRAY)

#outlines of circles
motherboard.setPenRadius(0.004)
motherboard.circle(circlecupX, circlecupY, 18)
motherboard.circle(circlecupX+60, circlecupY, 18)
motherboard.circle(circlecupX-60, circlecupY, 18)

#Statuses
motherboard.setFontFamily("Arial")
motherboard.setFontSize(20)
yellowStatus = "0"
redStatus = "2"
greenStatus = "3"
motherboard.text(circlecupX, circlecupY, yellowStatus)
motherboard.text(circlecupX+60, circlecupY, greenStatus)
motherboard.text(circlecupX-60, circlecupY, redStatus)

#-------------------------------------------------------------------
# Cup panel for the small rectangle
# 
#-------------------------------------------------------------------
#small cup panel
smallcupX = smallX
smallcupY = smallY + 120
motherboard.setPenRadius(0.005)
motherboard.setPenColor(motherboard.DARK_GRAY)
motherboard.rectangle(smallcupX, smallcupY, 100, 21)

#yellow status
motherboard.setPenColor(motherboard.CUP_YELLOW)
motherboard.filledCircle(smallcupX, smallcupY, 17)
motherboard.setPenColor(motherboard.DARK_GRAY)

#red status
motherboard.setPenColor(motherboard.CUP_RED)
motherboard.filledCircle(smallcupX-60, smallcupY, 17)
motherboard.setPenColor(motherboard.DARK_GRAY)

#green status
motherboard.setPenColor(motherboard.CUP_GREEN)
motherboard.filledCircle(smallcupX+60, smallcupY, 17)
motherboard.setPenColor(motherboard.DARK_GRAY)

#outlines of circles
motherboard.setPenColor(motherboard.DARK_GRAY)
motherboard.setPenRadius(0.004)
motherboard.circle(smallcupX, smallcupY, 18)
motherboard.circle(smallcupX+60, smallcupY, 18)
motherboard.circle(smallcupX-60, smallcupY, 18)

#Statuses
motherboard.setFontFamily("Arial")
motherboard.setFontSize(20)
yellowStatus = "0"
redStatus = "2"
greenStatus = "3"
motherboard.text(smallcupX, smallcupY, yellowStatus)
motherboard.text(smallcupX+60, smallcupY, greenStatus)
motherboard.text(smallcupX-60, smallcupY, redStatus)


#-------------------------------------------------------------------
# Timers
# 
#-------------------------------------------------------------------

time = "20:00"
motherboard.text(largeX, largeY - 145, time + " min")
motherboard.text(smallX, smallY - 120, time + " min")
motherboard.text(circleX, circleY - 130, time + " min")

#-------------------------------------------------------------------
# Order for large rectangle
# 
#-------------------------------------------------------------------
ordertext = "Chicken"
orderX = largeX - 49
orderY = largeY + 89
motherboard.setPenColor(motherboard.CUP_GREEN)
motherboard.filledRectangle(orderX, orderY, 49, 29)
motherboard.setPenColor(motherboard.DARK_GRAY)
motherboard.text(orderX, orderY, ordertext)

ordertext = "Beef"
orderX = largeX - 49
orderY = largeY + 29
motherboard.setPenColor(motherboard.CUP_RED)
motherboard.filledRectangle(orderX, orderY, 49, 29)
motherboard.setPenColor(motherboard.DARK_GRAY)
motherboard.text(orderX, orderY, ordertext)

ordertext = "Beef"
orderX = largeX - 49
orderY = largeY - 31
motherboard.setPenColor(motherboard.CUP_RED)
motherboard.filledRectangle(orderX, orderY, 49, 29)
motherboard.setPenColor(motherboard.DARK_GRAY)
motherboard.text(orderX, orderY, ordertext)

ordertext = "Chicken"
orderX = largeX - 49
orderY = largeY - 91
motherboard.setPenColor(motherboard.CUP_RED)
motherboard.filledRectangle(orderX, orderY, 49, 29)
motherboard.setPenColor(motherboard.DARK_GRAY)
motherboard.text(orderX, orderY, ordertext)

while True:
    motherboard.show()
