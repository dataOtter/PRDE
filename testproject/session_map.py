import flask as f
import uuid
from faceted_search import faceted_search_filter_instances as pidf

# global variable: map from guid to FilterSystem

def get_new_guid_for_fs(app):
    """return a guid which maps to a FilterSystem"""
    fs = pidf.FilterSystem()
    guid = str(uuid.uuid1())

    if not hasattr(app.config, 'session_map'):
        print('SESSION_MAP: session_map made')
        app.config.session_map = {}

    app.config.session_map[guid] = fs
    print ("SESSION_MAP: Guid made: " + guid)

    return guid


def get_FilterSystem(guid,app):
    """return a FilterSystem corresponding to a guid"""

    if not hasattr(app.config, 'session_map'):
        print('SESSION_MAP: session_map lost')

    if guid in app.config.session_map.keys():
        answer = app.config.session_map[guid]
    else:
        print ("SESSION_MAP: Guid lost: " + guid)
        return

    return answer


def update_FilterSystem(guid, fs, app):
    """Update the fs associated with a guid"""

    if not hasattr(app.config, 'session_map'):
        print('SESSION_MAP: session_map lost')

    if guid not in app.config.session_map.keys():
        print ("SESSION_MAP: Guid lost: " + guid)
        return

    app.config.session_map[guid] = fs

