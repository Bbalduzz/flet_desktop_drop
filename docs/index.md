# Introduction

FletDropzoneV2 for Flet.

## Examples

```
import flet as ft

from flet_dropzone_v2 import FletDropzoneV2


def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.add(

                ft.Container(height=150, width=300, alignment = ft.Alignment.CENTER, bgcolor=ft.Colors.PURPLE_200, content=FletDropzoneV2(
                    tooltip="My new FletDropzoneV2 Control tooltip",
                    value = "My new FletDropzoneV2 Flet Control", 
                ),),

    )


ft.run(main)
```

## Classes

[FletDropzoneV2](FletDropzoneV2.md)


