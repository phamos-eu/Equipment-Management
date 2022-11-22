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
			"options": "Equipment Maintenance",
			"width": 150
		},
		{
			"label": _("Status"),
			"fieldtype": "Data",
			"fieldname": "status",
			"width": "150"
		},
		{
			"label": _("Due Date"),
			"fieldtype": "Date",
			"fieldname": "due_date",
			"width": "150"
		},
		{
			"label": _("Last Location"),
			"fieldtype": "Link",
			"fieldname": "location",
			"options": "Location",
			"width": "150"
		},
		{
			"label": _("Location Status"),
			"fieldtype": "Data",
			"fieldname": "location_status",
			"width": "150"
		},
		{
			"label": _("Responsible Officer"),
			"fieldtype": "Link",
			"fieldname": "responsible_officer",
			"options": "User",
			"width": "150"
		}
	]
	return columns

def get_conditions(filters):
	conditions = ''

	if filters.name:
		conditions += f'and em.name="{filters.name}"'
		return conditions

	if filters.status:
		conditions += f'and em.status="{filters.status}"'

	return conditions

def get_data(filters):
	
	conditions = get_conditions(filters)
	query = f'select em.equipment, em.name, em.status, em.due_date, em.location, eq.location_status, em.responsible_officer from `tabEquipment Maintenance` em inner join `tabEquipment` eq on em.equipment=eq.name where em.equipment=em.equipment {conditions} order by due_date'
	# data = frappe.db.get_all("Equipment Maintenance", fields=['equipment','name','status','due_date','location','responsible_officer'], filters=conditions, order_by='due_date')
	data = frappe.db.sql(query)
	return data
