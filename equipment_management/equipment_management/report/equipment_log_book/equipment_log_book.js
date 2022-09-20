frappe.query_reports["Equipment Log Book"] = {
	onload: function(report) {
		frappe.views.QueryReport.prototype.add_card_button_to_toolbar = () => {}
		frappe.views.QueryReport.prototype.add_chart_buttons_to_toolbar = () => {}
	}
}