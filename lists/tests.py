from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from lists.views import home_page

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()  # 1. Cria uma requisição HTTP falsa
        response = home_page(request)  # 2. Passa a requisição para a nossa view
        html = response.content.decode('utf8')  # 3. Pega o conteúdo da resposta
        
        # 4. Verifica se o HTML está correto:
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>', html)
        self.assertTrue(html.endswith('</html>'))