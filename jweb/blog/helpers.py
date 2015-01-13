from types import NoneType

from django.core.urlresolvers import reverse

class BreadcrumbException(Exception):
    pass

def generate_breadcrumbs(cd, txt, name=None, url=None, no_link=False):
    if not isinstance(cd, dict):
        raise BreadcrumbException("argument 'cd' must be of type 'dict'")

    if not isinstance(txt, str):
        raise BreadcrumbException("argument 'txt' must be of type 'str'")

    if name and not isinstance(name, str):
        raise BreadcrumbException("argument 'name' must be of type 'str'")

    if url and not isinstance(url, str):
        raise BreadcrumbException("argument 'url' must be of type 'str'")

    bc = cd.get('breadcrumbs', '')
    link = ''

    if bc:
        bc += ' &raquo; '
    
    if no_link:
        if isinstance(txt, NoneType):
            return cd
        bc += txt
    else:
        if url:
            link = url
        elif name:
            link = reverse(name)
        else:
            link = reverse(txt.lower())
    
        bc += '<a href="{}">{}</a>'.format(link, txt)

    cd['breadcrumbs'] = bc

    return cd

