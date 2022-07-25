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
		cur_frm.add_custom_button(__('View Log Book'), function () {
			frappe.set_route('query-report', 'Equipment Ledger',
					{equipment: frm.doc.name});
		});

		cur_frm.add_custom_button(__('Report a Problem'), function () {
			frappe.set_route('problem-report','new-problem-report',
					{equipment: frm.doc.name});
			
		},__('Problem & Maintenance'));

		cur_frm.add_custom_button(__('Perform Equipment Maintenance'), function () {
			frappe.new_doc("Equipment Maintenance", "new-equipment-maintenance", doc => {
				doc.equipment = frm.doc.name
				frm.doc.maintenance_tasks.forEach((row,index) => {
					let table = frappe.model.add_child(doc,'maintenance_tasks')
					table.task = row.task
					table.status = row.status
					table.description = row.description
				})
				cur_frm.refresh_fields('maintenance_tasks')
			});
			
		},__('Problem & Maintenance'));

		cur_frm.add_custom_button(__('Scrap'), function () {
			frappe.set_route('manual-equipment-movement','new-manual-equipment-movement',
					{equipment: frm.doc.name, type: 'Scrap'});
			
		},__('Manual Equipment Movement'));

		cur_frm.add_custom_button(__('Loan'), function () {
			frappe.set_route('manual-equipment-movement','new-manual-equipment-movement',
					{equipment: frm.doc.name, type: 'Loan'});
			
		},__('Manual Equipment Movement'));

		cur_frm.add_custom_button(__('Send to Repair'), function () {
			frappe.set_route('manual-equipment-movement','new-manual-equipment-movement',
					{equipment: frm.doc.name, type: 'Repair'});
			
		},__('Manual Equipment Movement'));
	
		if (!frappe.user.has_role('System Manager') && frappe.user.has_role('eusectra basic User')) {
			frm.set_df_property('status', 'hidden',1)
		}
		// Hide + button
		$('button[data-doctype="Problem Report"]').hide()
		$('button[data-doctype="Equipment Maintenance"]').hide()
		$('button[data-doctype="Manual Equipment Movement"]').hide()
		
	}
});