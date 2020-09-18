from django.contrib import admin
from django.urls import path, include
#firstApp
import first.views
#portfolioApp
import portfolio.views
#사용자가 올린 이미지를 읽어올 수 있음.(동적이미지)
from django.conf import settings
from django.conf.urls.static import static
#accountsApp
import accounts.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', first.views.home, name="home"),
    #blog앱
    path('blog/', include('first.urls')),
    #portfolio앱
    path('portfolio/', portfolio.views.portfolio, name="portfolio"),
    #회원가입 및 로그인
    path('accounts/', include('accounts.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
