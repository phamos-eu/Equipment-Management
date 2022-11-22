# Copyright (c) 2022, Deepak Kumar and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class ManualEquipmentMovement(Document):
	def validate(self):
		equipment = frappe.get_doc('Equipment', self.equipment)
		if self.status == "Returned":
			equipment.location_status = "Available"
		else:
			equipment.location_status = self.type
		equipment.save(ignore_permissions=True)
		equipment.reload()
	
	def on_trash(self):
		equipment = frappe.get_doc('Equipment', self.equipment)
		mem = frappe.get_last_doc('Equipment')
		if equipment:
			if self.status == "Returned":
				equipment.location_status = "Available"
			else:
				equipment.location_status = mem.type
		else:
			equipment.location_status = ''
		equipment.save(ignore_permissions=True)
		equipment.reload()
