# Copyright (c) 2022, Deepak Kumar and contributors
# For license information, please see license.txt

import frappe
from frappe import _

def execute(filters=None):
	filters = frappe._dict(filters or {})
	columns = get_columns(filters)
	data = get_data(filters)
	return columns, data

def get_columns(filters):
	columns = [
		{
			"label": _("ID"),
			"fieldtype": "Link",
			"fieldname": "name",
			"options": "Equipment",
			"width": 150
		},
		{
			"label": _("Item Code"),
			"fieldtype": "Data",
			"fieldname": "item_code",
			"width": 150
		},
		{
			"label": _("Location"),
			"fieldtype": "Data",
			"fieldname": "storage_location",
			"width": 150
		},
		{
			"label": _("Location Status"),
			"fieldtype": "Data",
			"fieldname": "location_status",
			"width": "150"
		},
		{
			"label": _("Category"),
			"fieldtype": "Data",
			"fieldname": "category",
			"width": 150
		},
		{
			"label": _("Status"),
			"fieldtype": "Data",
			"fieldname": "status",
			"width": "150"
		},
		{
			"label": _("Serial Number"),
			"fieldtype": "Data",
			"fieldname": "serial_number",
			"width": "150"
		},
		{
			"label": "Indicator",
			"fieldname": "indicator",
			"fieldtype": "Data",
			"hidden": 1,	
		}
	]
	return columns

def get_conditions(filters):
	conditions = {}

	if "name" in filters:
		conditions["name"] = filters.name
		return conditions

	if "status" in filters:
		conditions["status"] = filters.status

	if "item_code" in filters:
		conditions["item_code"] = filters.item_code

	if "category" in filters:
		conditions["category"] = filters.category

	return conditions

@frappe.whitelist()
def get_data(filters):
	conditions = get_conditions(filters)
	data = frappe.db.get_all("Equipment", fields=['name','item_code','storage_location','location_status','category','status','serial_number','indicator'], filters=conditions, order_by='name')
	return data
