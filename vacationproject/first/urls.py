from django.contrib import admin
from django.urls import path
import first.views #from . import views 와 같음.

urlpatterns =[
    
    path('<int:blog_id>', first.views.detail, name="detail"),
    path('write', first.views.write, name="write"),#글쓰기 페이지를 띄워주는 함수 실행 path
    path('create', first.views.create, name="create"),#작성한 글을 DB에 저장하는 함수를 실행하는 path
    path('<int:blog_id>/update', first.views.update, name="update"),
    path('<int:blog_id>/delete', first.views.delete, name="delete"),
]