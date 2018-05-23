from runapp.models import Isue
from runapp.publication.public_content import publilconent

def public_for_num(num_isue):
    isue = Isue.objects.get(num=num_isue)
    content = isue.public_content
    publikresult = publilconent(content, num_isue)
    isue.public_url = publikresult
    print(publikresult)
    isue.save()

