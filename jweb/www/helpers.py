from django.core.urlresolvers import reverse

class BreadcrumbException(Exception):
    pass

def generate_breadcrumbs(cd, txt, name=None, url=None):
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

    if url:
        link = url
    elif name:
        link = reverse(name)
    else:
        link = reverse(txt.lower())

    bc += '<a href="{}">{}</a>'.format(link, txt)

    cd['breadcrumbs'] = bc

    return cd

