class Logger:

	def __init__(self):
		pass;


	def info(self, msg):
		print("[INFO] " + str(msg));


	def warning(self, msg):
		print("[WARNING] " + str(msg));


	def error(self, msg):
		print("[ERROR] " + str(msg));


	def debug(self, msg):
		print("[DEBUG] " + str(msg));
