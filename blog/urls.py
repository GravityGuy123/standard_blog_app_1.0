from django.urls import path
from django.contrib import admin
from .views import (
    hello_world,
    home,
    post_page,
    profile,
    props_page,
    test2,
    user_profile,
    product_list,
    product_details,
    post_list,
    details,
    test_posts,
    test_post_details,
    create_post_method1,
    create_post_method2,
    create_post_with_form,
    comment,
    edit_comment,
    create_comment,
    create_post2,
    create_post3,
    create_post4,
    create_with_save2,
    create_with_save3,
    create_with_save4,
    create_with_save5,
    create_post_with_form2,
    register_user,
    profile_view,
    posts_by_author,
    posts_except_admin,
    user_list,
    update_user_email,
    update_username,
    last_7_days_posts,
    advanced_search,
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
    path('user/', profile, name='profile'),


    # --- Posts by Author/User ---
    path('author_posts', posts_by_author, name='author_posts'),
    path('author/<str:author_name>/', posts_by_author, name='author_posts'),

    path('posts_except_admin/', posts_except_admin, name='posts_except_admin'),


    path('week_ago_posts/', last_7_days_posts, name='week_ago_posts'),

    # --- User Profiles ---
    path('user/<str:username>/', user_profile, name='user_profile'), # Individual user profile

    path('users/', user_list, name='users_list'),
    path('users/<int:user_id>/update_email/', update_user_email, name='update_user_email'),
    path('users/<int:user_id>/update_username/', update_username, name='update_username'),


    # --- Products ---
    path('products/', product_list, name='product_list'),
    path('products/<int:product_id>/', product_details, name='product_details'),


    # --- Create Posts ---
    path('create_post_func/', create_post_method1, name='create_post'),
    path('create_post2_func/', create_post_method2, name='create_post2'),

    path('create/', create_post_with_form, name='create_post'),
    path('create2/', create_post_with_form2, name='create_post2'),

    # with .create()
    path('create_post2/', create_post2, name='create_post3'),
    path('create_post3/', create_post3, name='create_post4'),
    path('create_post4/', create_post4, name='create_post5'),
    
    # with .save()
    path('create_with_save2/', create_with_save2, name='create_and_save2'),
    path('create_with_save3/', create_with_save3, name='create_and_save3'),
    path('create_with_save4/', create_with_save4, name='create_with_save4'),
    path('create_with_save5/', create_with_save5, name='create_with_save5'),


    # --- Comments ---
    path('post/<int:post_id>/comments/', comment, name='post_comment'),
    path('comments/<int:comment_id>/edit/', edit_comment, name='edit_comment'),


    path('post/<int:post_id>/create_comment/', create_comment, name='create_comment'),


    # --- Register User ---
    path('register/', register_user, name='register_user'),

    
    # --- User Profile ---
    path('profile/<str:username>/', profile_view, name='profile_view'),
    
    # --- Search ---
    path('search/', advanced_search, name='search_posts')
]