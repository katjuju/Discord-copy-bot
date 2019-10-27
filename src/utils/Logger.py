class Logger:

	def __init__(self):
		pass;


	@staticmethod
	def info(msg):
		print("[INFO] " + str(msg));


	@staticmethod
	def warning(msg):
		print("[WARNING] " + str(msg));


	@staticmethod
	def error(msg):
		print("[ERROR] " + str(msg));


	@staticmethod
	def debug(msg):
		print("[DEBUG] " + str(msg));
