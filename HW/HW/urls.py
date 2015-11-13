from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'HW.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^AddBook/','blog.views.add_book'),
    url(r'^AddAuthor/','blog.views.add_author'),
    url(r'^AllInformation/','blog.views.all_information'),
    url(r'^DeleteInformation/','blog.views.delete_information'),
    url(r'^Detail/','blog.views.show_detail'),
    #url(r'^Search/','blog.views.all_information'),
    url(r'^admin/', include(admin.site.urls)),
)