frappe.pages['list-of-equipment-pa'].on_page_load = function(wrapper) {
    var page = frappe.ui.make_app_page({
        parent: wrapper,
        title: 'List of Equipment',
        single_column: true
    });

    $(frappe.render_template("list_of_equipment_pa", {})).appendTo(page.body);

    // Fetch and render data
    frappe.fetchData = function fetchData(filters) {
        frappe.call({
            method: 'equipment_management.equipment_management.report.list_of_equipment.list_of_equipment.get_data',
            args: {
                filters: filters
            },
            callback: function(r) {
                let rows = r.message;
                renderTable(rows);
            }
        });
    }

    add_filters(page)

    // Fetch data on page load
    frappe.fetchData({});

    function renderTable(rows){
        const datatable = new frappe.DataTable('#datatable', {
            columns: [
                {
                    name: "ID",
                    width: 150,
                    editable: false
                }, 
                {
                    name: "Item Code",
                    width: 230,
                    editable: false
                }, 
                {
                    name: "Location",
                    width: 150,
                    editable: false
                }, 
                {
                    name: "Location Status",
                    width: 150,
                    editable: false
                }, 
                {
                    name: "Category",
                    width: 150,
                    editable: false
                }, 
                {
                    name: "Status",
                    width: 150,
                    editable: false
                }, 
                {
                    name: "Serial Number",
                    width: 210,
                    editable: false
                }
            ],
            data: rows,
            checkboxColumn: true,
            inlineFilters: true
        });
    }
};

function add_filters(page){
    let name_filter = page.add_field({
        fieldname: 'name',
        label: 'Equipment Name',
        fieldtype: 'Link',
        options: "Equipment",
        change() {
            let name = name_filter.get_value();
            frappe.fetchData({name: name})
        }
    });

    let status_filter = page.add_field({
        fieldname: 'status',
        label: 'Status',
        fieldtype: 'Select',
        options: ["", "Working", "Not Working"],
        change() {
            let status = status_filter.get_value();
            frappe.fetchData({status: status})
        }
    });

    let item_filter = page.add_field({
        fieldname: 'item',
        label: 'Item',
        fieldtype: 'Link',
        options: "Item",
        change() {
            let item = item_filter.get_value();
            frappe.fetchData({item_code: item})
        }
    });

    let category_filter = page.add_field({
        fieldname: 'category',
        label: 'Category',
        fieldtype: 'Link',
        options: "Item Group",
        change() {
            let category = category_filter.get_value();
            frappe.fetchData({category: category})
        }
    });
}