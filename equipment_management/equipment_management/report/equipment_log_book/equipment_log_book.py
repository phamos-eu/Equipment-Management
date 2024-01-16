# Copyright (c) 2022, Deepak Kumar and contributors
# For license information, please see license.txt

import frappe
from frappe import _

def execute(filters=None):
	columns = get_columns()
	data = get_data(filters)
	return columns, data

def get_columns():
	columns = [
		{
			"label": _("Posting Date"),
			"fieldtype": "Data",
			"fieldname": "posting_date",
			"width": 170
		},
		{
			"label": _("Equipment Name"),
			"fieldtype": "Link",
			"fieldname": "equipment",
			"options": "Equipment",
			"width": 150
		},
		{
			"label": _("Indicator"),
			"fieldtype": "Data",
			"fieldname": "indicator",
			"width": 1,
			"hidden":1
		},
		{
			"label": _("Equipment Status"),
			"fieldtype": "Data",
			"fieldname": "equipment_status",
			"width": 150
		},
		{
			"label": _("Item Code"),
			"fieldtype": "Link",
			"fieldname": "item_code",
			"options": "Item",
			"width": 150
		},
		{
			"label": _("Location"),
			"fieldtype": "Link",
			"fieldname": "storage_location",
			"options": "Location",
			"width": 150
		},
		{
			"label": "Reference Type",
			"fieldname": "doctype",
			"fieldtype": "Data",
			"width": 150
		},
		{
			"label": _("Reference"),
			"fieldtype": "Dynamic Link",
			"fieldname": "reference",
			"options": "doctype",
			"width": 150
		},
		{
			"label": "Status",
			"fieldname": "Data",
			"fieldtype": "eqmaint_status",
			"width": 150
		}
	]
	return columns
def get_data(filters):
	equipment = filters.get('equipment')
	equipment_status_filter = ""
	if "equipment_status" in filters:
		equipment_status_filter = "and eq.status='{}'".format(filters["equipment_status"])
	item_code_filter = ""
	if "item_code" in filters:
		item_code_filter = "and eq.item_code='{}'".format(filters["item_code"])
	reference_type_filter = ""
	if "reference_type" in filters:
		reference_type_filter = "and doctype.name='{}'".format(filters["reference_type"])
	reference_type_filter = ""
	if "reference_type" in filters:
		reference_type_filter = "and doctype.name='{}'".format(filters["reference_type"])
	maintenance_status_filter = ""
	if "maintenance_status" in filters:
		maintenance_status_filter = "and eqmaint.status='{}'".format(filters["maintenance_status"])
	query = '''select
    IFNULL(CONCAT(eqmaint.posting_date,' ',eqmaint.posting_time), eqmaint.modified) pd,
    eq.name,
    eq.indicator,
    eq.status,
    eq.item_code,
    eq.storage_location,
    doctype.name,
    eqmaint.name,
    eqmaint.status eqmaint_status

from 
    `tabEquipment` eq,`tabEquipment Maintenance` eqmaint,`tabDocType` doctype
where
    eq.name = eqmaint.equipment and
    eq.name = "{0}" and
    doctype.name = 'Equipment Maintenance'
	{6} {7} {8} {9}
union
select
    IFNULL(CONCAT(eqprob.posting_date,' ',eqprob.posting_time), eqprob.modified),
    eq.name,
    eq.indicator,
    eq.status,
    eq.item_code,
    eq.storage_location,
    doctype.name,
    eqprob.name,
    eqprob.status

from
    `tabEquipment` eq,`tabProblem Report` eqprob,`tabDocType` doctype
where
    eq.name = eqprob.equipment and
    eq.name = "{1}" and
    doctype.name = 'Problem Report'
	{6} {7} {8}
union
select
    IFNULL(eqlog.posting_date, eqlog.modified),
    eq.name,
    eq.indicator,
    eq.status,
    eq.item_code,
    eq.storage_location,
    doctype.name,
    eqlog.name,
    eqlog.status
    
from
    `tabEquipment` eq,`tabEquipment Log` eqlog,`tabDocType` doctype
where
    eq.name = eqlog.equipment and
    eq.name = "{2}" and
    doctype.name = 'Equipment Log'
	{6} {7} {8}
union
select
    IFNULL(CONCAT(rf.posting_date,' ',rf.posting_time), rf.modified),
    eq.name,
    eq.indicator,
    eq.status,
    eq.item_code,
    eq.storage_location,
    doctype.name,
    rf.name,
    null
    
from
    `tabEquipment` eq,`tabRFID Trace` rf,`tabDocType` doctype
where
    eq.name = rf.equipment and
    eq.name = "{3}" and
    doctype.name = 'RFID Trace'
	{6} {7} {8}
union
select
    IFNULL(CONCAT(mem.posting_date,' ',mem.posting_time), mem.modified),
    eq.name,
    eq.indicator,
    eq.status,
    eq.item_code,
    eq.storage_location,
    doctype.name,
    mem.name,
    mem.type
    
from
    `tabEquipment` eq,`tabManual Equipment Movement` mem,`tabDocType` doctype
where
    eq.name = mem.equipment and
    eq.name = "{4}"  and
    doctype.name = 'Manual Equipment Movement'
	{6} {7} {8}
union
select
    rl.datetime,
    eq.name,
    eq.indicator,
    eq.status,
    eq.item_code,
    rl.location,
    doctype.name,
    rl.name,
    null
from
    `tabEquipment` eq,`tabRFID Logs` rl,`tabDocType` doctype
where
    eq.rfid_number = rl.id and
    eq.name = "{5}" and
    doctype.name = 'RFID Logs'
	{6} {7} {8}
order by `pd` desc
	'''.format(equipment,equipment,equipment,equipment,equipment,equipment, equipment_status_filter, item_code_filter, reference_type_filter, maintenance_status_filter)
	print(query)
	data = frappe.db.sql(query)
	return data