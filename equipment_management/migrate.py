import frappe

def update_equipment_status_on_migrate():
    equipment = frappe.db.get_list('Equipment', pluck='name')

    for name in equipment:
        equip_doc = frappe.get_doc('Equipment', name)
        if frappe.db.exists("Problem Report", {'equipment':name, 'status':'Open', 'equipment_status':'Not Working'}):
            equip_doc.db_set('indicator', 3, update_modified=False)
            equip_doc.db_set('status', "Not Working", update_modified=False)

        elif frappe.db.exists("Problem Report", {'equipment':name, 'status':'Open', 'equipment_status':'Working'}):
            equip_doc.db_set('indicator', 2, update_modified=False)
            equip_doc.db_set('status', "Working", update_modified=False)
            
        else:
            equip_doc.db_set('indicator', 1, update_modified=False)
            equip_doc.db_set('status', "Working", update_modified=False)