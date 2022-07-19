// Copyright (c) 2022, Deepak Kumar and contributors
// For license information, please see license.txt

frappe.ui.form.on('Manual Equipment Movement', {
	refresh: function(frm) {
		if (frm.is_new()) {
			frm.set_df_property('edit_posting_time','hidden',0)
		}
		cur_frm.add_custom_button(__('Ledger'), function () {
			frappe.set_route('query-report', 'Equipment Ledger',
					{equipment: frm.doc.equipment});
		});
	},
	edit_posting_time: function(frm) {
		if (frm.is_new()) {
			if (frm.doc.edit_posting_time) {
				frm.set_df_property('posting_date','read_only',0)
				frm.set_df_property('posting_time','read_only',0)
			} else {
				frm.set_df_property('posting_date','read_only',1)
				frm.set_df_property('posting_time','read_only',1)
			}
		}
	}
});
