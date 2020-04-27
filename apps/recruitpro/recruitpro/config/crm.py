from frappe import _

def get_data():
    return [
        {
			"label": _("CRM"),
			"items": [
                {
					"type": "doctype",
					"name": "Lead",
					"description": _("recruitpro"),
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Customer",
					"description": _("recruitpro"),
					"onboard": 1,
				},
                {
					"type": "doctype",
					"name": "Sales Order",
					"description": _("recruitpro"),
					"onboard": 1,
				},
                {
					"type": "doctype",
					"name": "Sales Invoice",
					"description": _("recruitpro"),
					"onboard": 1,
				},
				 
            ]
        }
        
       
    ]
