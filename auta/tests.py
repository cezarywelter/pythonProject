from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse, resolve

from .models import Auto, ExtraInfo
from .views import wszystkie_auta, szczegoly_auta, nowy_auto, edytuj_auto


class AutaTests(TestCase):


    def setUp(self):
        User.objects.create_superuser(username='admin', password='admin')

# Testowanie urls
    def test_urls_wszystkie_auta(self):
        url = reverse('wszystkie_auta')
        # print(resolve(url))
        self.assertEquals(resolve(url).func,wszystkie_auta)

    def test_urls_szczegoly_auta(self):
        url = reverse('szczegoly_auta',args=[3])
        self.assertEquals(resolve(url).func, szczegoly_auta)

    def test_urls_nowy_auta(self):
        url = reverse('nowy_auto')
        self.assertEquals(resolve(url).func,nowy_auto)

    def test_urls_usun_auta(self):
        url = reverse('auto_usun',args=[3])
        self.assertEquals(resolve(url).func,auto_usun)

    def test_urls_edytuj_auta(self):
        url = reverse('edytuj_auta',args=[3])
        self.assertEquals(resolve(url).func,edytuj_auto)

# Testowanie views
    def test_views_wszystkie_auta(self):
        client = Client()
        response = client.get(reverse('wszystkie_auta'))
        self.assertEquals(response.status_code,200)

    def test_views_wszystkie_auta_templates(self):
        client = Client()
        response = client.get(reverse('wszystkie_auta'))
        self.assertTemplateUsed(response,'auta/wszystkie.html')

    def test_views_szczegoly_auta(self):
        auto = Auto.objects.create(marka="Auto testowe", rok_produkcji=2000)
        client = Client()
        response = client.get(reverse('szczegoly_auta',args=[1]))
        self.assertEquals(response.status_code,200)

    def test_views_szczegoly_auta_templates(self):
        auto = Auto.objects.create(marka="Auto testowe", rok_produkcji=2000)
        client = Client()
        response = client.get(reverse('szczegoly_auta',args=[1]))
        self.assertTemplateUsed(response,'auta/szczegoly.html')

    def test_views_nowy_auto(self):
        client = Client()
        client.login(username="admin", password="admin")
        response = client.get(reverse('nowy_auto'))
        self.assertEquals(response.status_code,200)

    def test_views_nowy_auto_templates(self):
        client = Client()
        client.login(username="admin", password="admin")
        response = client.get(reverse('nowy_auto'))
        self.assertTemplateUsed(response,'auta/auto_form.html')

    def test_views_edytuj_auto(self):
        auto = Auto.objects.create(marka="Auto testowe", rok_produkcji=2000)
        client = Client()
        client.login(username="admin", password="admin")
        response = client.get(reverse('edytuj_auto', args=[1]))
        self.assertEquals(response.status_code, 200)

    def test_views_edytuj_auto_templates(self):
        auto = Auto.objects.create(marka="Auto testowe", rok_produkcji=2000)
        client = Client()
        client.login(username="admin", password="admin")
        response = client.get(reverse('edytuj_auto', args=[1]))
        self.assertTemplateUsed(response, 'auto/auto_form.html')

    def test_views_auto_usun(self):
        auto = Auto.objects.create(marka="Auto testowe", rok_produkcji=2000)
        client = Client()
        client.login(username="admin", password="admin")
        response = client.get(reverse('auto_usun', args=[1]))
        self.assertEquals(response.status_code, 200)

    def test_views_auto_usun_templates(self):
        auto = Auto.objects.create(marka="Auto testowe", rok_produkcji=2000)
        client = Client()
        client.login(username="admin", password="admin")
        response = client.get(reverse('auto_usun', args=[1]))
        self.assertTemplateUsed(response, 'auto/auto_usun.html')

# Testowanie models
    def test_models_auto_jako_text(self):
        auto = Auto.objects.create(marka="Auto testowe", rok_produkcji=2000)
        self.assertEquals(str(auto), auto.marka+' ('+str(auto.rok_produkcji)+')')

    def test_models_nowe_auto_nie_jest_pusty(self):
        auto = Auto.objects.create(marka="Auto testowe", rok_produkcji=2000)
        self.assertNotEquals(auto,None)

    def test_models_auto_jest_unikalny(self):
        auto1 = Auto.objects.create(marka="Auto testowe", rok_produkcji=2000)
        with self.assertRaises(Exception):
            auto2 = Auto.objects.create(marka="Auto testowe", rok_produkcji=2000)

    def test_models_nowy_auto_jest_tylko_1(self):
        Auto.objects.create(marka="Auto testowe", rok_produkcji=2000)
        self.assertEquals(Auto.objects.all().count(),1)

    def test_models_extrainfo_czy_jest_w_choice(self):
        NADWOZIE = [0,1,2,3,4,5,6]
        einfo = ExtraInfo.objects.create(gatunek=0, czas_trwania=90)
        self.assertIn(einfo.gatunek,NADWOZIE)