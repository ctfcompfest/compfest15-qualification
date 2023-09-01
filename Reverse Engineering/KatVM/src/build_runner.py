import base64
import py_compile
from pathlib import Path
import tempfile

modules: list[tuple[str, bytes]] = []
build_dir = Path(__file__).parent

with tempfile.TemporaryDirectory() as tmpdir:
    for file in [
        build_dir.joinpath("runner").joinpath("utils.py"),
        build_dir.joinpath("runner").joinpath("vm.py"),
        build_dir.joinpath("runner").joinpath("katvm.py"),
    ]:
        module = file.stem
        target_pyc = Path(tmpdir).joinpath(module + ".pyc")
        py_compile.compile(file, cfile=target_pyc)  # type: ignore

        with open(target_pyc, "rb") as f:
            modules.append((module, base64.b64encode(f.read())))

with open(build_dir.joinpath("bootstrap.py.tmpl"), "r") as f:
    templ = f.read()

templ = templ.replace("{{DATA}}", str(modules))
with open(build_dir.joinpath("run_katvm.py"), "w") as f:
    f.write(templ)
