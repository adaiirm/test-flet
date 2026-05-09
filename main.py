import flet as ft

def main(page: ft.Page):
    page.title = "Keyboard focus bug example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # forward declare button click handler
    def button_click(_e):
        switch_content(_e)
    
    def button_click2(_e):
        switch_content1(_e)
    
    # crear referencias a los controles
    text_field = ft.TextField(
        label="1. Probar input",
        on_focus=lambda e: print("en foco textfield"),
        width=400)
        
    content_1 = ft.Column(
            [
                text_field,
                ft.Button(
                    width=200,
                    height=52,
                    on_focus=lambda e: print("en foco button 1"),
                    content=ft.Text("2. Cambiar de contenido"),
                    on_click=button_click
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    
    content_2 = ft.Column(
            [
                ft.Text("3. Now tap anywhere else inside the flet window. "
                        "The touch keyboard will appear after each tap, even"
                        "if you close it and there are no controls that use "
                        "keyboard focus. It does not happen when you click, "
                        "it only happens when you tap. You can stop it by "
                        "focusing on another application and then returning "
                        "to the flet application."),
                ft.Container(
                    content=ft.Text("3. Buttons make the keyboard show, too."),
                    padding=10,
                ),
                ft.GestureDetector(
                    content=ft.Container(
                        content=ft.Text("Volver a la página anterior"),
                        padding=10,
                    ),
                    on_tap=button_click2
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    
    switcher = ft.AnimatedSwitcher(content=content_1, duration=100)
    
    def switch_content1(_e):
        # limpiar contenido para evitar que el teclado se muestre al cambiar de contenido
        
        switcher.content = content_1
        page.update()

    def switch_content(_e):
        text_field.value = ""
        switcher.content = content_2
        page.update()

    page.add(ft.SafeArea(switcher))


ft.app(target=main)