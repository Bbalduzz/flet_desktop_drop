from dataclasses import dataclass, field
from typing import Any, Callable, List, Optional

import flet as ft
from flet.controls.control_event import Event, EventControlType


@dataclass(kw_only=True)
class DroppedFilesEvent(Event[EventControlType]):
    """Event fired when files are dropped onto the Dropzone."""

    files: List[str] = field(default_factory=list, metadata={"data_field": "files"})
    """List of accepted file paths (matching allowed_file_types filter)."""

    rejected_files: List[str] = field(
        default_factory=list, metadata={"data_field": "rejected_files"}
    )
    """List of rejected file paths (not matching allowed_file_types filter)."""


# Type alias for the on_dropped handler
DroppedFilesHandler = Callable[[DroppedFilesEvent], Any] | None


@ft.control("Dropzone")
class Dropzone(ft.LayoutControl):
    """
    A control that accepts file drops from the desktop.

    This control wraps the Flutter `desktop_drop` package and allows users
    to drag and drop files onto the control area.

    Properties:
        content: The child control to display inside the dropzone.
        allowed_file_types: List of allowed file extensions (e.g., ["pdf", "jpg"]).
                           If empty, all file types are allowed.

    Events:
        on_dropped: Fired when files are dropped. Receives DroppedFilesEvent with:
            - files: List of accepted file paths
            - rejected_files: List of rejected file paths (wrong extension)
        on_entered: Fired when a drag operation enters the dropzone.
        on_exited: Fired when a drag operation exits the dropzone.

    Example:
        ```python
        import flet as ft
        from flet_desktop_drop import Dropzone, DroppedFilesEvent

        def main(page: ft.Page):
            def on_dropped(e: DroppedFilesEvent):
                if e.files:
                    print(f"Accepted: {e.files}")
                if e.rejected_files:
                    print(f"Rejected: {e.rejected_files}")

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
    """

    content: Optional[ft.Control] = None
    allowed_file_types: List[str] = field(default_factory=list)

    on_dropped: DroppedFilesHandler = None
    on_entered: Optional[ft.ControlEventHandler["Dropzone"]] = None
    on_exited: Optional[ft.ControlEventHandler["Dropzone"]] = None

    def _get_children(self) -> List[ft.Control]:
        children = []
        if self.content is not None:
            self.content._set_attr_internal("n", "content")
            children.append(self.content)
        return children

    async def _trigger_event(self, event_name: str, event_data: Any) -> None:
        """Override to handle custom DroppedFilesEvent."""
        if event_name == "dropped" and self.on_dropped is not None:
            # Create our custom event with files and rejected_files
            if isinstance(event_data, dict):
                files = event_data.get("files", [])
                rejected_files = event_data.get("rejected_files", [])
            else:
                files = []
                rejected_files = []

            e = DroppedFilesEvent(
                name=event_name,
                control=self,
                files=files,
                rejected_files=rejected_files,
            )
            handler = self.on_dropped
            if callable(handler):
                result = handler(e)
                if result is not None and hasattr(result, "__await__"):
                    await result
        else:
            # Delegate to parent for other events
            await super()._trigger_event(event_name, event_data)
