from django import template
from ..models import Post
from django.db.models import Count
from django.utils.safestring import mark_safe
import markdown

# Used to register your own template tags and filters.
register = template.Library()


# Create a simple template tag(simple tags returns a string) that returns the number of posts published.
@register.simple_tag
def total_posts():
    return Post.published.count()


# Tag to display the latest posts in the sidebar of your blog (default 5 posts).
# Inclusion tags processes the data and returns a rendered template.
@register.inclusion_tag('blog/post/latest_posts.html')
def show_latest_posts(count=5):
    latest_posts = Post.published.order_by('-publish')[:count]
    return {'latest_posts': latest_posts}


# Create a tag to display the most commented posts.
@register.simple_tag
def get_most_commented_posts(count=5):
    # The annotate function to aggregate the total number of comments for each post.
    return Post.published.annotate(
        total_comments=Count('comments')).order_by('-total_comments')[:count]


@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))
