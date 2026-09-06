import Quartz


windows = Quartz.CGWindowListCopyWindowInfo(
    Quartz.kCGWindowListOptionOnScreenOnly,
    Quartz.kCGNullWindowID,
)

for window in windows:
    owner = window.get("kCGWindowOwnerName", "")
    title = window.get("kCGWindowName", "")
    bounds = window.get("kCGWindowBounds", {})
    width = int(bounds.get("Width", 0))
    height = int(bounds.get("Height", 0))
    owner_lower = owner.lower()
    title_lower = title.lower()

    if width >= 700 and height >= 500 and (
        "biubiubiu" in owner_lower
        or "biubiubiu" in title_lower
        or "raylib" in owner_lower
        or "raylib" in title_lower
    ):
        print(window["kCGWindowNumber"])
        break
