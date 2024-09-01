import flet as ft

def main(page: ft.Page):
    page.title = "Flet Soft Keyboard Example"

    # Create a TextField with autofocus and multiline
    text_field = ft.TextField(
        label="Enter text",
        autofocus=True,
        multiline=True,
    )

    # Handle soft keyboard appearance and disappearance
    def on_keyboard_event(e):
        if e.key == ft.KeyboardEvent.KEY_UP:
            # Soft keyboard disappeared
            print("Soft keyboard disappeared")
        elif e.key == ft.KeyboardEvent.KEY_DOWN:
            # Soft keyboard appeared
            print("Soft keyboard appeared")

    page.on_keyboard_event = on_keyboard_event

    page.add(text_field)

    # Update the page after setting autofocus
    page.update()

ft.app(target=main)
