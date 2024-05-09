import factory
import factory.fuzzy
from django.contrib.auth.models import User
from faker import Factory as FakerFactory

from .models import Post

faker = FakerFactory.create()


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    title = factory.LazyFunction(lambda: faker.sentence(nb_words=10))
    subtitle = factory.LazyFunction(lambda: faker.sentence(nb_words=6))
    slug = factory.Faker("slug")
    author = User.objects.get_or_create(username="admin")[0]

    @factory.lazy_attribute
    def content(self):
        # Creating paragraph using Faker.
        x = ""
        for _ in range(0, 5):
            x += faker.paragraph(nb_sentences=20) + "\n"
        return x

    status = factory.fuzzy.FuzzyChoice(
        choices=["draft", "Draft", "published", "Published"]
    )

    """
    Opcion 2 de slug segun el título
        def slug(self):
            return slugify(self.title)
    """

    @factory.post_generation
    def tags(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            self.tags.add(extracted)
        else:
            self.tags.add(
                "Beagle",
                "bulldog-ingles",
                "pastor-aleman",
                "golden-retriever",
                "labrador-retriever",
                "poodle",
                "husky-siberiano",
                "chihuahua",
                "dalmata",
                "boxer",
                "schnauzer",
            )


"""
!LazyFunction
El valor de un atributo no depende del objeto que se está creando.
Toma como argumento una función a llamar; eso no debería tomar ningún argumento y devolver un valor.
También es útil para asignar copias de objetos mutables (como listas) a la propiedad de un objeto. Ejemplo:

DEFAULT_TEAM = ['Player1', 'Player2']
teammates = factory.LazyFunction(lambda: list(DEFAULT_TEAM))

!LAzyAttribute
Toma como argumento un método a llamar (normalmente una lambda); ese método debería aceptar el objeto que se está construyendo como único argumento y devolver un valor.
"""
