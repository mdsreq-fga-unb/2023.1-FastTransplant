from .models import Donator, Receiver, Log

def new_log(page, description, user):
    Log.objects.create(
        page=page,
        description=description,
        user=user
    ).save()

def read_donator_pdf():
    pass

def check_compatibility(donators, receivers):
    if donators == "all":
        dons = Donator.objects.all()
        rec = Receiver.objects.get(id=receivers)
        return [{"donator": don, "receiver": rec, "compat": don.abo == rec.abo} for don in dons]
    elif receivers == "all":
        don = Donator.objects.get(id=donators)
        recs = Receiver.objects.all()
        return [{"donator": don, "receiver": rec, "compat": don.abo == rec.abo} for rec in recs]
    else:
        don = Donator.objects.get(id=donators)
        rec = Receiver.objects.get(id=receivers)
        return [{"donator": don, "receiver": rec, "compat": don.abo == rec.abo}]