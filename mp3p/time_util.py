class TimeUtil:

	def __init__(self, time_array):
		self.time_array = time_array
		self.length = len(time_array)
		self.conversion_array = [1, 60, 3600]

	def time_to_ms(self):
		time = 0
		for i in range(self.length):
			time += int(self.time_array[self.length - i - 1]) * int(self.conversion_array[i])
		time *= 1000
		return time
