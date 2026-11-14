"""Bman Downloader - start the app from this file (and build the exe from it).

bman_core.py and bman_ui.py must sit next to it."""
from __future__ import annotations

import sys

from bman_core import Index, IndexLoadError
from bman_ui import ArchiveGUI


def main() -> int:
    try:
        index = Index.load_combined()
    except IndexLoadError as exc:
        # Open anyway: the window explains what went wrong and Settings can fix it.
        print(str(exc), file=sys.stderr)
        index = Index.empty(str(exc))

    app = ArchiveGUI(index)
    app.mainloop()
    return 0

if __name__ == "__main__":
    if sys.platform == "win32" and not getattr(sys, 'frozen', False) and "__compiled__" not in globals():
        import ctypes
        try:
            kernel32 = ctypes.WinDLL('kernel32')
            user32 = ctypes.WinDLL('user32')
            hWnd = kernel32.GetConsoleWindow()
            if hWnd:
                user32.ShowWindow(hWnd, 0)
        except Exception:
            pass
    sys.exit(main())
