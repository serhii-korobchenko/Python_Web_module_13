from django.shortcuts import render, redirect
from .models  import Tag, Note, NoteToTag


# Create your views here.
def main(request):
    notes = Note.objects.all()
    return render(request, 'finance_app/index.html', {"notes": notes})

def tag(request):
    if request.method == 'POST':
        name = request.POST['name']
        if name:
            tl = Tag(name=name)
            tl.save()
        return redirect(to='/')
    return render(request, 'finance_app/category.html', {})

def note(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        list_tags = request.POST.getlist('tags')
        if name and description:
            tags = Tag.objects.filter(name__in=list_tags)
            note = Note.objects.create(name=name, description=description,)
            for tag in tags.iterator():
                note.tags.add(tag)
        return redirect(to='/')

    tags = Tag.objects.all()
    return render(request, 'finance_app/income.html', {"tags": tags})

def detail(request, note_id):
    note = Note.objects.get(pk=note_id)
    note.tag_list = ', '.join([str(name) for name in note.tags.all()])
    return render(request, 'finance_app/detail_income.html', {"note": note})


def set_done(request, note_id):
    Note.objects.filter(pk=note_id).update(done=True)
    return redirect(to='/')


def delete_note(request, note_id):
    note = Note.objects.get(pk=note_id)
    note.delete()
    return redirect(to='/')
