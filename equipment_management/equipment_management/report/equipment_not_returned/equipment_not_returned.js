// Copyright (c) 2023, Deepak Kumar and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Equipment Not Returned"] = {
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
			default: "Working"
		},
		{
			label: "Item Code",
			fieldname: "item_code",
			fieldtype: "Link",
			options: "Item",
		},
		{
			label: "Days Since Equipment Not Returned",
			fieldname: "compare_days",
			fieldtype: "Data",
		},
	],
	onload: function (report) {
		frappe.views.QueryReport.prototype.add_card_button_to_toolbar = () => { }
		frappe.views.QueryReport.prototype.add_chart_buttons_to_toolbar = () => { }
	},
	formatter: function (value, cell, columnDef, row) {

		if (columnDef.fieldname === "name")
			value = `<a href='/app/equipment/${value}' target=_blank> ${value} </a>`;

		if (columnDef.fieldname === "status") {
			if (row.indicator === 1) {
				return `<span class="ellipsis" title="Status: ${value}">
			<span class="filterable indicator-pill green ellipsis" data-filter="status,=,${value}">
				<span class="ellipsis"> ${value} </span>
			</span>
		</span>`
			}
			else if (row.indicator === 2) {
				return `<span class="ellipsis" title="Status: ${value}">
			<span class="filterable indicator-pill orange ellipsis" data-filter="status,=,${value}">
				<span class="ellipsis"> ${value} </span>
			</span>
		</span>`
			}
			else if (row.indicator === 3) {
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
}