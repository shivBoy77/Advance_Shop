from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from Blog.views import index, blog, blog_details, newsletter_unsubscribe
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('blog/', blog),
    path('blog_details/', blog_details),
    path('Un_sub_news/', newsletter_unsubscribe),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
