from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect
from books.forms import ContactForm
from books.models import Book


def search(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET.get('q')
        if not q:
            errors.append('Enter a search term.')
        elif len(q) > 20:
            errors.append('Please enter at most 20 characters.')
        else:
            books = Book.objects.filter(title__icontains=q)
            return render(request, 'search_results.html', {'books': books, 'query': q})
    return render(request, 'search_form.html', {'errors': errors})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd['email'],
                ['luis.nickelback@gmail.com']
            )
            return HttpResponseRedirect('/contatc/thanks')
    else:
        form = ContactForm(initial={'subject': 'I love your site!'})
    return render(request, 'contact_form.html', {'form': form})

        # CAP 7 - Exemplo 1
        # if not request.POST.get('subject'):
        #     errors.append('Enter a subject')
        # if not request.POST.get('message'):
        #     errors.append('Enter a message')
        # if request.POST.get('email') and '@' not in request.POST['email']:
        #     errors.append('Enter a valid e-mail address.')
        #
        # if not errors:
        #     send_mail(
        #         request.POST['subject'],
        #         request.POST['message'],
        #         request.POST.get('email') or 'noreply@example.com',
        #         ['luis.nickelback@gmail.com']
        #     )
        #     return HttpResponseRedirect('/contact/thanks')
        # return render(request, 'contact_form.html', {
        #     'errors': errors,
        #     'subject': request.POST.get('subject') or '',
        #     'message': request.POST.get('message') or '',
        #     'email': request.POST.get('email') or ''
        # })