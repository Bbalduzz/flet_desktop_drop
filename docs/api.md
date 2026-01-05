# API Reference

## Dropzone

::: src.flet_desktop_drop.flet_desktop_drop.Dropzone

## DroppedFilesEvent

::: src.flet_desktop_drop.flet_desktop_drop.DroppedFilesEvent

## Properties

### content

`Optional[ft.Control]`

The child control to display inside the dropzone. This is typically a `Container` with visual styling to indicate the drop area.

### allowed_file_types

`List[str]`

List of allowed file extensions (without the dot). For example: `["pdf", "jpg", "png"]`.

If empty (default), all file types are accepted.

## Events

### on_dropped

`Callable[[DroppedFilesEvent], Any] | None`

Fired when files are dropped onto the dropzone. The event handler receives a `DroppedFilesEvent` with:

- `files`: List of accepted file paths (matching the `allowed_file_types` filter)
- `rejected_files`: List of rejected file paths (not matching the filter)

### on_entered

`Optional[ft.ControlEventHandler["Dropzone"]]`

Fired when a drag operation enters the dropzone area. Use this to provide visual feedback.

### on_exited

`Optional[ft.ControlEventHandler["Dropzone"]]`

Fired when a drag operation exits the dropzone area. Use this to reset visual feedback.

## Example with Visual Feedback

```python
import flet as ft
from flet_desktop_drop import Dropzone, DroppedFilesEvent


def main(page: ft.Page):
    container = ft.Container(
        content=ft.Text("Drop files here"),
        width=300,
        height=200,
        bgcolor=ft.Colors.BLUE_GREY_100,
        border=ft.border.all(2, ft.Colors.BLUE_GREY_300),
        border_radius=10,
        alignment=ft.alignment.center,
    )

    def on_dropped(e: DroppedFilesEvent):
        container.bgcolor = ft.Colors.BLUE_GREY_100
        container.border = ft.border.all(2, ft.Colors.BLUE_GREY_300)

        if e.files:
            container.content = ft.Text(f"Received {len(e.files)} file(s)")
        page.update()

    def on_entered(e):
        container.bgcolor = ft.Colors.BLUE_100
        container.border = ft.border.all(2, ft.Colors.BLUE_400)
        page.update()

    def on_exited(e):
        container.bgcolor = ft.Colors.BLUE_GREY_100
        container.border = ft.border.all(2, ft.Colors.BLUE_GREY_300)
        page.update()

    dropzone = Dropzone(
        content=container,
        on_dropped=on_dropped,
        on_entered=on_entered,
        on_exited=on_exited,
        allowed_file_types=["pdf"],
    )

    page.add(dropzone)


ft.run(main)
```
