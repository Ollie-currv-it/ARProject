from django.shortcuts import render, redirect
from django.utils import timezone
from .models import UploadedModelFile
from .forms import UploadModelFileForm
from django.contrib.auth.models import User
from uploadModel.models import UploadedModelFile

def home(request):
    return render(request, 'uploadModel/home.html', {'models': UploadedModelFile.objects.all()})




# Create your views here.
def upload_model(request):
    form = UploadModelFileForm()  # Initialize the form
    if request.method == 'POST' and request.FILES.get('model_file'):
        model_file = request.FILES['model_file']
        uploaded_by = request.user if request.user.is_authenticated else None
        uploaded_instance = UploadedModelFile.objects.create(
            model_file=model_file,
            uploaded_by=uploaded_by,
            file_size=model_file.size,
            tags=request.POST.getlist('tags', []), # add tags to describe model #tags = [t.strip() for t in request.POST.get('tags', '').split(',') if t.strip()]  # comma-separated
            model_name=model_file.name,
            description='', # add description of the model
        )
        # Want to place the file somewhere accessible by the mobile devices

        return render(request, 'uploadModel/upload_success.html', {'filename': model_file.name})

    return render(request, 'uploadModel/upload_model.html', {'form': form})


def view_model(request, model_id):
    pass