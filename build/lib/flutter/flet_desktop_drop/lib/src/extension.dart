import 'package:flet/flet.dart';
import 'package:flutter/widgets.dart';

import 'flet_desktop_drop.dart';

class Extension extends FletExtension {
  @override
  Widget? createWidget(Key? key, Control control) {
    switch (control.type) {
      case "Dropzone":
        return DropzoneControl(key: key, control: control);
      default:
        return null;
    }
  }
}
