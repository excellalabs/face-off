from django import template

register = template.Library()

@register.inclusion_tag('cards.html')
def render_cards(cards, round, answer):
    context_for_rendering_inclusion_tag = {'cards': cards, 'round': round, 'answer': answer}
    return context_for_rendering_inclusion_tag