// Copyright (c) 2022, Deepak Kumar and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Equipment Report"] = {
	"filters": [
		{
			label: "Name",
			fieldname: "name",
			fieldtype: "Link",
			options: "Equipment",
		},
		{
			label: "Status",
			fieldname: "status",
			fieldtype: "Select",
			options: "\nWorking\nNot Working",
		},
		{
			label: "Item Code",
			fieldname: "item_code",
			fieldtype: "Link",
			options: "Item",
		},
		{
			label: "Category",
			fieldname: "category",
			fieldtype: "Link",
			options: "Item Group",
		}
	]
};
