#!/usr/bin/env python3

"""
    Download and setup missing Python versions using eGenix PyRun from:

        https://github.com/eGenix/egenix-pyrun/
"""

import dataclasses
import json
import shutil
import subprocess
import sys
import tarfile
import urllib.request
from argparse import ArgumentParser
from pathlib import Path
from pprint import pprint

from urllib3.util import parse_url


DEFAULT_VERSION = '3.11'


GET_PIP_URL = 'https://bootstrap.pypa.io/get-pip.py'  # https://github.com/eGenix/egenix-pyrun/issues/11


@dataclasses.dataclass
class ReleaseInfo:
    version: str
    urls: list[str]

    def get(self, *, version):
        for url in self.urls:
            if f'-py{version}_' in url:
                return url


def get_pyrun_release_info() -> ReleaseInfo:
    api_url = "https://api.github.com/repos/eGenix/egenix-pyrun/releases"
    with urllib.request.urlopen(api_url) as response:
        data = response.read().decode()
        releases = json.loads(data)

    latest_release = releases[0]
    # pprint(latest_release)

    print(latest_release['html_url'])
    print(latest_release['tag_name'])
    print(latest_release['name'])

    urls = []
    for asset in latest_release['assets']:
        urls.append(asset['browser_download_url'])

    return ReleaseInfo(version=latest_release['name'], urls=urls)


def setup_pyrun(*, pyrun_version: str, destination: str):
    print('_' * 100)
    dest_path = Path(destination).expanduser()
    dest_path.mkdir(parents=True, exist_ok=True)
    print(f'Setup pyrun for Python {pyrun_version} to: {dest_path}')

    release_info = get_pyrun_release_info()
    pprint(release_info)

    python_bin_name = f'python{pyrun_version}'
    path = shutil.which(python_bin_name)
    if path:
        path = Path(path).resolve()
        print(f'Found {python_bin_name} at {path}')
        print(path.name)
        if path.name.startswith('pyrun'):
            print(f'{python_bin_name} is pyrun -> update')
        else:
            sys.exit(0)

    url = release_info.get(version=pyrun_version)
    if not url:
        print(f'No PyRun release found for Python {pyrun_version}')
        sys.exit(1)

    print(f'Download {url}')

    subprocess.check_call(
        ['wget', '--timestamp', url],
        cwd=dest_path,
    )

    filename = Path(parse_url(url).path).name
    print(f'{filename=}')
    tgz_path = dest_path / filename
    assert tgz_path.is_file(), f'{tgz_path=}'

    final_path = dest_path / f'pyrun{pyrun_version}/'
    print(f'Extract {tgz_path} to {final_path}...')
    final_path.mkdir(parents=False, exist_ok=True)
    with tarfile.open(tgz_path, "r:gz") as tgz_file:
        for member in tgz_file.getmembers():
            if ".." in member.name or member.name.startswith("/"):
                raise ValueError(f"Unsafe file path detected: {member.name}")
        tgz_file.extractall(path=final_path)

    tgz_path.unlink()

    pyrun_bin = final_path / 'bin' / f'pyrun{pyrun_version}'

    print(f'Install pip/virtualenv for Python {pyrun_version}')
    # FIXME: # https://github.com/eGenix/egenix-pyrun/issues/11
    subprocess.check_call(
        ['wget', '--timestamp', GET_PIP_URL],
        cwd=dest_path,
    )
    get_pip_path = dest_path / 'get-pip.py'

    subprocess.check_call(
        [pyrun_bin, get_pip_path],
    )
    get_pip_path.unlink()
    subprocess.check_call(
        [pyrun_bin, '-m', 'pip', 'install', '-U', 'virtualenv'],
    )
    print('\n')

    print(f'Check {pyrun_bin}:')
    subprocess.check_call([pyrun_bin, '-V'])

    print('\n')


if __name__ == '__main__':
    parser = ArgumentParser(description='Setup PyRun for a specific Python version.')
    parser.add_argument(
        '--version',
        type=str,
        default=DEFAULT_VERSION,
        help=f'Python version to setup with PyRun (default: {DEFAULT_VERSION}),',
    )
    parser.add_argument(
        '--destination',
        type=str,
        help=f'Destination path to store PyRun (e.g.: ~/.local/)',
    )
    args = parser.parse_args()

    setup_pyrun(
        pyrun_version=args.version,
        destination=args.destination,
    )
