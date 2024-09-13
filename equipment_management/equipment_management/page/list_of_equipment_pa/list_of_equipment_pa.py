import frappe, json

def get_conditions(filters):
	if type(filters) == str:
		filters = json.loads(filters or {})
	conditions = {}

	if "name" in filters and filters["name"]:
		conditions["name"] = filters["name"]
		return conditions

	if "status" in filters and filters["status"]:
		conditions["status"] = filters["status"]

	if "item_code" in filters and filters["item_code"]:
		conditions["item_code"] = filters["item_code"]

	if "category" in filters and filters["category"]:
		conditions["category"] = filters["category"]

	return conditions

@frappe.whitelist()
def get_data(filters):
	conditions = get_conditions(filters)
	data = frappe.db.get_all("Equipment", 
						  fields=['name',
						  'item_code',
						  'storage_location',
						  'location_status',
						  'category',
						  'status',
						  'serial_number',
						  ], 
						  filters=conditions, 
						  order_by='name',
						  as_list=True)
	new_data = []
	for d in data:
		new_data.append(list(d))
	return new_data