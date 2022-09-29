// Copyright (c) 2022, Deepak Kumar and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Equipment Log Book"] = {
	"filters": [
		{
			"fieldname": "equipment",
			"fieldtype": "Link",
			"label": "Equipment",
			"mandatory": 1,
			"options": "Equipment",
			"wildcard_filter": 0
		   }
	],

	onload: function(report) {
		frappe.views.QueryReport.prototype.add_card_button_to_toolbar = () => {}
		frappe.views.QueryReport.prototype.add_chart_buttons_to_toolbar = () => {}
	},

	formatter: function (value, cell, columnDef, row) {
		if (columnDef.fieldname === "equipment_status") {
			
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
