from __future__ import unicode_literals
from frappe import _

def get_data():
	return {
		'heatmap': True,
		'heatmap_message': _('This is based on the Time Sheets created against this customer'),
		'fieldname': 'customer',
		'transactions': [
			{
				'label': _('Customer'),
				'items': ['Project']
			},
			
		]
}