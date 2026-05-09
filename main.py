import flet as ft

def main(page: ft.Page):
    page.title = "Keyboard focus bug example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # forward declare button click handler
    def button_click(_e):
        switch_content(_e)
    
    def button_click2(_e):
        switch_content1(_e)
        
    invisible_button = ft.Button(
        content=ft.Text("Invisible button"),
        height=0,
        width=0,
        autofocus=True
    )

    content_1 = ft.Column(
            [
                ft.TextField(
                    label="1. Probar input",
                    width=400),
                ft.Container(
                    ink=True,
                    width=200,
                    height=52,
                    border_radius=30,
                    alignment=ft.Alignment(0, 0),
                    border=ft.Border.all(1, ft.Colors.BLACK),
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
                ft.OutlinedButton("3. Buttons make the keyboard show, too."),
                ft.OutlinedButton("Volver a la página anterior", on_click=button_click2),
                invisible_button
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    
    switcher = ft.AnimatedSwitcher(content=content_1, duration=100)
    
    def switch_content1(_e):

        switcher.content = content_1
        page.update()

    def switch_content(_e):
        
        switcher.content = content_2
        page.update()

    page.add(ft.SafeArea(switcher))


ft.app(target=main)