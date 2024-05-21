import py_compile
from distutils.core import setup
from Cython.Build import cythonize

from Cython.Distutils import build_ext

import sysconfig
import os


class NoSuffixBuilder(build_ext):
    def get_ext_filename(self, ext_name):
        filename = super().get_ext_filename(ext_name)
        suffix = sysconfig.get_config_var("EXT_SUFFIX")
        ext = os.path.splitext(filename)[1]
        return filename.replace(suffix, "") + ext

file_list = [
    "app/config/config.py",
    "app/one/__init__.py",
    "app/one/one.py",
    "app/second/__init__.py",
    "app/second/second.py",
    "app/__init__.py",
    "app/run.py",
]


setup(
    cmdclass={"build_ext": NoSuffixBuilder},
    ext_modules=cythonize(file_list, force=True, compiler_directives={'language_level': '3', "annotation_typing": False})
)

py_compile.compile("main.py","build/lib.linux-aarch64-cpython-310/main.pyc")
