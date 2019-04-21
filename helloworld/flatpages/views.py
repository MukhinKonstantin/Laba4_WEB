# -*- coding: utf-8 -*-
#vim:fileencoding=utf-8
from django.http import HttpResponse

def home(request):
 return HttpResponse(u'Hello, World!', content_type="text/plain")
