frappe.listview_settings['Equipment'] = {

    formatters: {
        status(val, d, f) {
            let report_exist;
            frappe.call({
                method: "equipment_management.equipment_management.doctype.equipment.equipment.problem_report_exist",
                args: {
                    name: f.name
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

            if (val==="Working" && !report_exist) {
                return `<span class="ellipsis" title="Status: ${val}">
                <span class="filterable indicator-pill green ellipsis" data-filter="status,=,${val}">
                    <span class="ellipsis"> ${val} </span>
                </span>
            </span>`
            } 
            else if (val==="Working" && report_exist) {
                return `<span class="ellipsis" title="Status: ${val}">
                <span class="filterable indicator-pill orange ellipsis" data-filter="status,=,${val}">
                    <span class="ellipsis"> ${val} </span>
                </span>
            </span>`
            } 
            else if (val==="Not Working" && report_exist) {
                return `<span class="ellipsis" title="Status: ${val}">
                <span class="filterable indicator-pill red ellipsis" data-filter="status,=,${val}">
                    <span class="ellipsis"> ${val} </span>
                </span>
            </span>`
            }
            else {
                return `<span class="ellipsis" title="Status: ${val}">
                <span class="filterable indicator-pill gray ellipsis" data-filter="status,=,${val}">
                    <span class="ellipsis"> ${val} </span>
                </span>
            </span>`
            } 
            
        }
    }
}