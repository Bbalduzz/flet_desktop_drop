# API Reference

## Dropzone

A control that accepts file drops from the desktop.

```python
from flet_desktop_drop import Dropzone
```

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `content` | `Optional[ft.Control]` | The child control to display inside the dropzone |
| `allowed_file_types` | `List[str]` | List of allowed extensions (e.g., `["pdf", "jpg"]`). Empty = all allowed |

### Events

| Event | Type | Description |
|-------|------|-------------|
| `on_dropped` | `Callable[[DroppedFilesEvent], Any]` | Fired when files are dropped |
| `on_entered` | `ControlEventHandler` | Fired when drag enters the dropzone |
| `on_exited` | `ControlEventHandler` | Fired when drag exits the dropzone |

---

## DroppedFilesEvent

Event fired when files are dropped onto the Dropzone.

```python
from flet_desktop_drop import DroppedFilesEvent
```

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `files` | `List[str]` | List of accepted file paths |
| `rejected_files` | `List[str]` | List of rejected file paths (wrong extension) |

---

## Example

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
        if e.files:
            container.content = ft.Text(f"Received {len(e.files)} file(s)")
        page.update()

    def on_entered(e):
        container.bgcolor = ft.Colors.BLUE_100
        page.update()

    def on_exited(e):
        container.bgcolor = ft.Colors.BLUE_GREY_100
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
