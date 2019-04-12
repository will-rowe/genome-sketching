import subprocess
import tempfile

def _exec_notebook(path):
    with tempfile.NamedTemporaryFile(suffix=".ipynb") as fout:
        args = ["jupyter", "nbconvert", "--to", "notebook", "--execute",
                "--ExecutePreprocessor.timeout=1000",
                "--output", fout.name, path]
        subprocess.check_call(args)


def test():
    _exec_notebook('notebooks/Background.ipynb')
    _exec_notebook('notebooks/r3.1.Set-similarity-with-MinHash.ipynb')
    _exec_notebook('notebooks/r3.2.Set-membership-with-Bloom-filters.ipynb')
    _exec_notebook('notebooks/r3.3.Element-frequency-with-Count-Min-sketch.ipynb')
    _exec_notebook('notebooks/r3.4.Set-cardinality-with-HyperLogLog.ipynb')