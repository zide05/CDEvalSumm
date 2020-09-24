import argparse
import json
import os


def merge_dict(from_paths, to_path):
    result = {}
    for from_path in from_paths:
        tmp_data = json.load(open(from_path))
        for key, value in tmp_data.items():
            result[key] = value
    with open(to_path, "w") as tof:
        json.dump(result, tof)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-f_root", type=str, required=True)
    parser.add_argument("-f_paths", type=str, required=True)
    parser.add_argument("-t_path", type=str, required=True)
    args = parser.parse_args()

    root = args.f_root
    names = args.f_paths.split(",")
    merge_dict([os.path.join(root, name) for name in names], args.t_path)
