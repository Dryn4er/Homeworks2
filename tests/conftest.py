import pytest

from src.product import LawnGrass, Product, Smartphone


@pytest.fixture
def samsung():
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


@pytest.fixture
def smartphone():
    return Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )


@pytest.fixture
def grass():
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")


@pytest.fixture
def new_product():
    return (
        "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.Iphone 15, 210000.0 руб. Остаток: 8 шт.Xiaomi Redmi "
        "Note 11, 31000.0 руб. Остаток: 14 шт."
    )


@pytest.fixture
def mixin_log():
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
