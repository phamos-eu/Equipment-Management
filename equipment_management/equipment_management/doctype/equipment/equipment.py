# Copyright (c) 2022, Deepak Kumar and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Equipment(Document):
	pass

@frappe.whitelist()
def problem_report_exist(name):
	pr_doc = frappe.db.exists("Problem Report",{'equipment':name,'status':'Open'})
	if pr_doc:
		return 1
	return 0

@frappe.whitelist()
def create_rfid_tag(rfid_number):
	if not frappe.db.exists("RFID Tag", rfid_number):
		frappe.get_doc({
			"doctype": "RFID Tag",
			"title": rfid_number
		}).insert()