import asyncio
import random
import string
import tempfile
import aiofiles

from quart import Quart, render_template, request, send_file
from aiopath import AsyncPath

app = Quart(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True


def random_str(n: int):
    return "".join(
        random.SystemRandom().choice(string.ascii_uppercase + string.digits)
        for _ in range(n)
    )


@app.get("/")
async def home():
    return await render_template("index.html")


@app.post("/")
async def compile():
    form = await request.form
    data = form.get("content", type=str) or ""
    if len(data) > 5 * 1000:
        return "I think that's too much, sorry!", 4000

    tmpdir = AsyncPath(tempfile.gettempdir()).joinpath(random_str(8))
    await tmpdir.mkdir(exist_ok=True, parents=True)

    input_path = tmpdir.joinpath("input.kat")
    output_path = tmpdir.joinpath("compiled.kb")
    async with aiofiles.open(input_path, "w") as tmpinput:
        await tmpinput.write(data)

    proc = await asyncio.create_subprocess_shell(
        f"python build.py {await input_path.absolute()} {await output_path.absolute()}",
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )

    stdout, stderr = await proc.communicate()
    if proc.returncode != 0:
        return stdout, 400

    resp = await send_file(output_path, as_attachment=True)
    return resp


if __name__ == "__main__":
    app.run(port=5000, debug=True)
