import os
import tomllib
from pathlib import Path
from unittest import TestCase

from bx_django_utils.filename import clean_filename
from bx_py_utils.path import assert_is_dir, assert_is_file
from django_tools.unittest_utils.project_setup import check_editor_config
from django_yunohost_integration.path_utils import get_project_root
from django_yunohost_integration.test_utils import assert_project_version
from for_runners import __version__ as upstream_version

from for_runners_ynh import __version__


def assert_file_contains_string(file_path, string):
    with file_path.open('r') as f:
        for line in f:
            if string in line:
                return
    raise AssertionError(f'File {file_path} does not contain {string!r} !')


def test_version():
    assert '+ynh' in __version__, f'{__version__!r} does not contain "+ynh"'
    assert upstream_version in __version__, f'{__version__!r} does not contain {upstream_version!r}'

    # pyproject.toml needs a PEP 440 conform version and used "+ynh"
    # the YunoHost syntax is: "~ynh", just "convert this:
    manifest_version = __version__.replace('+', '~')

    assert_file_contains_string(
        file_path=Path(get_project_root(), 'manifest.toml'),
        string=f'version = "{manifest_version}"',
    )

    if 'GITHUB_ACTION' not in os.environ:
        # Github has a rate-limiting... So don't fetch the API if we run as GitHub action
        assert_project_version(
            current_version=__version__,
            github_project_url='https://github.com/jedie/django-for-runners',
        )


def test_screenshot_filenames():
    """
    https://forum.yunohost.org/t/yunohost-bot-cant-handle-spaces-in-screenshots/19483
    """
    screenshot_path = get_project_root() / 'doc' / 'screenshots'
    assert_is_dir(screenshot_path)
    renamed = []
    for file_path in screenshot_path.iterdir():
        file_name = file_path.name
        if file_name.startswith('.'):
            continue
        cleaned_name = clean_filename(file_name)
        if cleaned_name != file_name:
            new_path = file_path.with_name(cleaned_name)
            file_path.rename(new_path)
            renamed.append(f'{file_name!r} renamed to {cleaned_name!r}')
    assert not renamed, f'Bad screenshots file names found: {", ".join(renamed)}'


def test_check_editor_config():
    check_editor_config(package_root=get_project_root())


class ManifestTestCase(TestCase):
    def test_manifest_toml(self):
        manifest_path = get_project_root() / 'manifest.toml'
        assert_is_file(manifest_path)

        cfg = tomllib.loads(manifest_path.read_text(encoding='UTF-8'))

        self.assertEqual(cfg['packaging_format'], 2)
        self.assertEqual(
            set(cfg['install'].keys()),
            {
                'admin',
                'admin_email',
                'debug_enabled',
                'default_from_email',
                'domain',
                'init_main_permission',
                'log_level',
                'path',
            },
        )
        self.assertEqual(
            set(cfg['resources'].keys()),
            {
                'apt',
                'data_dir',
                'database',
                'install_dir',
                'permissions',
                'ports',
                'system_user',
            },
        )
