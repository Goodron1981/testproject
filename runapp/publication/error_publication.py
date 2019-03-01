from runapp.models import Isue
from runapp.publication.public_content import publikcontent

def public_error():
    isue_list = Isue.objects.filter(public_url="errorpublic")
    for isue in isue_list:
        content = isue.public_content
        num_isue = isue.num
        print('Nunmber isue :', num_isue)
        publikresult = publikcontent(content, num_isue)
        isue.public_url = publikresult
        if publikresult == 'errorpublic':
            isue.error_massage = "Ошибка при публикации"
        print(publikresult)
        isue.save()