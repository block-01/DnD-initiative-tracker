import json


class CharacterStats:
    def __init__(self, health: int, armour_class: int):
        """Data Structure of Character stats.

        Args:
            health: The maximum health of the player character.
            armour_class: The player characters armour class.
        """
        self.health: int = health
        self.armour_class = armour_class


class CharacterData:
    def __init__(
        self,
        player_name: str,
        character_name: str,
        character_level: int,
        character_class: str,
        character_subclass: str,
        character_stats: CharacterStats,
    ):
        """Data structure with information about the player Character.

        Args:
            player_name: The players name.
            character_name: The name of the character.
            character_level: The characters current level.
            character_class: The characters main class.
            character_subclass: The characters subclass.
            character_stats: The characters stats such as health and armour class.
        """
        self.player_name: str = player_name
        self.character_name: str = character_name
        self.character_level: int = character_level
        self.character_class: str = character_class
        self.character_subclass: str = character_subclass
        self.character_stats: CharacterStats = character_stats


class CharacterFiles:
    def create_character_data(
        self,
        player_name: str,
        character_name: str,
        character_class: str,
        character_subclass: str,
        character_level: int,
        health: int,
        armour_class: int,
    ) -> CharacterData:
        """Populates and returns the CharacterData dataclass with character information.

        Args:
            player_name: The players name.
            character_name: The name of the character.
            character_level: The characters current level.
            character_class: The characters main class.
            character_subclass: The characters subclass.
            health: The maximum health of the player character.
            armour_class: The player characters armour class.

        Returns:
            The CharacterData Dataclass containing the information about the character.
        """
        player_data = CharacterData(
            player_name=player_name,
            character_name=character_name,
            character_class=character_class,
            character_subclass=character_subclass,
            character_level=character_level,
            character_stats=CharacterStats(health=health, armour_class=armour_class),
        )

        return player_data

    def write_player_files(self, player_data: list[CharacterData]) -> None:
        """Writes a list of player data to a JSON file.

        Args:
            player_data: A list of data about the Player Characters.
        """
        json_contents: dict[str, dict[str, str | int | dict[str, int]]] = {}

        for player_item in player_data:
            character_sheet: dict[str, str | int | dict[str, int]] = {
                "character_name": player_item.character_name,
                "character_class": player_item.character_class,
                "character_subclass": player_item.character_subclass,
                "character_level": player_item.character_level,
                "character_stats": {
                    "health": player_item.character_stats.health,
                    "armour_class": player_item.character_stats.armour_class,
                },
            }
            json_contents[player_item.player_name] = character_sheet

        with open("player_data.json", "w") as file:
            file.write(json.dumps(json_contents, indent=4))

    def read_player_files(self, path: str = "player_data.json") -> list[CharacterData]:
        """Reads the contents of the player_data.json file.

        Args:
            path: The path to the JSON file, defaults to `player_data.json`.

        Returns:
            A list of Player Charcter data.
        """
        players_data: list[CharacterData] = []

        with open(path, "r") as json_file:
            json_contents: dict[str, dict[str, str | int | dict[str, int]]] = json.loads(
                json_file.read()
            )

        for item in json_contents:
            player_name = item
            character_name = json_contents[item]["character_name"]
            character_level = json_contents[item]["character_level"]
            character_class = json_contents[item]["character_class"]
            character_subclass = json_contents[item]["character_subclass"]
            health: int = json_contents[item]["character_stats"]["health"]
            armour_class: int = json_contents[item]["character_stats"]["armour_class"]

            player_data: CharacterData = CharacterData(
                player_name,
                character_name,
                character_level,
                character_class,
                character_subclass,
                CharacterStats(health, armour_class),
            )

            players_data.append(player_data)

        return players_data
