import Quartz


windows = Quartz.CGWindowListCopyWindowInfo(
    Quartz.kCGWindowListOptionOnScreenOnly,
    Quartz.kCGNullWindowID,
)

for window in windows:
    print(
        {
            "id": window.get("kCGWindowNumber"),
            "owner": window.get("kCGWindowOwnerName"),
            "title": window.get("kCGWindowName"),
            "bounds": window.get("kCGWindowBounds"),
        }
    )
