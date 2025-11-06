import argparse
import shutil
from pathlib import Path
import importlib.resources as resources

def list_docs():
    with resources.files("enterprise_docs.templates") as package_path:
        for f in package_path.iterdir():
            if f.suffix == ".md":
                print(f.name)

def copy_docs(destination: str):
    dest = Path(destination)
    dest.mkdir(parents=True, exist_ok=True)
    with resources.files("enterprise_docs.templates") as src:
        for f in src.iterdir():
            if f.suffix == ".md":
                shutil.copy(f, dest / f.name)
    print(f"✅ Copied documentation templates to {dest.resolve()}")

def main():
    parser = argparse.ArgumentParser(description="Enterprise Docs Manager")
    parser.add_argument("command", choices=["list", "sync"], help="list or sync documentation templates")
    parser.add_argument("--to", default="./docs", help="destination folder for sync")
    args = parser.parse_args()

    if args.command == "list":
        list_docs()
    elif args.command == "sync":
        copy_docs(args.to)

if __name__ == "__main__":
    main()