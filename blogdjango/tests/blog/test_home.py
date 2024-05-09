import pytest
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed

pytestmark = pytest.mark.django_db


# verificar que homegae exista y en el cliente de status 200
class TestHomePage:
    def test_homepage_url(self, client):
        url = reverse("homepage")
        resp = client.get(url)
        assert resp.status_code == 200

    # Verificar que a activarse el htmx, de una header de HTTP_HX-request y el template llamado sea
    def test_post_htmx_frament(self, client):
        headers = {"HTTP_HX-request": "true"}
        resp = client.get("/", **headers)
        assertTemplateUsed(resp, "blog/components/post-list-elements.html")


# asegurarnos que se vea la página de inicio al cargar el servidor
