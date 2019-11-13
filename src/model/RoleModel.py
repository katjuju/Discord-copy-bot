from model.PermissionsModel import *

class RoleModel:

	def __init__(self):
		self.id = None;
		self.name = None;
		self.permissions = None;
		self.color = None;
		self.hoist = None;
		self.position = None;
		self.mentionable = None;
		self.is_everyone = None;
		self.managed = None;


	def fillFromRole(self, role):
		self.id = role.id;
		self.name = role.name;
		self.color = role.color.value;
		self.hoist = role.hoist;
		self.position = role.position;
		self.mentionable = role.mentionable;
		self.is_everyone = role.is_default();
		self.managed = role.managed;

		permissionsModel = PermissionsModel();
		permissionsModel.fillFromPermissions(role.permissions);

		self.permissions = permissionsModel.__dict__;
