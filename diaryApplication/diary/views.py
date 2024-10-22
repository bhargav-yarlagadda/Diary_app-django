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

def fetch_individual_diary_entry(request, id):
    try:
        # Try to get the diary entry by id
        currentObj = Entry.objects.get(id=id)
        # If found, render the entry's details page
        return render(request, 'diaryEntry.html', {'entry': currentObj})
    except:
        # If entry is not found, render custom not found page
        return render(request, 'notFound.html')
    
def not_found(request,exception):
    return render(request,'notFound.html',{},status=404)