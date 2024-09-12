frappe.pages['list-of-equipment-pa'].on_page_load = function(wrapper) {
    var page = frappe.ui.make_app_page({
        parent: wrapper,
        title: 'List of Equipment',
        single_column: true
    });

    $(frappe.render_template("list_of_equipment_pa", {})).appendTo(page.body);

    // Fetch and render data
    function fetchData(filters) {
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

    // Fetch data on page load
    fetchData({});

    function renderTable(rows){
        const datatable = new frappe.DataTable('#datatable', {
            columns: ["ID", "item Code", "Location", "Location Status", "Category", "Status", "Serial Number"],
            data: rows,
            checkboxColumn: true,
            inlineFilters: true
        });
    }

    frappe.applyFilters = function applyFilters() {
        var filters = {
            name: document.getElementById("filter-name").value.trim(),
            status: document.getElementById("filter-status").value.trim(),
            item_code: document.getElementById("filter-item").value.trim(),
            category: document.getElementById("filter-category").value.trim(),
        };
        fetchData(filters);
    }

    var apply_awesomplete = function(fieldname, doctype){
        var awesomplete = new Awesomplete(document.getElementById(fieldname), {
            minChars: 0,
            autoFirst: true,
            replace: function (text) {
                this.input.value = text.value;
            }
        });

        document.getElementById(fieldname).addEventListener("input", function () {
            if (this.value.length >= 0) {
                frappe.call({
                    method: "frappe.client.get_list",
                    args: {
                        doctype: doctype,
                        fields: ["name"],
                        filters: { "name": ["like", "%" + this.value + "%"] },
                        limit: 10
                    },
                    callback: function (response) {
                        var list = response.message.map(function (item) {
                            return { label: item.name, value: item.name };
                        });
                        awesomplete.list = list;
                    }
                });
            }
        });
    }

    apply_awesomplete("filter-name", "Equipment")
    apply_awesomplete("filter-item", "Item")
    apply_awesomplete("filter-category", "Item Group")
};
