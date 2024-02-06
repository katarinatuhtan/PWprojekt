from django.test import SimpleTestCase
from django.urls import reverse, resolve
from . import views


class TestUrls(SimpleTestCase):

    def test_landing_url_is_resolved(self):
        url = reverse('main:landing')
        self.assertEquals(resolve(url).func.view_class, views.LandingPageView)

    def test_join_url_is_resolved(self):
        url = reverse('main:join')
        self.assertEquals(resolve(url).func.view_class, views.VolonterCreateView)

    def test_about_url_is_resolved(self):
        url = reverse('main:about')
        self.assertEquals(resolve(url).func.view_class, views.AboutPageView)

    def test_volonter_url_is_resolved(self):
        url = reverse('main:volonter')
        self.assertEquals(resolve(url).func.view_class, views.VolonterListView)

    def test_projects_url_is_resolved(self):
        url = reverse('main:projects')
        self.assertEquals(resolve(url).func.view_class, views.ProjektiListView)

    def test_crud_url_is_resolved(self):
        url = reverse('main:crud')
        self.assertEquals(resolve(url).func.view_class, views.CrudPageView)

    def test_updatevolonter_url_is_resolved(self):
        url = reverse('main:updatevolonter', args=[1])  # 1 kao primjer PK-a
        self.assertEquals(resolve(url).func.view_class, views.VolonterUpdateView)

    def test_deletevolonter_url_is_resolved(self):
        url = reverse('main:deletevolonter', args=[1])  # 1 kao primjer PK-a
        self.assertEquals(resolve(url).func.view_class, views.VolonterDeleteView)

    def test_addprojekt_url_is_resolved(self):
        url = reverse('main:addprojekt')
        self.assertEquals(resolve(url).func.view_class, views.ProjektCreateView)

    def test_projektlist_url_is_resolved(self):
        url = reverse('main:projektlist')
        self.assertEquals(resolve(url).func.view_class, views.ProjektListView)

    def test_updateprojekt_url_is_resolved(self):
        url = reverse('main:updateprojekt', args=[1])  # 1 kao primjer PK-a
        self.assertEquals(resolve(url).func.view_class, views.ProjektUpdateView)

    def test_register_url_is_resolved(self):
        url = reverse('main:register')
        self.assertEquals(resolve(url).func, views.register)