setTimeout(() => {
    frappe.web_form.set_value('posting_time',frappe.datetime.now_time())
}, 100);