from django import template

register = template.Library()


@register.inclusion_tag('_stars.html')
def show_stars(count):
    return {
        'star_count': range(int(count)),
        'leftover_count': range(int(count), 5)
    }