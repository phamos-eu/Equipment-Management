# Copyright (c) 2022, Deepak Kumar and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class ProblemReport(Document):
	pass


def update_equipment_status(doc,method):
	equip_doc = frappe.get_doc('Equipment', doc.equipment)
	if frappe.db.exists("Problem Report", {'equipment':doc.equipment,'status':'Open','equipment_status':'Not Working'}):
		equip_doc.indicator = 3
		equip_doc.status = "Not Working"
		equip_doc.save(ignore_permissions=True)

	elif frappe.db.exists("Problem Report", {'equipment':doc.equipment,'status':'Open','equipment_status':'Working'}):
		equip_doc.indicator = 2
		equip_doc.status = "Working"
		equip_doc.save(ignore_permissions=True)
		
	else:
		equip_doc.indicator = 1
		equip_doc.status = "Working"
		equip_doc.save(ignore_permissions=True)
