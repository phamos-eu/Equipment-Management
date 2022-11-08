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
			"label": _("Equipment Inventory Number"),
			"fieldtype": "Link",
			"fieldname": "equipment",
			"options": "Equipment",
			"width": 150
		},
		{
			"label": _("ID"),
			"fieldtype": "Link",
			"fieldname": "name",
			"options": "Problem Report",
			"width": 150
		},
		{
			"label": _("Status"),
			"fieldtype": "Data",
			"fieldname": "status",
			"width": "150"
		},
		{
			"label": _("Last Location"),
			"fieldtype": "Link",
			"fieldname": "last_location",
			"options": "Location",
			"width": "150"
		},
		{
			"label": _("Problem Title"),
			"fieldtype": "Data",
			"fieldname": "problem_title",
			"width": "150"
		},
		{
			"label": _("Posting Date"),
			"fieldtype": "Date",
			"fieldname": "posting_date",
			"width": "150"
		},
		{
			"label": _("Created By"),
			"fieldtype": "Link",
			"fieldname": "owner",
			"options": "User",
			"width": "150"
		}
	]
	return columns

def get_conditions(filters):
	conditions = {}

	if filters.name:
		conditions["name"] = filters.name
		return conditions

	if filters.status:
		conditions["status"] = filters.status

	return conditions

def get_data(filters):
	
	conditions = get_conditions(filters)
	data = frappe.db.get_all("Problem Report", fields=['equipment','name','status','last_location','problem_title','posting_date','owner'], filters=conditions, order_by='posting_date desc')

	return data
