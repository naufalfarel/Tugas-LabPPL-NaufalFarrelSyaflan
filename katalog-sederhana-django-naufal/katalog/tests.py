from django.test import TestCase
from django.urls import reverse


class KatalogPageTests(TestCase):
    def test_homepage_dapat_diakses(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Temukan produk favorit')

    def test_daftar_produk_dapat_diakses(self):
        response = self.client.get(reverse('produk_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Notebook Orion Slim 14')

    def test_detail_produk_dapat_diakses_berdasarkan_id(self):
        response = self.client.get(reverse('produk_detail', args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Notebook Orion Slim 14')

    def test_kontak_dapat_diakses(self):
        response = self.client.get(reverse('kontak'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'support@naufalstore.id')
