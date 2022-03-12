from django.test import TestCase
from . import views
# Create your tests here.
class CodificarTest(TestCase):
    def test_Md5_Coded(self):
        codificar = views.Codificar()
        sha256_waited = '02c6e1eaaac3519f60228a651e5f96db3322939406d1f80ab85c2e62e0f2bd19'
        sha256_created = codificar.codificador('contrasenia1234')
        sha256_obtained = sha256_created.hexdigest()
        self.assertEqual(sha256_obtained, sha256_waited)
        #sha256_waited = '02c6e1eaaac3519f60228a651e5f96db3322939406d1f80ab85c2e62e0f2bd19'