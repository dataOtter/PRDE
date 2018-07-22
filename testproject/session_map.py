import flask as f
import uuid
from faceted_search import faceted_search_filter_instances as pidf

# global variable: map from guid to FilterSystem
session_map = {}


def get_new_guid_for_fs():
    """return a guid which maps to a FilterSystem"""
    fs = pidf.FilterSystem()
    guid = str(uuid.uuid1())
    session_map[guid] = fs
    print ("SESSION_MAP: Guid made: " + guid)

    f.g.foo = 'abc'
    print('g.foo should be abc, is: {0}'.format(f.g.foo))

    return guid


def get_FilterSystem(guid):
    """return a FilterSystem corresponding to a guid"""
    if guid in session_map.keys():
        answer = session_map[guid]
    else:
        print ("SESSION_MAP: Guid lost: " + guid)
        return

    f.g.foo = 'abc'
    print('g.foo should be abc, is: {0}'.format(f.g.foo))

    return answer


def update_FilterSystem(guid, fs):
    """Update the fs associated with a guid"""
    if guid in session_map.keys():
        answer = session_map[guid]
    else:
        print ("SESSION_MAP: Guid lost: " + guid)
        return

    f.g.foo = 'abc'
    print('g.foo should be abc, is: {0}'.format(f.g.foo))

    session_map[guid] = fs

