frappe.ready(function() {
	// bind events here
	frappe.web_form.after_load = () => {
		frappe.web_form.set_value('posting_time',frappe.datetime.now_time())
	}
})