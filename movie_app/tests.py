from django.test import TestCase

class TestMovie(TestCase):

    def test_index(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Фильмы', response.content.decode())
        self.assertIn('Режиссеры', response.content.decode())
        self.assertIn('Актеры', response.content.decode())

    def test_movies(self):
        response = self.client.get('/movies/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Список всех фильмов', response.content.decode())

    def test_directors(self):
        response = self.client.get('/directors/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Список всех режиссеров', response.content.decode())

    def test_acters(self):
        response = self.client.get('/acters/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Список всех актеров', response.content.decode())