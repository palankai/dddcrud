from .messaging import evt


ContactCreated = evt('contact_created', 'name', 'phone')
ContactUpdated = evt('contact_updated', 'name', 'phone')
ContactDeleted = evt('contact_deleted', 'name')
