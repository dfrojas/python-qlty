import json

from django.contrib import admin
from django.utils.safestring import mark_safe

from core.models import Snippet

# from pygments import highlight
# from pygments.lexers import JsonLexer
# from pygments.formatters import HtmlFormatter


class SnippetAdmin(admin.ModelAdmin):
    list_display = ('id', 'slug', 'result', )

admin.site.register(Snippet, SnippetAdmin)
