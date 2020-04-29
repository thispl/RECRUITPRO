# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "recruitpro"
app_title = "recruitpro"
app_publisher = "teampro"
app_description = "app recruitpro"
app_icon = "octicon octicon-file-directory"
app_color = "blue"
app_email = "sharmila.h@teampro.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/recruitpro/css/recruitpro.css"
# app_include_js = "/assets/recruitpro/js/recruitpro.js"

# include js, css files in header of web template
# web_include_css = "/assets/recruitpro/css/recruitpro.css"
# web_include_js = "/assets/recruitpro/js/recruitpro.js"

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

# Website user home page (by function)
# get_website_user_home_page = "recruitpro.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "recruitpro.install.before_install"
# after_install = "recruitpro.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "recruitpro.notifications.get_notification_config"

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

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }
doc_events = {
    "Candidate": {
        "on_update": "recruitpro.api.create_mobilization"
    }
    "Position Candidate": {
        "on_update": "recruitpro.api.create_mobilization"
    },
    # "Project": {
    #    "on_update": "recruitment.utils.apply_perm"
    # }
}
# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"recruitpro.tasks.all"
# 	],
# 	"daily": [
# 		"recruitpro.tasks.daily"
# 	],
# 	"hourly": [
# 		"recruitpro.tasks.hourly"
# 	],
# 	"weekly": [
# 		"recruitpro.tasks.weekly"
# 	]
# 	"monthly": [
# 		"recruitpro.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "recruitpro.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "recruitpro.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "recruitpro.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

