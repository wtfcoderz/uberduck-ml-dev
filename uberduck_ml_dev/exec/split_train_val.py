# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/exec.split_train_val.ipynb (unless otherwise specified).

__all__ = ['write_filenames', 'run', 'parse_args']

# Cell
import os
from pathlib import Path

import numpy as np
from sklearn.model_selection import train_test_split


def write_filenames(filenames, output_dir, output_filename):
    """
    Writes a list of filenames of as each line of a .txt file specified by output_filename.
    """
    with open(os.path.join(output_dir, output_filename), "w") as f:
        for item in filenames:
            f.write(f"{item}\n")


def run(
    path,
    val_percent=0.2,
    val_num=None,
    train_file="train.txt",
    val_file="val.txt",
):
    """Split file in t
    Default behavior only creates a training and validation set (not test set).
    """
    with open(path) as f:
        lines = [l.strip("\n") for l in f.readlines()]

    train, val = train_test_split(lines, test_size=val_num if val_num else val_percent)
    write_filenames(train, Path(os.path.dirname(path)), train_file)
    write_filenames(val, Path(os.path.dirname(path)), val_file)

# Cell
import argparse
import sys


def parse_args(args):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-i", "--in", dest="input_path", help="Path to input file list", required=True
    )
    parser.add_argument("-v", "--val-pct", dest="val_pct", type=float, default=0.1)
    args = parser.parse_args(args)
    return args


try:
    from nbdev.imports import IN_NOTEBOOK
except:
    IN_NOTEBOOK = False

if __name__ == "__main__" and not IN_NOTEBOOK:
    args = parse_args(sys.argv[1:])
    run(args.input_path, val_percent=args.val_pct)