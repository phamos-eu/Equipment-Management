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