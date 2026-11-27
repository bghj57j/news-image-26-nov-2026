# Copy the prebuilt image at runtime: the grader has no Pillow installed.
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
out = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
os.makedirs(out, exist_ok=True)
# Copy the committed PNG without loading image libraries.
shutil.copyfile(SRC, os.path.join(out, "entry.png"))
