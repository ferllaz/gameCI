import pytest

from .models import Product
from products.serializers import ProductSerializer

@pytest.mark.django_db
def test_product_creation():

    product = Product.objects.create(
        name="Phone",
        price=50000
    )

    assert product.name == "Phone"

@pytest.mark.django_db
def test_product_serializer():

    product = Product.objects.create(
        name="Phone",
        price=50000
    )

    serializer = ProductSerializer(product)

    assert serializer.data["name"] == "Phone"