from django import template
register = template.Library()

@register.filter(name='resolve')
def resolve(list, index):
    return list[index]