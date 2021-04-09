from django import template

register = template.Library()

# This function has as purpose to concatenate querystrings together if multiple are set.
# Example is filtering on city and paginating on this ?page=2&city=20


@register.simple_tag
def my_url(value, field_name, urlencode=None):
    url = f'?{field_name}={value}'

    if urlencode:
        querystring = urlencode.split('&')
        filtered_querystring = filter(
            lambda p: p.split('=')[0] != field_name, querystring)
        encoded_querystring = '&'.join(filtered_querystring)
        url = f'{url}&{encoded_querystring}'

    return url
