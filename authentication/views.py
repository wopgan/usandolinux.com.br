from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from authentication.models import Person

def create_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        github_link = request.POST.get('github_link', '').strip() or None
        linkedin_link = request.POST.get('linkedin_link', '').strip() or None
        instagram_link = request.POST.get('instagram_link', '').strip() or None


        if Person.objects.filter(username=username).exists():
            #return render(request, 'authentication/create_user.html', {'error': 'Usuário já existe'})
            print('Usuário já existe')
        if Person.objects.filter(email=email).exists():
            #return render(request, 'authentication/create_user.html', {'error': 'E-mail já existe'})
            print('E-mail já existe')

        user = Person.objects.create_user(
            username=username, 
            email=email, 
            password=password, 
            name=name, 
            surname=surname, 
            github_link=github_link, 
            linkedin_link=linkedin_link, 
            instagram_link=instagram_link
            )
        
        return redirect('login')
    

    return render(request, 'authentication/create_user.html')


def update_user(request, user_id):
    user = get_object_or_404(Person, id=user_id)

    if request.method == 'POST':
        user.username = request.POST.get('username', user.username)
        user.email = request.POST.get('email', user.email)
        user.name = request.POST.get('name', user.name)
        user.surname = request.POST.get('surname', user.surname)
        user.github_link = request.POST.get(
            'github_link', '').strip() or user.github_link
        user.linkedin_link = request.POST.get(
            'linkedin_link', '').strip() or user.linkedin_link
        user.instagram_link = request.POST.get(
            'instagram_link', '').strip() or user.instagram_link

        if Person.objects.exclude(id=user_id).filter(username=user.username).exists():
            #return render(request, 'authentication/update_user.html', {'user': user, 'error': 'Username já em uso'})
            print('Username já em uso')

        if Person.objects.exclude(id=user_id).filter(email=user.email).exists():
            #return render(request, 'authentication/update_user.html', {'user': user, 'error': 'E-mail já cadastrado'})
            print('E-mail já cadastrado')

        user.save()
        return redirect('/')

    return render(request, 'authentication/update_user.html', {'user': user})
