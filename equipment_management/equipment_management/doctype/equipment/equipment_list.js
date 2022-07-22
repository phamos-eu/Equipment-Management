frappe.listview_settings['Equipment'] = {
    add_fields: ["indicator"],
    formatters: {
        status(val, d, f) {
    
            if (f.indicator===1) {
                return `<span class="ellipsis" title="Status: ${val}">
                <span class="filterable indicator-pill green ellipsis" data-filter="status,=,${val}">
                    <span class="ellipsis"> ${val} </span>
                </span>
            </span>`
            }
            else if (f.indicator===2) {
                return `<span class="ellipsis" title="Status: ${val}">
                <span class="filterable indicator-pill orange ellipsis" data-filter="status,=,${val}">
                    <span class="ellipsis"> ${val} </span>
                </span>
            </span>`
            }
            else if (f.indicator===3) {
                return `<span class="ellipsis" title="Status: ${val}">
                <span class="filterable indicator-pill red ellipsis" data-filter="status,=,${val}">
                    <span class="ellipsis"> ${val} </span>
                </span>
            </span>`
            } else {
                return `<span class="ellipsis" title="Status: ${val}">
                <span class="filterable indicator-pill gray ellipsis" data-filter="status,=,${val}">
                    <span class="ellipsis"> ${val} </span>
                </span>`
            }
            
        }
    },
    onload: function(listview) {
        // if (cur_list.view === "Report") {
        //     frappe.set_route('query-report','Equipment Report')
        // }
        cur_list.page.add_button(__('Equipment Report'), function () {
			frappe.set_route('query-report', 'Equipment Report');
		});
    }
}