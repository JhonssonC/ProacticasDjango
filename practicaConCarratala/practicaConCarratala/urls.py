from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'practicaConCarratala.views.home', name='home'),
    #url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),

)

urlpatterns = patterns('blog.views',
    (r"^entrada/(?P<pk>\d+)/$", "entrada"),
    (r"^months/(\d+)/(\d+)/$", "month"),
    (r"^poncomentario/(\d+)/$", "poncomentario"),
    (r'^admin/', include(admin.site.urls)),
    (r"", "main"),
)