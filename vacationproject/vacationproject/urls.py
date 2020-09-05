from django.contrib import admin
from django.urls import path
import first.views
import portfolio.views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', first.views.home, name="home"),
    path('blog/<int:blog_id>', first.views.detail, name="detail"),
    path('blog/write', first.views.write, name="write"),#글쓰기 페이지를 띄워주는 함수 실행 path
    path('blog/create', first.views.create, name="create"),#작성한 글을 DB에 저장하는 함수를 실행하는 path
    path('blog/<int:blog_id>/update', first.views.update, name="update"),
    path('blog/<int:blog_id>/delete', first.views.delete, name="delete"),
    
    path('portfolio/', portfolio.views.portfolio, name="portfolio"),
]
