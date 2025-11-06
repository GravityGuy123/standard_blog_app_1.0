from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Post, Comment
from django.contrib.auth.models import User
from .forms import PostForm, PostForm2, CommentForm
from django.core.exceptions import ValidationError

# Create your views here.
def hello_world(response):
    """
    Handles a request and returns Hello World
    """

    return HttpResponse('Hello World')


def home(request):
    """
    Renders the Home Page Template
    """

    context = {
        'title': 'My Awesome Blog',
        'username': 'gravity',
        'post_count': 15
    }
    return render(request, 'pages/home.html', context)
    

def post_page(request):
    """
    Renders the post page
    """

    contexts = {
        'title': {'title': 'Post Page'},

        'posts': [
            {'title': 'First Post', 'author': 'John'},
            {'title': 'Second] Post', 'author': 'Anika'},
            {'title': 'Third Post', 'author': 'Simone'},
        ]
    }
        

    return render(request, 'pages/post.html', contexts)


def profile(request):
    """
    Renders the Profile Page
    """

    contexts = {
        'infos': [
            {'name': 'GravityGuy',
             'age': 25,
             'hobbies': ['Reading', 'Coding', 'Swimming', 'Gaming', 'Surfing', 'Figure Scating', 'Hiking'],
             'favorite_quote': "Code is Poetry."}
        ]
    }

    return render(request, 'pages/profile.html', contexts)



def props_page(request):
    """
    Displaying the Props
    """

    contexts = {
        'title': 'Props Page',
        'name': 'Sonic',
        'town': 'Nnewi',
        'state': 'Anambra State',
        'age': 23
    }
    return render(request, 'pages/test.html', contexts,)



def test2(request):
    contexts = {
        'title': {'page_title': '2nd Test Page'},
        'books': [
            {'title': 'Avatar', 'author': 'Yangcheng'},
            {'title': 'Married to the devils son', 'author': 'Odibeze'},
            {'title': 'Take me Home', 'author': 'Maximus'},
            {'title': 'Last Bite', 'author': 'Tiffany Bush'},
        ]
    }

    return render(request, 'pages/test2.html', contexts)


def user_profile(request, username):
    """
    Username parameter comes from the URL 
    """

    context = {
        'username': username
    }
    return render(request, 'pages/user_profile.html',context)


def post_detail(request, post_id):
    """
    post_id parameter comes from the URL
    """

    context = {
        'post_id': post_id
    }
    return render(request, 'pages/post_details.html', context)
    # return render(request, 'pages/post_details.html', {'context': context})


def product_list(request):
    """
    Render a list of Products
    """

    products = [
        {'id': 1, 'name': 'Laptop', 'price': 999},
        {'id': 2, 'name': 'Mouse', 'price': 25},
        {'id': 3, 'name': 'Keyboard', 'price': 75},
    ]

    context = {'products': products}
    return render(request, 'pages/product_list.html', context)


def product_details(request, product_id):
    """
    Render a list of Products
    """

    products = {
        1: {'name': 'Laptop', 'price': 999, 'description': 'Powerful Laptop for work and play'},
        2: {'name': 'Mouse', 'price': 25, 'description': 'Ergonomic Wireless Mouse'},
        3: {'name': 'Keyboard', 'price': 75, 'description': 'Mechanical keyboard with RGB Lights'},
    }

    product = products.get(product_id)
    context = {'product': product, 'product_id': product_id}
    return render(request, 'pages/product_details.html', context)


def post_list(request):
    """
    Displays all blog posts
    """

    posts = Post.objects.all() # Get all posts from database
    context = {'posts': posts}
    return render(request, 'pages/post_list.html', context)


def details(request, post_id):
    """
    Display a single post
    """

    # Get the post or return 404
    post = get_object_or_404(Post, id=post_id)

    # Fetch comments related to this post
    # It is imparative that the related name of the post variable within the Comment class in the models.py file to be exactly the same(in this case it is comments).
    comments = post.comments.all().order_by('-created_at')
    
    # Handle comment form submission
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('details', post_id=post.id)
    else:
        form = CommentForm()

    context = {
        'post': post,
        'comments': comments,
        'form': form
    }
    return render(request, 'pages/details.html', context)


def test_posts(request):
    """
    Display all test posts
    """

    posts = Post.objects.all()
    context = {'posts': posts}

    return render(request, 'pages/test_posts.html', context)


def test_post_details(request, post_id):
    """
    Displays a specific test post
    """

    post = get_object_or_404(Post, id=post_id)
    context = {'post': post}
    return render(request, 'pages/test_posts_details.html', context)
    

def create_post_check_method1(request):
    """
    Checks if a post exists and then creates if it doesn't
    """
    user = User.objects.first()

    # check if post already exists
    post, created = Post.objects.get_or_create(
        title='My First Post',
        defaults={
            'content': 'This is the content of my first post',
            'author': user
        }
    )

    if created:
        message = f"New post created with ID: {post.id}"
    else:
        message = f"Post already exists with ID: {post.id}"

    return HttpResponse(message)


# 1. Using .create()
# a.
def create_post_method1 (request):
    """
    Get the first logged in user and create a post the user
    """

    # Get the first user
    user = User.objects.first()

    # Create a post in one line
    post = Post.objects.create(
        title = 'My First Post',
        content = 'This is the content of my first post',
        author = user
    )

    return HttpResponse(f"Post created with ID: {post.id}")


# b.
def create_post2(request):
    """
    Create post with default values with .create()
    """
    user = User.objects.first()
    post = Post.objects.create(
        title = 'Quick Post',
        content = 'Short Content',
        author = user
    )


    return HttpResponse(f'Post - ({post.title}) created successfully')
    # visit http://127.0.0.1:8000/create_post2/ to create
    # NB: If the HttpResponse is not returned, the post still get's created but just doesn't show


# c.
def create_post3(request):
    """
    Create post with computed values with .create()
    """

    title = 'Quick Title for Post 3'
    user = User.objects.last()

    post = Post.objects.create(
        title = title,
        content = 'Learn Django step by step',
        author = user
    )

    return HttpResponse(f'Post - ({post.title}) created successfully for ({post.author})')


# d.
def create_post4(request):
    """
    Create multiple posts in a loop with .create()
    """

    user = User.objects.last()
    created_posts = []

    for create in range(1, 6):
        post = Post.objects.create(
            title = f'Sample loop post {create}',
            content = f'This is the content for sample loop post {create}.',
            author = user
        )

        created_posts.append(post)

    return HttpResponse(f'Created {len(created_posts)} posts with a loop.')
    

# 2. Using .save()
# a.
def create_post_method2(request):
    user = User.objects.first()

    # Step 1: Create the object (not saved yet)
    post = Post (
        title = 'My Second Post',
        content = 'This is the content of my second post',
        author = user
    )

    # Step 2: You can modify it before saving
    post.published = True

    # Step 3: Save to Datebase
    post.save()

    return HttpResponse(f"Post created with ID: {post.id}")


# b.
def create_with_save2(request):
    """
    Create and modify a post before saving with .save()
    """

   # Try to get user with username 'gravityguy'
    try:
        user = User.objects.get(username__iexact='gravityguy')
    except User.DoesNotExist:
        # If not found, fall back to last registered user
        user = User.objects.last()

    post = Post(
        title = 'Draft Post',
        content = 'This starts as a draft.',
        author = user
        )
    
    post.title = 'Draft Title Changed'
    post.save()

    return HttpResponse(f'Post created with Title - ({post.title})')

# c.
def create_with_save3(request):
    """
    Create and run a conditional logic before saving with .save()
    """

    user = User.objects.last()
    post = Post(
        title = 'Second Draft Post by .save().',
        content = 'This is the content of the second draft post by .save().',
        author = user
    )

    if 'urgent' in post.title.lower():
        post.content = f'{post.content} This is an urgent post'
    
    # Now save
    post.save()

    return HttpResponse(f'Post created: {post.title}')

# d.
def create_with_save4(request):
    """
    Create a post and handle errors before saving with .save()
    """

    # Try to get user with username 'admin'
    try:
        user = User.objects.get(username__iexact='Admin')
    except User.DoesNotExist:
        user = User.objects.last()
    
    try:
        post = Post(
            title = 'Third Draft Post by .save().',
            content = 'This is the content of the third draft post by .save().',
            author = user
        )

        # validate before saving
        post.full_clean() # This checks all model validators
        post.save()

        return HttpResponse(f'post created successfully - ({post.title})')
    except ValidationError as e:
        return HttpResponse(f'Validation Error {e}')

# user = User.objects.get(username__icontain='Admin')
# user = User.objects.get(username__iexact='Admin')
# Using icontain checks whether there's a username that contains 'Admin'. The 'i' before contain makes it case insensitive such that it gets the username, whether or not a letter within the it has a different case. icontain is necessary there might be other letters or characters before, within or after, as longs as there 'a d m i n' in whatever order. iexact on the other hand will only be true if the username is exactly what you are checking. No letter or character(s), before, within, or after. The 'i' before exact makes the check case insensitive


# e.
def create_with_save5(request):
    """
    Create, save and update a post's field before saving with .save()
    """

    try:
        user = User.objects.get(username__iexact='GravityGuy')
    except User.DoesNotExist:
        user = User.objects.last()

    post = Post(
        title = 'Title for draft post 5',
        content = 'This is the content',
        author = user
    )
    post.save()

    # later, update only specific fields
    post.content = 'This is the updated content for draft post 5'
    post.save(update_fields=['content']) # Only updates content

    return HttpResponse(f'Post with title ({post.title}) successfully created.')


# 3a. Using Django Forms
def create_post_with_form(request):
    """
    Create a post using Django forms
    """

    # Check if form was submitted (POST request)
    if request.method == 'POST':
        # Create form with submitted data
        form = PostForm(request.POST)

        # Check if data is valid
        if form.is_valid():

            # Save but don't commit to database yet
            post = form.save(commit=False)

            # Set the author to logged-in user
            post.author = request.user

            # Now Save to database
            post.save()

            return redirect('post_list') # Redirect to Post Page
        
    else:
        # if GET request show empty form
        form = PostForm()

    return render(request, 'pages/create_post.html', {'form': form})


# 3b.
def create_post_with_form2(request):
    """
    This form automatically creates form fields based on the Post model and handle both GET (show form) and POST (process form) requests.
    """

    if request.method == 'POST':
        # User submitted the form
        form = PostForm2(request.POST)

        if form.is_valid():
            # Form data is valid, save but don't commit to database yet
            post = form.save(commit=False)

            # Set the author to logged-in User
            post.author = request.user

            # Now save to database
            post.save()

            # Redirect to success page
            return redirect('details', post_id = post.id)
        
        # It will show errors if form is invalid
    
    else:
        # Get request: show empty form
        form = PostForm2()

    # Render the template with the form
    return render(request, 'pages/create_post2.html', {'form': form})


def comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = post.comments.all() # Fetch all comments

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post_comments', post_id=post_id)
    else:
        form = CommentForm()

    context = {'post': post, 'comments': comments, 'form': form}
    return render(request, 'pages/post_comment.html', context)


def create_comment(request, post_id):
    """
    Create a Comment object linked to a Post and a User using the .create() method
    """
    
    # Get the target post
    post = get_object_or_404(Post, id=post_id)

    # For practice, pick any user (in real use, you'd use request.user)
    user = User.objects.last()

    # Create the comment
    comment = Comment.objects.create(
        post = post,
        author = user,
        text = 'This is an Awesome post',
    )
    # print(comment.id)
    return HttpResponse(f"Comment created by {user.username} for post: {post.title} ")

# The comment get's created for post 1 once you log into the address below
# http://127.0.0.1:8000/post/1/create_comment/



def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    # Optional: ensure only the author can edit
    if comment.author != request.user:
        return HttpResponse("You are not allowed to edit this comment", status=403)

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)  # bind form to existing comment
        if form.is_valid():
            form.save()  # updates the comment and updates `updated_at`
            return redirect('details', post_id=comment.post.id)
    else:
        form = CommentForm(instance=comment)  # pre-fill form with existing comment

    return render(request, 'pages/edit_comment.html', {
        'form': form,
        'comment': comment, # Template now accesses comment.post.id
        })


