from runapp.models import Isue
from runapp.publication.public_content import publikcontent

def public_for_num(num_isue):
    isue = Isue.objects.get(num=num_isue)
    content = isue.public_content
    publikresult = publikcontent(content, num_isue)
    isue.public_url = publikresult
    print(publikresult)
    isue.save()

