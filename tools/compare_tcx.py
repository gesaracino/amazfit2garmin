from pathlib import Path
import xml.etree.ElementTree as ET


def strip_namespace(tag: str) -> str:
    if "}" in tag:
        return tag.split("}", 1)[1]
    return tag


def flatten(element, prefix=""):
    data = {}

    name = strip_namespace(element.tag)

    current = f"{prefix}/{name}" if prefix else name

    text = (element.text or "").strip()

    if text:
        data[current] = text

    for key, value in element.attrib.items():
        data[f"{current}@{key}"] = value

    children = list(element)

    for index, child in enumerate(children):

        child_name = strip_namespace(child.tag)

        duplicates = [
            c
            for c in children
            if strip_namespace(c.tag) == child_name
        ]

        if len(duplicates) > 1:
            child_prefix = f"{current}/{child_name}[{index}]"
        else:
            child_prefix = current

        data.update(flatten(child, child_prefix))

    return data


def compare(file_a: Path, file_b: Path):

    tree_a = ET.parse(file_a)
    tree_b = ET.parse(file_b)

    a = flatten(tree_a.getroot())
    b = flatten(tree_b.getroot())

    keys = sorted(set(a.keys()) | set(b.keys()))

    print("=" * 80)

    print(f"A : {file_a}")
    print(f"B : {file_b}")

    print("=" * 80)

    for key in keys:

        va = a.get(key)
        vb = b.get(key)

        if va == vb:
            continue

        print()
        print(key)
        print(f"    ours   : {va}")
        print(f"    garmin : {vb}")


if __name__ == "__main__":

    compare(
        Path("samples/our_generated_run.tcx"),
        Path("samples/garmin_reference_run.tcx"),
    )