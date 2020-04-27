from frappe import _

def get_data():
    return [
        {
			"label": _("RecruitPRO"),
			"items": [
                {
					"type": "doctype",
					"name": "Candidate",
					"description": _("recruitpro"),
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Sub Agent",
					"description": _("recruitpro"),
					"onboard": 1,
				},
				 {
					"type": "doctype",
					"name": "Mobilization",
					"description": _("recruitpro"),
					"onboard": 1,
				},
			
               
            ]
        }
        
       
    ]
