# -*- coding: utf-8 -*-
# Copyright (c) 2020, teampro and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
# import frappe
from frappe.model.document import Document

class Project(Document):
	pass

# @frappe.whitelist()
# def project_sa_candidate(project):
#     allocated = frappe.db.sql("""
#         SELECT sa_agent,sa_name,sa_mobile_number,count(sa_agent) as achieved_count,
#         (SELECT COUNT(pending_for) as count1 FROM `tabCandidate` cc WHERE cc.project= '%s' AND cc.pending_for = 'IDB' AND 
#         cc.sa_agent = sa.name) as selected,
#         (SELECT COUNT(pending_for) as count2 FROM `tabCandidate` cfp WHERE cfp.project= '%s' AND cfp.pending_for IN ('Submitted','Interviewed') AND
#         cfp.sa_agent = sa.name) as fp,
#         (SELECT COUNT(pending_for) as count3 FROM `tabCandidate` csl WHERE csl.project= '%s' AND csl.pending_for IN ('Linedup','Shortlisted') AND
#         csl.sa_agent = sa.name) as sl,
#         (SELECT COUNT(pending_for) as count4 FROM `tabCandidate` cpsl WHERE cpsl.project= '%s' AND  cpsl.pending_for ='Proposed PSL' AND 
#         cpsl.sa_agent = sa.name) as psl,
#         (SELECT COUNT(pending_for) as count5 FROM `tabCandidate` csp WHERE csp.project= '%s' AND csp.pending_for ='Sourced' AND 
#         csp.sa_agent = sa.name) as sp,
#         (SELECT COUNT(pending_for) as count6 FROM `tabCandidate` tsa WHERE tsa.project= '%s' AND tsa.pending_for IN ('Submitted','Interviewed','Linedup','Shortlisted','IDB','Proposed PSL','Sourced') AND 
#         tsa.sa_agent = sa.name) as tsa
#         FROM `tabCandidate` c 
#         JOIN `tabSub Agent` sa ON  sa.name = c.sa_agent 
#         WHERE c.project='%s'AND c.sa_agent IS NOT NULL AND c.project IS NOT NULL GROUP BY sa.name
#         """ %(project,project,project,project,project,project,project),as_dict=1)
#     return(allocated) 

# @frappe.whitelist()
# def count_task(project):
#     position = frappe.db.count('Position',{'project':project})
#     count = frappe.db.sql("select sum(vac),sum(sp),sum(fp),sum(sl),sum(psl) from `tabPosition` where `project` = %s",project)
#     return position, count
    