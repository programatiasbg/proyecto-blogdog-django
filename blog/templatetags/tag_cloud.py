from django import template
from taggit.models import Tag

register = template.Library()


@register.inclusion_tag("blog/components/tag-cloud.html")
def tag_cloud():
    return {"tags": Tag.objects.all()}
