from eve.utils import config

from eve_sqlalchemy.decorators import registerSchema

from tables import People, Invoices

ID_FIELD = 'id'
config.ID_FIELD = ID_FIELD
RESOURCE_METHODS = ['GET', 'POST']

registerSchema('people')(People)
registerSchema('invoices')(Invoices)

DEBUG = True

DOMAIN = {
    'people': People._eve_schema['people'],
    'Invoices': Invoices._eve_schema['invoices']
}

# but you can always customize it:
DOMAIN['people'].update({
    'item_title': 'person',
    'additional_lookup': {
        'url': 'regex("[0-9]+")',
        'field': 'id'
    },
    'cache_control': 'max-age=10,must-revalidate',
    'cache_expires': 10,
    'resource_methods': ['GET', 'POST', 'DELETE']
})
