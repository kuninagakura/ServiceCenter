import motherboard

def main():
	return 0

class cupPanel:

	def __init__(self, num_cups):
		self.num_red = 0
		self.num_yellow = 0
		self.num_green = num_cups

	def cupStatus(self, red, yellow, green):
		self.num_red = red
		self.num_yellow = yellow
		self.num_green = green
		
	def update(self):
		return 


if __name__ == "__main__":
	main()