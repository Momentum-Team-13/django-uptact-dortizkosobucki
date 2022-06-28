from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact
from .forms import ContactForm, NoteForm 


# Create your views here.
def list_contacts(request):
    contacts = Contact.objects.all()
    return render(request, "contacts/list_contacts.html",
                  {"contacts": contacts})


def add_contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='list_contacts')

    return render(request, "contacts/add_contact.html", {"form": form})

def add_notes(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'GET':
        new_note = NoteForm()
    else:
        new_note = NoteForm(data=request.POST)
        if new_note.is_valid():
            new_note.contact=contact
            new_note.save()
            return redirect(to='list_contacts')

    return render(request, "contacts/add_notes.html", {"contact": contact, "new_note": new_note})

def edit_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'GET':
        form = ContactForm(instance=contact)
    else:
        form = ContactForm(data=request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect(to='list_contacts')

    return render(request, "contacts/edit_contact.html", {
        "form": form,
        "contact": contact
    })


def delete_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect(to='list_contacts')

    return render(request, "contacts/delete_contact.html",
                  {"contact": contact})

def view_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    return render(request, "contacts/view_contact.html", {"contact":contact})

def view_notes(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        return render(request, "notes/view_note.html")