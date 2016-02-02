# -*- coding: utf-8 -*-


from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from oscar.core.loading import get_class

from demo.apps.dashboard.staticpages.views import *

list_view = get_class('demo.apps.dashboard.staticpages.views', 'PageListView')
create_view = get_class('demo.apps.dashboard.staticpages.views', 'PageCreateView')
update_view = get_class('demo.apps.dashboard.staticpages.views', 'PageUpdateView')
delete_view = get_class('demo.apps.dashboard.staticpages.views', 'PageDeleteView')

urlpatterns = (
      url(r'^$', list_view.as_view(), name='staticpage-list'),
      url(r'^create/$', create_view.as_view(), name='staticpage-create'),
      url(r'^update/(?P<pk>[-\w]+)/$',
          update_view.as_view(), name='staticpage-update'),
      url(r'^delete/(?P<pk>\d+)/$',
          delete_view.as_view(), name='staticpage-delete')
)

