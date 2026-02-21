from django.shortcuts import render, redirect, get_object_or_404
from .models import *

def welcome(request):
    return render(request, 'welcome.html')

def home(request):
    verse = DailyVerse.objects.last()
    meetings = Meeting.objects.all().order_by('date')
    return render(request, 'home.html', {
        'verse': verse,
        'meetings': meetings
    })
def about(request):
    return render(request,'about.html')


# View to show all gallery folders
def gallery_folders(request):
    folders = GalleryFolder.objects.all()
    return render(request, 'gallery_folders.html', {'folders': folders})

# View to show images inside a specific folder
def folder_images(request, folder_id):
    folder = get_object_or_404(GalleryFolder, id=folder_id)
    images = folder.images.all()  # uses related_name="images" in GalleryImage model
    return render(request, 'folder_images.html', {'folder': folder, 'images': images})

def sermons(request):
    sermons = Sermon.objects.all()
    return render(request, "live.html", {"sermons": sermons})


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        ContactMessage.objects.create(
            name=name,
            email=email,
            message=message
        )

        return render(request, "contact.html", {"success": True})

    return render(request, "contact.html")

def offerings(request):
    return render(request,"offerings.html")