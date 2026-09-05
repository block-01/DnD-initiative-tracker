from random import randint


def select_random_player(players_dict: dict[str, str]) -> str:
    """Selects a random player.

    Args:
        players_dict: A dictionary of players and their characters.

    Returns: The Randomly selected player.
    """
    random_int = randint(0, len(players_dict) - 1)

    return (
        str(players_dict.keys())
        .replace("dict_keys([", "")
        .replace("])", "")
        .replace("'", "")
        .replace(" ", "")
        .split(",")[random_int]
    )


def assign_player_number(players_dict: dict[str, str]) -> dict[str, int]:
    """Assigns a random number to each player.

    Args:
        players_dict: A dictionary of players and their characters.

    Returns:
        A dictionary containing the player name and a randomly assigned number.
    """
    players_number: dict[str, int] = {}

    for player in players_dict:
        assigned: bool = False

        while assigned is False:
            random_int = randint(1, len(players_dict))

            if random_int not in players_number.values():
                players_number[player] = random_int

                assigned = True

    return players_number
