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
		cur_frm.add_custom_button(__('Ledger'), function () {
			frappe.set_route('query-report', 'Equipment Ledger',
					{equipment: frm.doc.name});
		});

		cur_frm.add_custom_button(__('Report a Problem'), function () {
			frappe.set_route('problem-report','new-problem-report-1',
					{equipment: frm.doc.name});
			
		},__('Problem & Maintenance'));

		cur_frm.add_custom_button(__('Perform Equipment Maintenance'), function () {
			frappe.set_route('equipment-maintenance','new-equipment-maintenance-1',
					{equipment: frm.doc.name});
			
		},__('Problem & Maintenance'));

		cur_frm.add_custom_button(__('Scrap'), function () {
			frappe.set_route('manual-equipment-movement','new-manual-equipment-movement-1',
					{equipment: frm.doc.name, type: 'Scrap'});
			
		},__('Manual Equipment Movement'));

		cur_frm.add_custom_button(__('Loan'), function () {
			frappe.set_route('manual-equipment-movement','new-manual-equipment-movement-1',
					{equipment: frm.doc.name, type: 'Loan'});
			
		},__('Manual Equipment Movement'));

		cur_frm.add_custom_button(__('Send to Repair'), function () {
			frappe.set_route('manual-equipment-movement','new-manual-equipment-movement-1',
					{equipment: frm.doc.name, type: 'Repair'});
			
		},__('Manual Equipment Movement'));
		
	}
});
