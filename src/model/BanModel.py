class BanModel:
	def __init__(self):
		self.user = None;
		self.reason = None;


	def fillFromBan(self, ban):
		self.user = ban.user.id;
		self.reason = ban.reason;
