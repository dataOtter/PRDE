
import uuid
from faceted_search import faceted_search_filter_instances as pidf

# global variable: map from guid to FilterSystem
session_map = {}

def get_new_guid_for_fs():
    """return a guid which maps to a FilterSystem"""
    fs = pidf.FilterSystem()
    guid = str(uuid.uuid1())
    session_map[guid] = fs
    return guid

def get_FilterSystem(guid):
    """return a FilterSystem corresponding to a guid"""
    answer = session_map[guid]
    assert(answer, "Guid not found")
    return answer

def update_FilterSystem(guid, fs):
    """Update the fs associated with a guid"""
    answer = session_map[guid]
    assert(answer, "Guid not found")
    session_map[guid] = fs

