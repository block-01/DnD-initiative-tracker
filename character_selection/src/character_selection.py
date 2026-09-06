from random import randint
from character import character


def select_random_player(character_list: list[character.CharacterData]) -> str:
    """Selects a random player.

    Args:
        character_list: A list of players and their characters.

    Returns: The Randomly selected player.
    """
    random_int = randint(0, len(character_list) - 1)

    return character_list[random_int].player_name


def assign_player_number(
    character_list: list[character.CharacterData],
) -> dict[str, int]:
    """Assigns a random number to each player.

    Args:
        character_list: A list of players and their characters.

    Returns:
        A dictionary containing the player name and a randomly assigned number.
    """
    players_number: dict[str, int] = {}

    for player in character_list:
        assigned: bool = False

        while assigned is False:
            random_int = randint(1, len(character_list))

            if random_int not in players_number.values():
                players_number[player.player_name] = random_int

                assigned = True

    return players_number
