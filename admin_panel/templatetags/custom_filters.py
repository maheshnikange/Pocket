from django import template
import base64
register = template.Library()

@register.filter(name='image_to_base64')
def image_to_base64(image):
    if image == '':
        return ''
    data = base64.b64encode(image.content).decode('utf-8')
    return data
