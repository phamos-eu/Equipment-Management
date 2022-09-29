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
			"width": 150
		},
		{
			"label": _("Name"),
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
			"fieldtype": "Data",
			"fieldname": "item_code",
			"width": 150
		},
		{
			"label": _("Location"),
			"fieldtype": "Data",
			"fieldname": "location",
			"width": 150
		},
		{
			"label": "doctype",
			"fieldname": "doctype",
			"fieldtype": "Data",
			"width": 150
		},
		{
			"label": "Status",
			"fieldname": "Data",
			"fieldtype": "status",
			"width": 150
		},
		{
			"label": _("Reference"),
			"fieldtype": "Dynamic Link",
			"fieldname": "reference",
			"options": "doctype",
			"width": 150
		}
	]
	return columns
def get_data(filters):
	equipment = filters.get('equipment')
	query = '''select
    IFNULL(eqmaint.posting_date, eqmaint.modified) pd,
    eq.name,
    eq.indicator,
    eq.status,
    eq.item_code,
    eq.location,
    doctype.name,
    eqmaint.status,
    eqmaint.name

from 
    `tabEquipment` eq,`tabEquipment Maintenance` eqmaint,`tabDocType` doctype
where
    eq.name = eqmaint.equipment and
    eq.name = "{0}" and
    doctype.name = 'Equipment Maintenance'
union
select
    IFNULL(eqprob.posting_date, eqprob.modified),
    eq.name,
    eq.indicator,
    eq.status,
    eq.item_code,
    eq.location,
    doctype.name,
    eqprob.status,
    eqprob.name

from
    `tabEquipment` eq,`tabProblem Report` eqprob,`tabDocType` doctype
where
    eq.name = eqprob.equipment and
    eq.name = "{1}" and
    doctype.name = 'Problem Report'

union
select
    IFNULL(eqlog.posting_date, eqlog.modified),
    eq.name,
    eq.indicator,
    eq.status,
    eq.item_code,
    eq.location,
    doctype.name,
    eqlog.status,
    eqlog.name
    
from
    `tabEquipment` eq,`tabEquipment Log` eqlog,`tabDocType` doctype
where
    eq.name = eqlog.equipment and
    eq.name = "{2}" and
    doctype.name = 'Equipment Log'

union
select
    IFNULL(rf.posting_date, rf.modified),
    eq.name,
    eq.indicator,
    eq.status,
    eq.item_code,
    eq.location,
    doctype.name,
    null,
    rf.name
    
from
    `tabEquipment` eq,`tabRFID Trace` rf,`tabDocType` doctype
where
    eq.name = rf.equipment and
    eq.name = "{3}" and
    doctype.name = 'RFID Trace'

union
select
    IFNULL(mem.posting_date, mem.modified),
    eq.name,
    eq.indicator,
    eq.status,
    eq.item_code,
    eq.location,
    doctype.name,
    mem.type,
    mem.name
    
from
    `tabEquipment` eq,`tabManual Equipment Movement` mem,`tabDocType` doctype
where
    eq.name = mem.equipment and
    eq.name = "{4}"  and
    doctype.name = 'Manual Equipment Movement'
    order by `pd` desc'''.format(equipment,equipment,equipment,equipment,equipment)
	data = frappe.db.sql(query)
	return data