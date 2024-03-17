from django.shortcuts import render, redirect
from .models import Document
from .forms import DocumentForm


def home(request):
    return render(request, 'documents/base.html')


def documents(request):
    documents = Document.objects.all()
    return render(request, 'documents/documents.html', {'documents': documents})


def create_document(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('documents')
    else:
        form = DocumentForm()

    return render(request, 'documents/create_document.html', {'form': form})


def validate(request, document_id):
    document = Document.objects.get(id=document_id)
    document.is_validated = True
    document.save()
    return redirect('documents')