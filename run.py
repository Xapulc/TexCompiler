import argparse
import os
import sys
import yaml

from LatexSubject import LatexSubject

if __name__ == "__main__":
    with open("default_config.yaml") as yml:
        def_cfg = yaml.load(yml)
    with open("subjects.yaml") as yml:
        subjects_cfg = yaml.load(yml)

    subjects = {}
    for command_name, subject in subjects_cfg.items():
        subjects[command_name] = LatexSubject(def_cfg["editor"],
                                              def_cfg["source"],
                                              def_cfg["default_pattern"],
                                              subject["name"],
                                              subject["path"],
                                              pdf_name=subject.setdefault("pdf", "document"),
                                              title=subject.setdefault("title", None))

    # start parse
    parser = argparse.ArgumentParser(description="Support program for TeX projects",
                                     epilog=f"Projects: {list(subjects.keys())}")
    subparsers = parser.add_subparsers()

    # compile tex
    parser_compile = subparsers.add_parser("compile", help=f"compile one of project")
    parser_compile.add_argument("command_name", choices=subjects.keys(), type=str,
                                help="name of project")
    parser_compile.add_argument("numbers", default=None, nargs="*",
                                type=int, help="numbers of target files")
    parser_compile.set_defaults(func=lambda args: subjects[args.command_name].compile(args.numbers))

    # create tex from pattern
    parser_create = subparsers.add_parser("create", help=f"create new file in one of project")
    parser_create.add_argument("command_name", choices=subjects.keys(), type=str,
                               help="name of project")
    parser_create.add_argument("number", type=int, help="number of target files")
    parser_create.set_defaults(func=lambda args: subjects[args.command_name].create(args.number))

    # edit tex by config editor
    parser_edit = subparsers.add_parser("edit", help=f"edit tex in one of project")
    parser_edit.add_argument("command_name", choices=subjects.keys(), type=str,
                             help="name of project")
    parser_edit.add_argument("number", type=int, help="number of target files")
    parser_edit.set_defaults(func=lambda args: subjects[args.command_name].edit(args.number))

    args = parser.parse_args()
    args.func(args)
