# tests/test_views.py
from flask_testing import TestCase
from wsgi import app

class TestViews(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_read_many_products(self):
        response = self.client.get("/api/v1/products")
        products = response.json
        self.assertIsInstance(products, list)
        self.assertGreater(len(products), 2) # 2 is not a mistake here.
        
    def test_get_1(self):
        response = self.client.get("/api/v1/products/1")
        product = response.json
        self.assert_200(response, True)
        # self.assertEqual(response.status_code, 200)
        self.assertIsInstance(product, dict)
        self.assertEqual(product['name'], "Skello")
        
    def test_get_wrong(self):
        response = self.client.get("/api/v1/products/5000")
        product = response.json
        self.assert_404(response, True)
    
    def test_get_wrong(self):
        response = self.client.get("/api/v1/products/5000")
        product = response.json
        self.assert_404(response, True)
    
    def del_1(self):
        response = self.client.delete("/api/v1/products/1")
        products = response.json
        self.assert_204(response, True)
        response2 = self.client.get("/api/v1/products/1")
        self.assert_404(response, True)
        