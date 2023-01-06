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
		},
		{
			"label": "Days Since Equipment is Out",
			"fieldname": "days",
			"fieldtype": "Int",
			"width": "100"
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

	if filters.item_code:
		conditions["item_code"] = filters.item_code

	if filters.category:
		conditions["category"] = filters.category

	return conditions

def get_data(filters):
	
	conditions = get_conditions(filters)
	data = frappe.db.get_all("Equipment", fields=['name','item_code','storage_location','location_status','category','status','serial_number','indicator'], filters=conditions, order_by='name')
	query = f'select name, DATEDIFF(storage_location_date, last_location_date) as days from `tabEquipment` where storage_location != last_location order by name'
	diff_query = frappe.db.sql(query,as_dict=1)

	for i in diff_query:
		for j in data:
			if (i.get('name') == j.get('name')):
				j['days'] = i.get('days')
			else:
				j['days'] = ''
	return data
