from django.shortcuts import render


# Головна сторінка блогу
def home_view(request):
    context = {
        "blog_name": "TechBlog",
        "description": "Найкращі статті про технології та програмування"
    }
    return render(request, "blog/home.html", context)




# Перевірка досвіду користувача (через POST форму)
def check_experience(request):
    experience_years = None
    if request.method == 'POST':
        # Отримуємо число років досвіду з форми, якщо не передано — беремо 0
        experience_years = int(request.POST.get('years', 0))
    return render(request, "blog/experience.html", {"years": experience_years})




# Відображення списку популярних постів
def popular_posts(request):
    posts_data = [
        {"title": "Вивчаємо Python", "views": 1520},
        {"title": "Django для початківців", "views": 980},
        {"title": "JavaScript ES6", "views": 1340},
        {"title": "React Hooks", "views": 760},
        {"title": "Machine Learning", "views": 2100},
    ]
    
    context = {
        "blog_title": "Популярні статті TechBlog",
        "posts": posts_data,
    }
    return render(request, "blog/popular.html", context)





def student_profile(request):
    context = {
        'student_name': 'Марія Іванова',
        'age': 16,
        'grade': 11,
        'subjects': ['Математика', 'Фізика', 'Програмування', 'Англійська'],
        'average_score': 4.8,
        'is_honor_student': True
    }
    return render(request, 'student_profile.html', context)




def about_view(request):
    context = {
        "blog_name": "TechBlog",
        "description": "Найкращі статті про технології та програмування",
        "author": "Ім'я автора",
        "contact_email": "author@example.com"
    }
    return render(request, "blog/about.html", context)
