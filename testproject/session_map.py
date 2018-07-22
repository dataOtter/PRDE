import flask as f
import uuid
from faceted_search import faceted_search_filter_instances as pidf

from pymemcache.client import base
import pickle

def get_new_guid_for_fs(app):
    """return a guid which maps to a FilterSystem"""
    fs = pidf.FilterSystem()
    guid = str(uuid.uuid1())

    mc = base.Client(('localhost', 11211))
    fs_str = pickle.dumps(fs)    
    mc.set(guid, fs_str)

    print ("SESSION_MAP: Guid made: " + guid)
    
    return guid


def get_FilterSystem(guid,app):
    """return a FilterSystem corresponding to a guid"""

    mc = base.Client(('localhost', 11211))
    fs_str = mc.get(guid)
    fs = pickle.loads(fs_str)
    
    return fs


def update_FilterSystem(guid, fs, app):
    """Update the fs associated with a guid"""

    mc = base.Client(('localhost', 11211))
    fs_str = pickle.dumps(fs)    
    mc.set(guid, fs_str)


