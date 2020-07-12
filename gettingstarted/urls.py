from django.urls import path, include

from django.contrib import admin

admin.autodiscover()

import geneal.views

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("", geneal.views.index, name="index"),
    path("db/", geneal.views.db, name="db"),
    path("create/", geneal.views.add_person, name="get_name"),
    path("admin/", admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
]
