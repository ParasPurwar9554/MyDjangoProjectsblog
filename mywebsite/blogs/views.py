from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,Http404
from django.urls import reverse
from django.template.loader import render_to_string
from datetime import date

# Create your views here.

blog_details = [
    {
        "slug": "python_intro",
        "image": "python.png",
        "date": date(2025, 12, 7),
        "title": "Python Introduction",
        "preview": """Python is a high level language,
        This is open source that is used widely in software development and data science""",
        "content": """Django is a high-level Python web framework
         that encourages rapid development and clean, pragmatic design.
         Built by experienced developers, it takes care of much of the hassle of web development"""
    },
    {
        "slug": "django_basics",
        "image": "django.png",
        "date": date(2025, 11, 28),
        "title": "Getting Started with Django",
        "preview": "Learn the fundamental concepts of the Django framework, including MVC architecture and project setup.",
        "content": "Django follows the Model-View-Controller (MVC) architectural pattern, often referred to as MVT (Model-View-Template) in Django's documentation. This separation allows for cleaner, more maintainable code."
    },
    {
        "slug": "data_science_libraries",
        "image": "python.png",
        "date": date(2025, 11, 15),
        "title": "Top Python Libraries for Data Science",
        "preview": "A look at essential libraries like Pandas, NumPy, and Matplotlib that power data analysis in Python.",
        "content": "Pandas is crucial for data manipulation and analysis, offering data structures like DataFrames. NumPy provides support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays."
    },
    {
        "slug": "web_scraping_python",
        "image": "django.png",
        "date": date(2025, 10, 30),
        "title": "Web Scraping with Beautiful Soup",
        "preview": "An introductory guide to extracting data from websites using Python and the Beautiful Soup library.",
        "content": "Beautiful Soup is a Python library for pulling data out of HTML and XML files. It works with your favorite parser to provide idiomatic ways of navigating, searching, and modifying the parse tree."
    },
    {
        "slug": "python_vs_java",
        "image": "python.png",
        "date": date(2025, 10, 15),
        "title": "Python vs. Java: Which to Learn?",
        "preview": "A comparison between Python and Java, highlighting their strengths, weaknesses, and typical use cases.",
        "content": "Python is generally favored for data science and rapid prototyping due to its simpler syntax and extensive library support. Java, on the other hand, is a strong choice for large-scale enterprise applications and mobile development."
    }
]

# You can now print the updated list to verify
# print(blog_details)

def home_page(request):
    sorted_blogs = sorted(blog_details, key=lambda post:post['date'],reverse=True)
    latest_blogs = sorted_blogs[:2]
    return render(request,"blogs/index.html",{"blogs":latest_blogs})

def blogposts(request):
    return render(request,"blogs/allposts.html",{"blogs":blog_details})

def process_blog_name(blog):
    bloglist = blog.split("_")
    return " ".join(bloglist)

def blog_post(request,blog):
    try:
        res = blog_details[blog]
        return render(request,"blogs/posts.html",{"blog_text":res,"blog_name":process_blog_name(blog)})
    except Exception:
        resData = render_to_string("404.html")
        return HttpResponseNotFound(resData)     
