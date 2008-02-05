import resources

import zope.security.management
import zope.security.interfaces

from zope.publisher.interfaces import IRequest

def getRequest():
    try:
        i = zope.security.management.getInteraction() # raises NoInteraction
    except zope.security.interfaces.NoInteraction:
        return

    for p in i.participations:
        if IRequest.providedBy(p):
            return p

def need(library_name):
    request = getRequest()
    # only take note of needed libraries if there is a request, and it is
    # capable of handling resource librarys
    if request and hasattr(request, 'resource_libraries'):
        if not library_name in request.resource_libraries:
            request.resource_libraries.append(library_name)

def getRequired(name):
    return resources.library_info[name].required

def getIncluded(name):
    return resources.library_info[name].included
    
