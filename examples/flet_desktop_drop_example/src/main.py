import os

import flet as ft

from flet_desktop_drop import DroppedFilesEvent, Dropzone


class Colors:
    BLACK = "#000000"
    WHITE = "#FFFFFF"
    GRAY_50 = "#FAFAFA"
    GRAY_100 = "#F5F5F5"
    GRAY_200 = "#E5E5E5"
    GRAY_300 = "#D4D4D4"
    GRAY_400 = "#A3A3A3"
    GRAY_500 = "#737373"
    GRAY_600 = "#525252"
    GRAY_800 = "#262626"
    GRAY_900 = "#171717"
    BLUE = "#2563EB"
    RED = "#DC2626"


def main(page: ft.Page):
    page.title = "Dropzone"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 40
    page.bgcolor = Colors.WHITE
    page.fonts = {
        "Inter": "https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap"
    }
    page.theme = ft.Theme(font_family="Inter")

    # State
    is_dragging = False

    # Components
    icon = ft.Icon(
        icon=ft.Icons.UPLOAD_FILE_OUTLINED,
        size=32,
        color=Colors.GRAY_400,
    )

    primary_text = ft.Text(
        value="Drop files here",
        size=14,
        weight=ft.FontWeight.W_500,
        color=Colors.GRAY_800,
    )

    secondary_text = ft.Text(
        value="PDF files only",
        size=12,
        weight=ft.FontWeight.W_400,
        color=Colors.GRAY_500,
    )

    status_text = ft.Text(
        value="",
        size=12,
        weight=ft.FontWeight.W_400,
        color=Colors.GRAY_500,
    )

    files_column = ft.Column(
        controls=[],
        spacing=4,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    def create_file_chip(filename: str, accepted: bool):
        return ft.Container(
            content=ft.Row(
                controls=[
                    ft.Icon(
                        icon=ft.Icons.CHECK_CIRCLE_OUTLINE
                        if accepted
                        else ft.Icons.CANCEL_OUTLINED,
                        size=14,
                        color=Colors.GRAY_600 if accepted else Colors.RED,
                    ),
                    ft.Text(
                        value=filename,
                        size=12,
                        weight=ft.FontWeight.W_400,
                        color=Colors.GRAY_800 if accepted else Colors.RED,
                    ),
                ],
                spacing=6,
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            padding=ft.Padding(left=10, right=10, top=4, bottom=4),
            border_radius=4,
            bgcolor=Colors.GRAY_100 if accepted else "#FEF2F2",
        )

    def on_dropped(e: DroppedFilesEvent):
        files_column.controls.clear()

        # Add accepted files
        for f in e.files:
            files_column.controls.append(create_file_chip(os.path.basename(f), True))

        # Add rejected files
        for f in e.rejected_files:
            files_column.controls.append(create_file_chip(os.path.basename(f), False))

        if e.files or e.rejected_files:
            count = len(e.files) + len(e.rejected_files)
            accepted = len(e.files)
            if accepted == count:
                status_text.value = (
                    f"{accepted} file{'s' if accepted != 1 else ''} accepted"
                )
                status_text.color = Colors.GRAY_600
            elif accepted == 0:
                status_text.value = f"{count} file{'s' if count != 1 else ''} rejected"
                status_text.color = Colors.RED
            else:
                status_text.value = (
                    f"{accepted} accepted, {len(e.rejected_files)} rejected"
                )
                status_text.color = Colors.GRAY_600
        else:
            status_text.value = ""

        dropzone_container.border = ft.Border.all(1.5, Colors.GRAY_200)
        page.update()

    def on_entered(e):
        dropzone_container.border = ft.Border.all(1.5, Colors.BLUE)
        dropzone_container.bgcolor = Colors.GRAY_50
        icon.color = Colors.BLUE
        page.update()

    def on_exited(e):
        dropzone_container.border = ft.Border.all(1.5, Colors.GRAY_200)
        dropzone_container.bgcolor = Colors.WHITE
        icon.color = Colors.GRAY_400
        page.update()

    dropzone_container = ft.Container(
        content=ft.Column(
            controls=[
                ft.Container(height=24),
                icon,
                ft.Container(height=12),
                primary_text,
                ft.Container(height=2),
                secondary_text,
                ft.Container(height=16),
                files_column,
                status_text,
                ft.Container(height=24),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=0,
        ),
        width=360,
        bgcolor=Colors.WHITE,
        border_radius=8,
        border=ft.Border.all(1.5, Colors.GRAY_200),
        alignment=ft.Alignment.CENTER,
    )

    dropzone = Dropzone(
        content=dropzone_container,
        on_dropped=on_dropped,
        on_entered=on_entered,
        on_exited=on_exited,
        allowed_file_types=["pdf"],
    )

    page.add(
        ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text(
                        value="Dropzone",
                        size=18,
                        weight=ft.FontWeight.W_600,
                        color=Colors.BLACK,
                    ),
                    ft.Container(height=4),
                    ft.Text(
                        value="Drag and drop files to upload",
                        size=13,
                        weight=ft.FontWeight.W_400,
                        color=Colors.GRAY_500,
                    ),
                    ft.Container(height=32),
                    dropzone,
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=0,
            ),
            padding=40,
        )
    )


ft.run(main)
