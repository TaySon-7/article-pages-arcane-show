from django.test import TestCase
from .models import Article
from datetime import datetime
from .views import test
from django.http import HttpRequest
from .views import article_page

# Create your tests here
class Article_page_test(TestCase):
     def test_article_page_displays_correct_article(self):
          Article.objects.create(
             title="title 1",
             full_text="full text 1",
             summary="summary 1",
             category="category 1",
             pubdate=datetime.now()
             
          )
          request = HttpRequest()
          response = article_page(request, 1)
          html = response.content.decode("utf8")

          self.assertIn("title 1", html)
          self.assertNotIn("summary 1",html)
          self.assertIn("full text 1",html)





