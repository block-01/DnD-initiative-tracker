#!/usr/bin/env python3
from argparse import ArgumentParser, Namespace

from character_selection import character_selection
from initative_tracker.window import window
from character import character

player_info: dict[str, str] = character.read_player_file()

if __name__ == "__main__":
    dnd_helper_options: ArgumentParser = ArgumentParser(
        prog="DnD helper applicaiton",
        usage="""Select a Random player or assign each player a random number.""",
    )

    dnd_helper_options.add_argument(
        "--random_player", action="store_true", help="Choices a random player."
    )

    dnd_helper_options.add_argument(
        "--assign_random",
        action="store_true",
        help="Assigns each player a random number.",
    )

    dnd_helper_options.add_argument(
        "--initative",
        action="store_true",
        help="Opens up a grphical user interface for initiative tracking.",
    )

    args: Namespace = dnd_helper_options.parse_args()

    if args.random_player:
        print(character_selection.select_random_player(player_info))

    elif args.assign_random:
        player_dict: dict[str, int] = character_selection.assign_player_number(
            player_info
        )

        for name, number in player_dict.items():
            print(f"Player '{name}' has been assigned the number '{number}'")

    elif args.initative:
        window.window_main()

    else:
        character.CharacterFiles.write_player_files(
            character.CharacterFiles,
            [
                character.CharacterFiles.create_character_data(
                    character.CharacterFiles,
                    "Player-01",
                    "test char",
                    "test_class",
                    "test_subclass",
                    0,
                    10,
                    10,
                ),
                character.CharacterFiles.create_character_data(
                    character.CharacterFiles,
                    "Player-02",
                    "test char",
                    "test_class",
                    "test_subclass",
                    0,
                    10,
                    10,
                ),
            ],
        )  # TODO: Debugging Info, will be moved eventually
        character.CharacterFiles.read_player_files(
            character.CharacterFiles
        )  # TODO: Debugging Info, will be moved eventually
        print("Use --help to show available options.")
