from frappe import _

def get_data():
    return [
        {
			"label": _("Project"),
			"items": [
                {
					"type": "doctype",
					"name": "Project",
					"description": _("recruitpro"),
					"onboard": 1,
				},
                {
					"type": "doctype",
					"name": "Position",
					"description": _("recruitpro"),
					"onboard": 1,
				},
            ]
        }
        
			
       
    ]
