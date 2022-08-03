from __future__ import unicode_literals

import frappe

def get_context(context):
	# do your magic here
	pass
def get_list_context(context):
	context.get_list = get_equipment_maintenance_list

def get_equipment_maintenance_list(doctype, txt, filters, limit_start, limit_page_length, order_by):
	data = frappe.db.sql(""" select name, status, due_date from `tabEquipment Maintenance` where status='Pending' """,as_dict=1)
	return data