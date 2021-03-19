import unittest

from app import app
from cache_teste import cache

class TestFibonacci(unittest.TestCase):

    def valores_parametros(self, numero):
        tester = app.test_client()
        response = tester.get(f"/{numero}")
        self.assertEqual(response.status_code, 200)
        valor = int(response.data.decode())
        self.assertEqual(cache[numero], valor)

    def test_10(self):
        self.valores_parametros(10)
    
    def test_all(self):
        for i in range(1,301):
            self.valores_parametros(i)
    




if __name__ == "__main__":
    unittest.main()