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
    simple_update,
    simple_update2,
    simple_update3,
    edit_post,
    login_view,
    logout_view,
    hard_delete1,
    forgot_password,
    reset_password,
    deactivate_account,
    reactivate_account,
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
    path('user/<str:username>/', user_profile, name='user_profile'),

    path('users/', user_list, name='users_list'),
    path('users/<int:user_id>/update_email/', update_user_email, name='update_user_email'),
    path('users/<int:user_id>/update_username/', update_username, name='update_username'),


    # --- Products ---
    path('products/', product_list, name='product_list'),
    path('products/<int:product_id>/', product_details, name='product_details'),


    # --- Create Posts ---
    path('create_post_func/', create_post_method1, name='create_post'),
    path('create_post2_func/', create_post_method2, name='create_post2'),

    path('create/', create_post_with_form2, name='create_post'),
    path('create2/', create_post_with_form, name='create_post2'),

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
    path('search/', advanced_search, name='search_posts'),


    # --- Update Posts ---
    path('simple_update1/', simple_update, name='simple_update1'),
    path('simple_update2/', simple_update2, name='simple_update2'),
    path('simple_update3/', simple_update3, name='simple_update3'),


    # --- Edit Posts ---
    path('edit_post/', edit_post, name='edit_post'),
    path('edit_post/<int:post_id>/', edit_post, name='edit_post'),

    
    # path('comments/<int:comment_id>/edit/', edit_comment, name='edit_comment'),


    # --- Authentication ---
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),

    
    # --- Forgot & Rest Password ---
    path('forgot_password/', forgot_password, name='forgot_password'),
    path('reset_password<int:user_id>/', reset_password, name='reset_password'),

    
    # --- Delete Post ---
    path('post<int:post_id>/delete', hard_delete1, name='hard_delete1'),

    # --- Deactivate Account ---
    path('deactivate/', deactivate_account, name='deactivate_account'),

    # --- Reactivate Account ---
    path('reactivate/', reactivate_account, name='reactivate_account'),
]