# flet-desktop-drop

A Flet control for drag and drop file support on desktop platforms.

This control wraps the Flutter [desktop_drop](https://pub.dev/packages/desktop_drop) package and allows users to drag and drop files onto a designated area in your Flet application.

## Installation

Add the dependency to your Flet app's `pyproject.toml`:

```toml
dependencies = [
  "flet-desktop-drop @ git+https://github.com/Bbalduzz/flet-desktop-drop",
  "flet>=0.80.1",
]
```

## Quick Start

```python
import flet as ft
from flet_desktop_drop import Dropzone, DroppedFilesEvent


def main(page: ft.Page):
    def on_dropped(e: DroppedFilesEvent):
        if e.files:
            print(f"Accepted files: {e.files}")
        if e.rejected_files:
            print(f"Rejected files: {e.rejected_files}")

    dropzone = Dropzone(
        content=ft.Container(
            content=ft.Text("Drop files here"),
            width=300,
            height=200,
            bgcolor=ft.Colors.BLUE_GREY_100,
            border_radius=10,
            alignment=ft.alignment.center,
        ),
        on_dropped=on_dropped,
        allowed_file_types=["pdf", "png", "jpg"],
    )

    page.add(dropzone)


ft.run(main)
```

## Features

- Drag and drop files from desktop onto your Flet app
- Filter files by extension with `allowed_file_types`
- Visual feedback with `on_entered` and `on_exited` events
- Access both accepted and rejected files in the drop event

## Platform Support

This control works on desktop platforms:

- macOS
- Windows
- Linux

and any other platform supported by the desktop-drop flutter package.

## API Reference

See [API Reference](api.md) for detailed documentation.
