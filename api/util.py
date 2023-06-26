from .models import Log

def new_log(page, description, user):
    Log.objects.create(
        page=page,
        description=description,
        user=user
    ).save()

def read_donator_pdf():
    pass
