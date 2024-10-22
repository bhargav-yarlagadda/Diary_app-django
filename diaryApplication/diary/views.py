from django.shortcuts import render,redirect
from .models import Entry
# Create your views here.
def home_page(request):
    return render(request,'Home.html')

def add_new_entry(request):
    if request.method == 'POST':
        heading = request.POST.get('heading')
        entry = request.POST.get('entry')
        print(heading,entry)
        NewEntry = Entry.objects.create(header=heading, entry=entry)
        return redirect('/view-entries')
    return render(request,'Entry.html')
def fetch_entries(request):
    entries = Entry.objects.all().order_by('-timestamp')  # Get all entries sorted by timestamp in descending order
    return render(request, 'viewDiaryEntries.html', {'entries': entries})
