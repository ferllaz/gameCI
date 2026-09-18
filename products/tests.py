import pytest

from .models import Game
from .serializers import GameSerializer
from rest_framework.test import APIClient

@pytest.mark.django_db
def test_game_creation():

    game = Game.objects.create(
        name="Minecraft",
        genre="Sandbox",
        price=14999
    )

    assert game.genre == "Sandbox"

@pytest.mark.django_db
def test_game_serializer():

    game = Game.objects.create(
        name="Minecraft",
        genre="Sandbox",
        price=14999
    )

    serializer = GameSerializer(game)

    assert serializer.data["genre"] == "Sandbox"

@pytest.mark.django_db
def test_get_games():

    Game.objects.create(
        name="Minecraft",
        genre="Sandbox",
        price=14999
    )

    client = APIClient()

    response = client.get("/api/games/")

    assert response.status_code == 200

    assert response.data[0]["name"] == "Minecraft"