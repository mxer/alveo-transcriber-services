from application.misc.events import handle_api_event
from .helper_lists import datastore_list

@handle_api_event('alveo', 'datastore:list')
def alveo_datastore_list(user_id, revision):
    return datastore_list(user_id=user_id, revision=revision)
