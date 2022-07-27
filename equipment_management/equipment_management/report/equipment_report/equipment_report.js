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
		},
	],
	formatter: function (value, cell, columnDef, row) {
		
		if (columnDef.fieldname === "name")
			value  = `<a href='/app/equipment/${value}' target=_blank> ${value} </a>`;

		if (columnDef.fieldname === "status") {
			if (row.indicator===1) {
                return `<span class="ellipsis" title="Status: ${value}">
                <span class="filterable indicator-pill green ellipsis" data-filter="status,=,${value}">
                    <span class="ellipsis"> ${value} </span>
                </span>
            </span>`
            }
            else if (row.indicator===2) {
                return `<span class="ellipsis" title="Status: ${value}">
                <span class="filterable indicator-pill orange ellipsis" data-filter="status,=,${value}">
                    <span class="ellipsis"> ${value} </span>
                </span>
            </span>`
            }
            else if (row.indicator===3) {
                return `<span class="ellipsis" title="Status: ${value}">
                <span class="filterable indicator-pill red ellipsis" data-filter="status,=,${value}">
                    <span class="ellipsis"> ${value} </span>
                </span>
            </span>`
            } else {
                return `<span class="ellipsis" title="Status: ${value}">
                <span class="filterable indicator-pill gray ellipsis" data-filter="status,=,${value}">
                    <span class="ellipsis"> ${value} </span>
                </span>`
            }
		}
		return value
	}
};