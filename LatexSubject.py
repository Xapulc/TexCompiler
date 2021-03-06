import os
import subprocess


class LatexSubject(object):
    def __init__(self,
                 viewer: str,
                 editor: str,
                 source: str,
                 pattern: str,
                 desc: str,
                 path: str,
                 pdf_name: str = "document",
                 title: str = None):
        self._viewer = viewer
        self._editor = editor
        self._source = source
        self._pattern = pattern
        self._desc = desc
        self._path = path
        self._pdf = pdf_name
        self._title = title

    def get_desc(self):
        return self._desc

    def compile(self, targets: list):
        cur_path = os.path.abspath(".")
        os.chdir(os.path.join(self._path, self._source))

        if targets is not None and targets:
            for target in targets:
                file_name = f"{self._pdf}{target}"
                subprocess.run(["latexmk", "-quiet", "-pdf", f"{file_name}.tex"])
                subprocess.run(["rm", "-f", f"../{file_name}.pdf"])
                subprocess.run(["mv", f"{file_name}.pdf", f"../{file_name}.pdf"])
        else:
            for target in os.listdir("."):
                file_name = target[:-len(".tex")]
                subprocess.run(["latexmk", "-quiet", "-pdf", f"{file_name}.tex"])
                subprocess.run(["rm", "-f", f"../{file_name}.pdf"])
                subprocess.run(["mv", f"{file_name}.pdf", f"../{file_name}.pdf"])

        subprocess.run(["latexmk", "-c"])
        os.chdir(cur_path)

    def create(self, target: int):
        with open(self._pattern, "r") as pattern:
            tex_file = pattern.readlines()
            if self._title is not None:
                endline = tex_file[-1]
                tex_file[-1] = "\section*{" + f"{self._title} {target}" + "}\n"
                tex_file.append(endline)

            is_exists = False
            target_file = f"{self._pdf}{target}.tex"
            target_dir = os.path.join(self._path, self._source)
            if os.path.exists(target_dir):
                if os.path.exists(os.path.join(target_dir, target_file)):
                    is_exists = True
            else:
                os.mkdir(target_dir)

            if is_exists:
                print(f"File: {target_file} already exists")
            else:
                with open(os.path.join(target_dir, target_file), "w+") as newfile:
                    newfile.writelines(tex_file)

    def edit(self, target: int):
        subprocess.run([self._editor,
                        os.path.join(self._path, self._source, f"{self._pdf}{target}.tex")])

    def view(self, target: int):
        subprocess.run([self._viewer,
                        os.path.join(self._path, f"{self._pdf}{target}.pdf")])
