from django import template

register = template.Library()

@register.filter
def split_activities(value, delimiter="."):
    """Splits a string by the given delimiter, removes empty items, and adds a hyphen."""
    return ["- " + item.strip() for item in value.split(delimiter) if item.strip()]
