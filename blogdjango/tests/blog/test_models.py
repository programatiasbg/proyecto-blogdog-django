import pytest

pytestmark = pytest.mark.django_db

class TestPostModel:
    def test_str_return(self, post_factory):
        post = post_factory(
            title="test-post"
        )  # overriding title defined in factories.py
        assert post.__str__() == "test-post"

    # verifica que se le asigno 1 tag al post
    def test_add_tag(self, post_factory):
        x = post_factory(title="test-post", tags=["tets-tag-1"])
        # assert x.tags.count() == 2, da erros ya con post_factory solo creamos y asignamos 1 tag
        assert x.tags.count() == 1
