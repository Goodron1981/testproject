from django.test import TestCase

    # Create your tests here.
def test():
    a = 10
    b = 0
    try:
        c = a/b
    except:
        print("Erro")
    else:
        print('Ok')