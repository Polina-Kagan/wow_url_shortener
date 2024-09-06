from django.shortcuts import redirect, render, get_object_or_404
from .forms import LinkCreationForm
from .models import ShortLink
import random
import string

def generate_short_code():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(6))

def cutter(request):
    if request.method == 'POST':
        form = LinkCreationForm(request.POST)
        if form.is_valid():
            short_link = form.save(commit=False)
            short_link.user = request.user
            if len(short_link.original_url) > 250:
                entered_chars = len(short_link.original_url)
                form.add_error('original_url', f'URL must be no more than 250 characters. You entered {entered_chars} characters.')
            elif ShortLink.objects.filter(short_code=short_link.short_code).exists():
                form.add_error('short_code', 'This short code is already in use. Please choose another.')
            else:
                short_link.save()
                return redirect('cutter')
    else:
        form = LinkCreationForm()

    user_links = ShortLink.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'cutter/cutter.html', {'form': form, 'user_links': user_links})

def redirect_short_link(request, short_code):
    link = get_object_or_404(ShortLink, short_code=short_code)
    return redirect(link.original_url)