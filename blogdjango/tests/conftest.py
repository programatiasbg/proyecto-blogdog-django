from pytest_factoryboy import register
from .factories import PostFactory

register(PostFactory)

"""
La función register se llama con PostFactory como argumento,
lo que registra la fábrica PostFactory con pytest.
"""
