import 'package:flet/flet.dart';
import 'package:flutter/material.dart';
import 'package:desktop_drop/desktop_drop.dart';

class DropzoneControl extends StatefulWidget {
  final Control control;

  const DropzoneControl({
    super.key,
    required this.control,
  });

  @override
  State<DropzoneControl> createState() => _DropzoneControlState();
}

class _DropzoneControlState extends State<DropzoneControl> {
  bool _dragging = false;

  List<String> get _allowedFileTypes {
    // Python field name is snake_case: allowed_file_types
    final types = widget.control.get<List<dynamic>>("allowed_file_types");
    if (types == null) return [];
    return types.map((e) => e.toString().toLowerCase()).toList();
  }

  void _onDragDone(List<String> acceptedFiles, List<String> rejectedFiles) {
    // Pass raw Map with both accepted and rejected files
    widget.control.triggerEvent("dropped", {
      "files": acceptedFiles,
      "rejected_files": rejectedFiles,
    });
  }

  void _onDragEntered() {
    widget.control.triggerEvent("entered");
  }

  void _onDragExited() {
    widget.control.triggerEvent("exited");
  }

  @override
  Widget build(BuildContext context) {
    debugPrint(
        "Dropzone build: ${widget.control.id} (${widget.control.hashCode})");

    bool disabled = widget.control.disabled;

    // Get content child using buildWidget
    Widget? contentWidget = widget.control.buildWidget("content");
    Widget child = contentWidget ?? Container();

    Widget dropZone = DropTarget(
      onDragEntered: (details) {
        setState(() {
          _dragging = true;
        });
        _onDragEntered();
      },
      onDragExited: (details) {
        setState(() {
          _dragging = false;
        });
        _onDragExited();
      },
      onDragDone: (details) {
        List<String> allFiles = details.files.map((file) => file.path).toList();
        List<String> acceptedFiles = [];
        List<String> rejectedFiles = [];

        // Separate files into accepted and rejected based on allowed_file_types
        for (final filePath in allFiles) {
          if (_allowedFileTypes.isEmpty) {
            acceptedFiles.add(filePath);
          } else {
            final extension = filePath.split('.').last.toLowerCase();
            if (_allowedFileTypes.contains(extension)) {
              acceptedFiles.add(filePath);
            } else {
              rejectedFiles.add(filePath);
            }
          }
        }

        setState(() {
          _dragging = false;
        });

        // Always fire event so user gets feedback about rejected files too
        _onDragDone(acceptedFiles, rejectedFiles);
      },
      enable: !disabled,
      child: child,
    );

    return LayoutControl(control: widget.control, child: dropZone);
  }
}
