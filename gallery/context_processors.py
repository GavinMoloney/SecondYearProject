from .models import Votes

def all_votes(request):
    votes = Votes.objects.all()
    return {'all_votes': votes}
