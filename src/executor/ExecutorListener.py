class ExecutorListener:

	async def taskChanged(self, newTaskName):
		pass;


	async def taskFinished(self, details=""):
		pass;


	async def taskError(self, details):
		pass;


	async def aborted(self):
		pass;


	async def completed(self):
		pass;
