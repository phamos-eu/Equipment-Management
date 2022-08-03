from . import __version__ as app_version

app_name = "equipment_management"
app_title = "Equipment Management"
app_publisher = "Deepak Kumar"
app_description = "Equipment Management"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "deepak@korecent.com"
app_license = "MIT"

# Includes in <head>
# ------------------

fixtures = ["Workspace","Role","Custom DocPerm","Web Page"]
# include js, css files in header of desk.html
# app_include_css = "/assets/equipment_management/css/equipment_management.css"
app_include_js = "/assets/js/equipment_management.min.js"

# include js, css files in header of web template
# web_include_css = "/assets/equipment_management/css/equipment_management.css"
# web_include_js = "/assets/equipment_management/js/equipment_management.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "equipment_management/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "equipment_management.install.before_install"
after_install = ["equipment_management.migrate.update_equipment_status_on_migrate"]

# Uninstallation
# ------------

# before_uninstall = "equipment_management.uninstall.before_uninstall"
# after_uninstall = "equipment_management.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "equipment_management.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Problem Report": {
		"on_update": "equipment_management.equipment_management.doctype.problem_report.problem_report.update_equipment_status",
	}
}

after_migrate = ["equipment_management.migrate.update_equipment_status_on_migrate"]
# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"equipment_management.tasks.all"
# 	],
# 	"daily": [
# 		"equipment_management.tasks.daily"
# 	],
# 	"hourly": [
# 		"equipment_management.tasks.hourly"
# 	],
# 	"weekly": [
# 		"equipment_management.tasks.weekly"
# 	]
# 	"monthly": [
# 		"equipment_management.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "equipment_management.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "equipment_management.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "equipment_management.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"equipment_management.auth.validate"
# ]

# Translation
# --------------------------------

# Make link fields search translated document names for these DocTypes
# Recommended only for DocTypes which have limited documents with untranslated names
# For example: Role, Gender, etc.
# translated_search_doctypes = []
