use std::collections::HashMap;

pub struct CharacterData {
    player_name: String,
    character_name: String,
    character_level: u8,
    character_class: String,
    characrter_subclass: String,
    character_health: u8,
    character_armour_class: u8,
}


pub fn new_character(
    player_name: String,
    character_name: String,
    character_level: u8,
    character_class: String,
    characrter_subclass: String,
    character_health: u8,
    character_armour_class: u8,
    ) -> CharacterData{

        CharacterData {
            player_name: player_name.to_string(),
            character_name: character_name.to_string(),
            character_level: character_level,
            character_class: character_class.to_string(),
            characrter_subclass: characrter_subclass.to_string(),
            character_health: character_health,
            character_armour_class: character_armour_class
        }

        // return character;

}

pub fn read_character_struct(character_data: CharacterData) -> HashMap<&'static str, String>{
    let mut character_data_conts = HashMap::new();
    character_data_conts.insert("player_name", character_data.player_name);
    character_data_conts.insert("character_name", character_data.character_name);
    character_data_conts.insert("character_level", character_data.character_level.to_string());
    character_data_conts.insert("character_class", character_data.character_class);
    character_data_conts.insert("characrter_subclass", character_data.characrter_subclass);
    character_data_conts.insert("character_health", character_data.character_health.to_string());
    character_data_conts.insert("character_armour_class", character_data.character_armour_class.to_string());

    return  character_data_conts;    

}
