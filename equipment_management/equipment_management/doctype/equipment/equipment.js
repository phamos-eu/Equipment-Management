// Copyright (c) 2022, Deepak Kumar and contributors
// For license information, please see license.txt

frappe.ui.form.on('Equipment', {
	// refresh: function(frm) {

	// }
	refresh: function(frm) {
		let report_exist;
		frappe.call({
			method: "equipment_management.equipment_management.doctype.equipment.equipment.problem_report_exist",
			args: {
				name: frm.doc.name
			},
			async: 0,
			callback: function(r){
				if (r.message) {
					report_exist = 1
				} else {
					report_exist = 0
				}
			}
		})
		if (frm.doc.status==="Working" && !report_exist) {
			$('.indicator-pill.whitespace-nowrap').removeClass('gray')
			$('.indicator-pill.whitespace-nowrap').addClass('green')
		} 
		else if (frm.doc.status==="Working" && report_exist) {
			$('.indicator-pill.whitespace-nowrap').removeClass('gray')
			$('.indicator-pill.whitespace-nowrap').addClass('orange')
		} 
		else if (frm.doc.status==="Not Working" && report_exist) {
			$('.indicator-pill.whitespace-nowrap').removeClass('gray')
			$('.indicator-pill.whitespace-nowrap').addClass('red')
		}
	}
});
