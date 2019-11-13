class MemberModel:

	def __init__(self):
		self.id = None;
		self.name = None;
		self.discriminator = None;
		self.bot = None;
		self.nick = None;
		self.rolesId = None;


	def fillFromMember(self, member):
		self.id = member.id;
		self.name = member.name;
		self.discriminator = member.discriminator;
		self.bot = member.bot;
		self.nick = member.nick;
		self.rolesId = list();

		for role in member.roles:
			self.rolesId.append(role.id);
