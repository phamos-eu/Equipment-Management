// Copyright (c) 2022, Deepak Kumar and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["List of Equipment Maintenance"] = {
	"filters": [
		{
			label: "Name",
			fieldname: "name",
			fieldtype: "Link",
			options: "Equipment Maintenance",
		},
		{
			label: "Status",
			fieldname: "status",
			fieldtype: "Select",
			options: "\nPending\nRepair Needed\nCompleted",
		}
	],
	onload: function(report) {
		frappe.views.QueryReport.prototype.add_card_button_to_toolbar = () => {}
		frappe.views.QueryReport.prototype.add_chart_buttons_to_toolbar = () => {}
	},
	formatter: function (value, cell, columnDef, row) {
		
		if (columnDef.fieldname === "name")
			value  = `<a href='/app/equipment-maintenance/${value}' target=_blank> ${value} </a>`;

		if (columnDef.fieldname === "status") {
			if (value==="Pending") {
                return `<span class="ellipsis" title="Status: ${value}">
                <span class="filterable indicator-pill red ellipsis" data-filter="status,=,${value}">
                    <span class="ellipsis"> ${value} </span>
                </span>
            </span>`
            }
            else if (value==="Repair Needed") {
                return `<span class="ellipsis" title="Status: ${value}">
                <span class="filterable indicator-pill orange ellipsis" data-filter="status,=,${value}">
                    <span class="ellipsis"> ${value} </span>
                </span>
            </span>`
            }
            else if (value==="Completed") {
                return `<span class="ellipsis" title="Status: ${value}">
                <span class="filterable indicator-pill green ellipsis" data-filter="status,=,${value}">
                    <span class="ellipsis"> ${value} </span>
                </span>
            </span>`
            }
		}
		return value
	}
};
