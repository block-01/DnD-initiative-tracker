mod player_system;

use gtk::prelude::*;
use gtk::{Application, ApplicationWindow, Button};
use std::process;
use crate::player_system::*;

fn main() {
    println!("Initalising Window");

    let app = Application::builder().application_id("org.initiative_tracker.TestApplication").build();

    app.connect_activate(|app| {
        let window = ApplicationWindow::builder()
            .application(app)
            .default_width(320)
            .default_height(200)
            .title("Test Application")
            .build();

        let button = Button::with_label("Exit");

        button.connect_clicked(|_| {
            println!("Exiting application");
            process::exit(0x0100); // Exits the application when the button is pressed
        });

        window.add(&button);

        window.show_all();
    });

    let char_conts = new_character(
        "Test player_name".to_string(), 
        "Test Character Name".to_string(),
        1,
        "Barbarian".to_string(),
        "Path of the Experiment".to_string(),
        0,
        0,

    );
    
    let character_read = read_character_struct(char_conts); 
    
    for (_key, _item) in character_read {
        println!("{_key}: {_item}");
    }

    app.run();

}
