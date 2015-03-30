from mezzanine.pages.models import Page
from mezzanine.utils.views import render
from mezzanine.blog.models import BlogPost
from django.template import Context,loader,RequestContext
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.template.loader import render_to_string,get_template
from datetime import datetime
from django.contrib.sitemaps import GenericSitemap
from mezzanine.blog.models import BlogPost
from mezzanine.pages.models import RichTextPage
def direct_to_template(request, template, extra_context=None, **kwargs):
    """
    Replacement for Django's ``direct_to_template`` that uses
    ``TemplateResponse`` via ``mezzanine.utils.views.render``.
    """
    context = extra_context or {}
    context["params"] = kwargs
    for (key, value) in context.items():
        if callable(value):
            context[key] = value()

    posts = []
    latest_post = BlogPost.objects.filter(status = 2).order_by('-created')[0:3]
    for post in latest_post:
        posts.append(post.__dict__)
    context["posts"] = posts
    context["posts_len"] = len(posts)
    # import pdb;pdb.set_trace()
    from django.utils import timezone
    context["now_date"] = timezone.now()
    return render(request, template, context)

def email_store(request):
    import re
    subject = "Aptuz Technology Solutions" 
    to = ['sagar@aptuz.com']
    from_email = 'test@example.com'
     
    if not re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", request.GET["email"]):
        return HttpResponse('Invaild Request')
    else:
        ctx = {
            'name' : request.GET["name"],
            'email' : request.GET["email"],
            'subj' : request.GET["subj"],
            'msg' : request.GET["msg"],
        }

        message = get_template('mail.html').render(Context(ctx))
        msg = EmailMessage(subject, message, to=to, from_email=from_email)
        msg.content_subtype = 'html'
        msg.send()

        return HttpResponse('success')

def my_sitemap(request,**kwargs):
    from django.contrib.sitemaps.views import sitemap
    blog_dict = {
        'queryset': BlogPost.objects.published(),
        'date_field': 'created',
    }
    page_dict = {
        'queryset': RichTextPage.objects.published(),
    }

    sitemaps = {
        'pages': GenericSitemap(page_dict, priority = 0.8, changefreq = "always"),
        'blog': GenericSitemap(blog_dict, priority=0.6, changefreq = "always"),
    }

    return sitemap(request,sitemaps)
