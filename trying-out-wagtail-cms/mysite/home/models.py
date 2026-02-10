from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField


class HomePage(Page):
    body = RichTextField(blank=True) # blank true -> not mandatory, can leave empty
    
    # add body to layout of editing interface
    content_panels = Page.content_panels + ["body"]
