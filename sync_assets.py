import argparse
import hashlib
import json
import shutil
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parent
MANIFEST_PATH = ROOT_DIR / "asset_manifest.json"


def file_hash(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as file:
        for chunk in iter(lambda: file.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_manifest() -> list[dict[str, str]]:
    with MANIFEST_PATH.open("r", encoding="utf-8") as file:
        return json.load(file)


def resolve_target(relative_path: str) -> Path:
    target = (ROOT_DIR / relative_path).resolve()
    root = ROOT_DIR.resolve()
    if root != target and root not in target.parents:
        raise ValueError(f"Refusing to write outside project: {target}")
    return target


def sync_assets(dry_run: bool, only: str | None) -> int:
    changed = 0
    missing = 0

    for item in load_manifest():
        label = item["label"]
        if only and only not in label and only not in item["target"] and only not in item["source"]:
            continue

        source = Path(item["source"])
        target = resolve_target(item["target"])

        if not source.exists():
            missing += 1
            print(f"MISSING source: {label} -> {source}")
            continue

        source_hash = file_hash(source)
        target_hash = file_hash(target) if target.exists() else None

        if source_hash == target_hash:
            print(f"OK      {label}")
            continue

        changed += 1
        action = "WOULD UPDATE" if dry_run else "UPDATED"
        print(f"{action} {label}")

        if not dry_run:
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, target)

    print()
    print(f"Changed: {changed}")
    print(f"Missing sources: {missing}")

    return 1 if missing else 0


def main() -> None:
    parser = argparse.ArgumentParser(description="Sync source guide images into site assets.")
    parser.add_argument("--dry-run", action="store_true", help="Only report changes; do not copy files.")
    parser.add_argument("--only", help="Only sync entries whose label, source, or target contains this text.")
    args = parser.parse_args()

    raise SystemExit(sync_assets(dry_run=args.dry_run, only=args.only))


if __name__ == "__main__":
    main()
