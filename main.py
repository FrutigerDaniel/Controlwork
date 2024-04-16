import flet as ft

def main(page: ft.Page):
    page.title = "Flet counter example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    txt_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)

    def minus_click(e):
        txt_number.value = str(int(txt_number.value) - 1)
        page.update()

    def plus_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()
    def cancel_click(e):
        txt_number.value = str(int(txt_number.value == 0))
        page.update()

    def save_click(e):
        ft.TextButton(text="Text button"),
        file = open("otus.txt", "w")
        file.write(txt_number.value)
        file.close()



    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.CLEAR, on_click=cancel_click),
                txt_number,
                ft.IconButton(ft.icons.ADD, on_click=plus_click),
                ft.IconButton(ft.icons.BROWSER_UPDATED_OUTLINED, on_click=save_click)

            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

ft.app(main)