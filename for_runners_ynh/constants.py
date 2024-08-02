from pathlib import Path

import for_runners_ynh
from bx_py_utils.path import assert_is_file


PACKAGE_ROOT = Path(for_runners_ynh.__file__).parent.parent
assert_is_file(PACKAGE_ROOT / 'pyproject.toml')


CLI_EPILOG = 'Project Homepage: https://github.com/YunoHost-Apps/django-for-runners_ynh'
