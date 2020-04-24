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
				 
            ]
        },
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
        },
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
			
               
            ]
        },
        {
			"label": _("Mobilization"),
			"items": [
                {
					"type": "doctype",
					"name": "Mobilization",
					"description": _("recruitpro"),
					"onboard": 1,
				},
			
       
    ]
