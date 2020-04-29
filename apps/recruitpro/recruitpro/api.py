import frappe
import json
# import shortuuid
import qrcode
import base64
from PIL import Image
from io import BytesIO
from frappe import _
from frappe.utils.data import today
from frappe.utils import datetime, nowdate, add_days, flt
from frappe.utils.print_format import download_pdf
from datetime import date


@frappe.whitelist()
def create_mobilization(doc, method):
    if doc.pending_for == 'Proposed PSL':
        frappe.errprint(doc.name)
        mobilization_id = frappe.db.get_value("Mobilization", {"candidate": doc.name})
        # interview = frappe.db.get("Candidate", docs.candidate)
        # if interview:
        #     interview_date = interview.interview_date
        project = frappe.get_doc("Project", doc.project)
        position = frappe.db.get_value("Position", doc.position, "subject")
        # territory = frappe.db.get_value("Customer", doc.customer, "territory")
        payment_terms = project.payment_terms
        if mobilization_id:
            mobilization = frappe.get_doc("Mobilization", mobilization_id)
        else:
            mobilization = frappe.new_doc("Mobilization")
        mobilization.update({
            "customer": doc.customer,
            "territory": territory,
            "project": doc.project,
            "payment_terms": payment_terms,
            "position": doc.position,
            "candidate": doc.name,
            "name1": doc.given_name,
            "designation": task,
            "contact_no": doc.mobile,
            "current_location": doc.current_location,
            "passport_no": doc.passport_no,
            "ecr_status": doc.ecr_status,
            "associate_name": doc.associate_name,
            "associate": doc.associate,
            "associate_contact_no": doc.contact_no,
            "expiry_date": doc.expiry_date,
            "date_of_issue": doc.issued_date,
            "place_of_issue": doc.place_of_issue,
            "cr_executive": project.cpc,
            "ca_executive": ca_executive,
            "department": department,
            "source_executive": source_executive,
            "selection_date": doc.interview_date,
            "tl": tl,
            "degree": doc.degree,
            "specialization": doc.specialization,
            "yop": doc.yop,
            "basic": doc.basic,
            "food": doc.food,
            "other_allowances": doc.other_allowances,
            "dob": doc.dob
        })
        
        mobilization.save(ignore_permissions=True)
