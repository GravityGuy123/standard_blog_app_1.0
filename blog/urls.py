from django.urls import path
from django.contrib import admin
from .views import (hello_world, home, post_page, profile, props_page, test2, user_profile, product_list, product_details, post_list, details, test_posts, test_post_details, create_post_method1, create_post_method2, create_post_with_form, comment, edit_comment, create_comment, create_post2, create_post3, create_post4, create_with_save2, create_with_save3, create_with_save4, create_with_save5, create_post_with_form2
)


urlpatterns = [
    # --- Main Pages ---
    path('', home, name='home'),
    path('admin/', admin.site.urls),

    # --- Test / Demo Pages ---
    path('hello/', hello_world, name='hello'),
    path('test/', props_page, name='test'),
    path('test2/', test2, name='test2'),

    # --- Blog / Posts ---
    path('post_list/', post_list, name='post_list'),      # All posts list
    path('post_list/<int:post_id>/', details, name='details'), # Single post details

    path('test_posts/', test_posts, name='test_posts'),
    path('test_posts/<int:post_id>/', test_post_details, name='test_post_details'),

    path('post/', post_page, name='post'),
    path('profile/', profile, name='profile'),

    # --- User Profiles ---
    path('user/<str:username>/', user_profile, name='user_profile'), # Individual user profile

    # --- Products ---
    path('products/', product_list, name='product_list'),
    path('products/<int:product_id>/', product_details, name='product_details'),

    # --- Create Posts ---
    path('create_post_func/', create_post_method1, name='create_post'),
    path('create_post2_func/', create_post_method2, name='create_post2'),

    path('create/', create_post_with_form, name='create_post'),
    path('create2/', create_post_with_form2, name='create_post2'),

    # with .create()
    path('create_post2/', create_post2, name='create_post2'),
    path('create_post3/', create_post3, name='create_post3'),
    path('create_post4/', create_post4, name='create_post4'),
    
    # with .save()
    path('create_with_save2/', create_with_save2, name='create_and_save2'),
    path('create_with_save3/', create_with_save3, name='create_and_save3'),
    path('create_with_save4/', create_with_save4, name='create_with_save4'),
    path('create_with_save5/', create_with_save5, name='create_with_save5'),

    # --- Comments ---
    path('post/<int:post_id>/comments/', comment, name='post_comment'),
    path('comments/<int:comment_id>/edit/', edit_comment, name='edit_comment'),


    path('post/<int:post_id>/create_comment/', create_comment, name='create_comment'),
]