"""Verify the published readable-text archive using Python's standard library."""
import hashlib
import json
from pathlib import Path


def main():
    root = Path(__file__).resolve().parent
    manifest = json.loads((root / "manifest.json").read_text(encoding="utf-8"))
    paths = set()
    errors = []
    total = 0
    for entry in manifest["files"]:
        rel = Path(entry["path"])
        if rel.is_absolute() or ".." in rel.parts or entry["path"] in paths:
            errors.append("Unsafe or duplicate path: " + entry["path"])
            continue
        paths.add(entry["path"])
        path = root / rel
        if not path.is_file() or path.is_symlink():
            errors.append("Missing file or symlink: " + entry["path"])
            continue
        data = path.read_bytes()
        total += len(data)
        checks = {
            "size_bytes": len(data),
            "sha256": hashlib.sha256(data).hexdigest(),
            "git_blob_sha1": hashlib.sha1(
                b"blob " + str(len(data)).encode("ascii") + b"\0" + data
            ).hexdigest(),
        }
        for key, actual in checks.items():
            if actual != entry[key]:
                errors.append(entry["path"] + ": " + key + " mismatch")
        try:
            data.decode("utf-8")
        except UnicodeDecodeError:
            errors.append(entry["path"] + ": invalid UTF-8")
    expected = manifest["inventory"]["new_unique_text_snapshots"]
    if len(paths) != expected:
        errors.append("Snapshot count mismatch")
    disk_paths = {str(p.relative_to(root)) for p in root.glob("*/*.txt")}
    if disk_paths != paths:
        errors.append("Unlisted or missing snapshot files")
    by_path = {e["path"]: e for e in manifest["files"]}
    for alias in manifest["duplicate_sources"]:
        target = by_path.get(alias["snapshot_path"])
        if target is None or target["sha256"] != alias["sha256"]:
            errors.append("Invalid duplicate mapping")
    report = {
        "status": "PASS" if not errors else "FAIL",
        "check": "archive integrity only; no scientific claims reverified",
        "snapshots_checked": len(paths),
        "snapshot_bytes": total,
        "duplicate_mappings_checked": len(manifest["duplicate_sources"]),
        "errors": errors,
    }
    print(json.dumps(report, indent=2))
    raise SystemExit(bool(errors))


if __name__ == "__main__":
    main()
