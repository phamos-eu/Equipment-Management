# Copyright (c) 2023, Deepak Kumar and contributors
# For license information, please see license.txt

import frappe
from frappe import _


def execute(filters=None):
    """ Return report data """
    filters = frappe._dict(filters or {})
    columns = get_columns()
    data = get_data(filters)
    return columns, data


def get_columns():
    """ Return Columns """
    columns = [
        {
            "label": _("ID"),
            "fieldtype": "Link",
            "fieldname": "name",
            "options": "Equipment",
            "width": 200
        },
        {
            "label": _("Item Code"),
            "fieldtype": "Data",
            "fieldname": "item_code",
            "width": 200
        },
        {
            "label": _("Location"),
            "fieldtype": "Data",
            "fieldname": "storage_location",
            "width": 200
        },
        {
            "label": _("Location Status"),
            "fieldtype": "Data",
            "fieldname": "location_status",
            "width": 200
        },
        {
            "label": _("Status"),
            "fieldtype": "Data",
            "fieldname": "status",
            "width": 200
        },
        {
            "label": "Indicator",
            "fieldname": "indicator",
            "fieldtype": "Data",
            "hidden": 1,
        },
        {
            "label": "Days Since Equipment Not Returned",
            "fieldname": "days",
            "fieldtype": "Int",
            "width": 200
        }
    ]
    return columns


def get_conditions(filters):
    """ Condition for report """
    conditions = []

    if filters.name:
        conditions.append(
            ("name", "=", filters.name)
        )

    if filters.status:
        conditions.append(
            ("status", "=", filters.status)
        )

    if filters.item_code:
        conditions.append(
            ("item_code", "=", filters.item_code)
        )

    if filters.compare_days:
        conditions.append(
            ("ABS(DATEDIFF(last_location_date, storage_location_date))",
             ">=", filters.compare_days)
        )

    sql_conditions = []
    for field, compare, value in conditions:
        sql_condition = f'and {field} {compare} "{value}"'
        sql_conditions.append(sql_condition)

    return " ".join(sql_conditions)


def get_data(filters):
    """ Return Data for report"""

    conditions = get_conditions(filters)
    query = f'select name, item_code, storage_location, location_status, status, indicator, \
    		ABS(DATEDIFF(last_location_date, storage_location_date)) as days from `tabEquipment` \
            where storage_location != last_location {conditions} order by name'

    data = frappe.db.sql(query)
    return data
