import factory
from blog.models import Post
from django.contrib.auth.models import User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
        skip_postgeneration_save = True

    password = "test"
    username = "test"
    is_superuser = True
    is_staff = True


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    title = "algo"
    subtitle = "algo"
    slug = "algo"
    content = "algo"
    status = "published"  # o "draft"
    author = factory.SubFactory(UserFactory)

    # no es obligatorio, pero sirve para guardar la intacia
    @classmethod
    def _after_postgeneration(cls, instance, create, extracted=None, **kwargs):
        instance.save()

    @factory.post_generation
    def tags(self, create, extracted,**kwargs):
        if not create:
            return

        if extracted:
            #pasar los tags ya creados y se almacenan
            self.tags.add(*extracted)
