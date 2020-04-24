# -*- coding: utf-8 -*-
# Copyright (c) 2020, teampro and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
# import frappe
from frappe.model.document import Document

class Position(Document):
	pass
@frappe.whitelist()
def sa_candidate(position,project):
    allocated = frappe.db.sql("""
        SELECT sa_agent,sa_name,sa_mobile_number,count(sa_agent) as achieved_count,
        (SELECT COUNT(pending_for) as count1 FROM `tabCandidate` cc WHERE cc.position= '%s' and cc.pending_for = 'IDB' AND 
        cc.sa_agent = sa.name) as selected,
        (SELECT COUNT(pending_for) as count2 FROM `tabCandidate` cfp WHERE cfp.position= '%s' AND cfp.pending_for IN ('Submitted','Interviewed') AND
        cfp.sa_agent = sa.name) as fp,
        (SELECT COUNT(pending_for) as count3 FROM `tabCandidate` csl WHERE csl.position= '%s' AND csl.pending_for IN ('Linedup','Shortlisted') AND
        csl.sa_agent = sa.name) as sl,
        (SELECT COUNT(pending_for) as count4 FROM `tabCandidate` cpsl WHERE cpsl.position= '%s' AND  cpsl.pending_for ='Proposed PSL' AND 
        cpsl.sa_agent = sa.name) as psl,
        (SELECT COUNT(pending_for) as count5 FROM `tabCandidate` csp WHERE csp.position= '%s' AND csp.pending_for ='Sourced' AND 
        csp.sa_agent = sa.name) as sp,
        (SELECT COUNT(pending_for) as count6 FROM `tabCandidate` tsa WHERE tsa.position= '%s' AND tsa.pending_for IN ('Submitted','Interviewed','Linedup','Shortlisted','IDB','Proposed PSL','Sourced') AND 
        tsa.sa_agent = sa.name) as tsa
        FROM `tabCandidate` c 
        JOIN `tabSub Agent` sa ON  sa.name = c.sa_agent 
        WHERE c.position='%s' AND c.sa_agent IS NOT NULL AND c.task IS NOT NULL GROUP BY sa.name
        """ %(position,position,position,position,position,position,position),as_dict=1)
    frappe.errprint(allocated)
    return(allocated)    