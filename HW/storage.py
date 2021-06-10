import os
import tempfile
import json
import argparse


def read_file(file_path):
    if not os.path.exists(file_path):
        return {}
    with open(file_path, "r") as f:
        file_content = f.read()
        if file_content:
            return json.loads(file_content)
        return {}


def write_file(file_path, content):
    with open(file_path, "w") as f:
        f.write(json.dumps(content))


def parser():
    parsed = argparse.ArgumentParser()
    parsed.add_argument("--key")
    parsed.add_argument("--value")
    return parsed.parse_args()


def get_value(file_path, key):
    data = read_file(file_path)
    return data.get(key, [])


def put_value(file_path, key, value):
    data = read_file(file_path)
    data[key] = data.get(key, list())
    data[key].append(value)
    write_file(file_path, data)


def main(file_path):
    args = parser()

    if args.key and args.value:
        put_value(file_path, args.key, args.value)
    elif args.key:
        print(", ".join(get_value(file_path, args.key)))
    else:
        print("lame")


if __name__ == "__main__":
    storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
    main(storage_path)
