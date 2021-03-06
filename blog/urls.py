from django.urls import path

from . import  views
app_name = "blog"
urlpatterns = [
    path('', views.index, name="home"),
    path('signup/', views.signup, name="signup"),
    path('login/', views.loginView, name="login"),
    path('logout/', views.LogoutView, name="logout"),
    path('profile/<str:pk>/',views.dashboard,name="profile"),
    path('add_post/',views.Addpost,name="add_post"),
    path('edit_post/<pk>/',views.updatePost,name="edit_post"),
    path('delete_post/<pk>/',views.deletePost,name="delete_post"),
    path('postdetail/<int:pk>/',views.detailPost,name='postdetail'),
    path('categorypost/<str:pk>/lists/',views.category_post_list,name="category_posts"),
    path('likepost/<int:pk>/',views.likeview,name="like_post"),
    path('changeprofilepic/',views.changeProfilePic,name="changepropic"),
    path('changecoverpic/',views.changeCoverPic,name="changecoverpic"),

    # path('add_post/<str:pk>/',views.Addpost,name="add_post"),
]