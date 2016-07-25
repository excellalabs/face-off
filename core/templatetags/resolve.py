from django import template
register = template.Library()

@register.filter(name='resolve')
def resolve(list_obj, index):
    return list_obj[index]
