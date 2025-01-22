#document.querySelectorAll(".Button-Buy").forEach(button => {
#    button.addEventListener("click", () => {
#        console.log('Button clicked!');
#    });
#});

#/* querySelectorAll = vybere všechny classy Button-Buy 
#    forEach = pro každý button dej addEventListener "click" 
#    addEventListener = poslouchej když někdo klikne třeba
#    console.log = vypíše něco do console
#*/

buttons = ["Button-Buy1", "Button-Buy2", "Button-Buy3"]  # Představuje tři tlačítka

def on_button_click(button):#funkce pro kliknuti 
    print(f'Button {button} clicked!')#text po kliknuti

for button in buttons: #cyklus for
    print(f'Listening to {button}')
    on_button_click(button) 
