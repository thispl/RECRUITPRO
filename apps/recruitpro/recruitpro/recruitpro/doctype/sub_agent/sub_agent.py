# -*- coding: utf-8 -*-
# Copyright (c) 2020, teampro and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
# import frappe
from frappe.model.document import Document

class SubAgent(Document):
	pass

# @frappe.whitelist()
# def sams_sa_allocated(sa_agent):
#     allocated = frappe.db.sql("""
#         SELECT c.project,count(c.pending_for) as total_sa,
#         (SELECT COUNT(pending_for) as count1 FROM `tabCandidate` cc WHERE cc.pending_for = 'Proposed PSL' AND 
#         cc.sa_agent = sa.name) as selected,
#         (SELECT status FROM `tabProject` p WHERE p.status IN ('Completed','Cancelled','Open','Overdue','Hold','DnD') AND 
#         p.name = c.project) as status,
#         (SELECT territory FROM `tabProject` pp WHERE pp.territory IS NOT NULL AND 
#         pp.name = c.project) as territory
#         FROM `tabCandidate` c 
#         JOIN `tabProject` sa ON  sa.name = c.project
#         WHERE c.sa_agent='%s' AND c.pending_for IN ('Submitted','Interviewed','Linedup','Shortlisted','IDB','Proposed PSL','Sourced')
#         GROUP BY sa.name
#         """ %(sa_agent),as_dict=1)
#     # frappe.errprint(allocated)
#     return(allocated) 