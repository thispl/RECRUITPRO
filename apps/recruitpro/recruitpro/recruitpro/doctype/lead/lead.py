# -*- coding: utf-8 -*-
# Copyright (c) 2020, teampro and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
# import frappe
from frappe.model.document import Document

class Lead(Document):
	pass
# @frappe.whitelist()

# def make_customer(source_name, target_doc=None):
# 	return _make_project(source_name, target_doc)

# def _make_customer(source_name, target_doc=None, ignore_permissions=False):	
# 	doclist = get_mapped_doc("Lead", source_name,
# 		{"Lead": {
# 			"doctype": "Customer",
# 			"field_map": {
# 				"lead": "from_lead"
# 				# "contact_no": "phone_1",
# 				# "fax": "fax_1"
# 			}
# 		}}, ignore_permissions=ignore_permissions)

# 	return doclist