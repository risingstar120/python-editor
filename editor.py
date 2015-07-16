#!/usr/bin/env python
"""Tools for invoking editors programmatically."""

from __future__ import print_function

import locale
import os.path
import subprocess
import tempfile
from distutils.spawn import find_executable


__all__ = [
    'edit',
    'get_editor',
    'EditorError',
]


class EditorError(RuntimeError):
    pass


def get_default_editors():
    # TODO: Make platform-specific
    return [
        'vim',
        'emacs',
        'nano',
    ]


def get_editor_args(editor):
    if editor in ['vim', 'gvim']:
        return '-f -o'

    elif editor == 'emacs':
        return '-nw'

    elif editor == 'gedit':
        return '-w --new-window'

    elif editor == 'nano':
        return '-R'

    else:
        return ''


def get_platform_editor_var():
    # TODO: Make platform specific
    return "$EDITOR"


def get_editor():
    # Get the editor from the environment.  Prefer VISUAL to EDITOR
    editor = os.environ.get('VISUAL') or os.environ.get('EDITOR')
    if editor:
        return editor

    # None found in the environment.  Fallback to platform-specific defaults.
    for ed in get_default_editors():
        path = find_executable(ed)
        if path is not None:
            return path

    raise EditorError("Unable to find a viable editor on this system."
        "Please consider setting your %s variable" % get_platform_editor_var())


def edit(filename=None, contents=None):
    editor = get_editor()
    args = get_editor_args(os.path.basename(editor))
    args = [editor] + args.split(' ')

    if filename is None:
        tmp = tempfile.NamedTemporaryFile()
        filename = tmp.name

    if contents is not None:
        with open(filename, mode='wb') as f:
            f.write(contents)

    args += [filename]

    proc = subprocess.Popen(args, close_fds=True)
    proc.communicate()

    with open(filename, mode='rb') as f:
        return f.read()


def _get_editor(ns):
    print(get_editor())


def _edit(ns):
    contents = ns.contents
    if contents is not None:
        contents = contents.encode(locale.getpreferredencoding())
    print(edit(filename=ns.path, contents=contents))


if __name__ == '__main__':
    import argparse
    ap = argparse.ArgumentParser()
    sp = ap.add_subparsers()

    cmd = sp.add_parser('get-editor')
    cmd.set_defaults(cmd=_get_editor)

    cmd = sp.add_parser('edit')
    cmd.set_defaults(cmd=_edit)
    cmd.add_argument('path', type=str, nargs='?')
    cmd.add_argument('--contents', type=str)

    ns = ap.parse_args()
    ns.cmd(ns)
