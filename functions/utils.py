import os
import subprocess
from urllib.parse import urlparse
from urllib.parse import unquote_plus

def get_subprocess_output(cmdline, redirect_stderr=True, display_output_on_exception=True, logger=None, **kwargs):
    if redirect_stderr: kwargs['stderr'] = subprocess.STDOUT

    try:
        output = subprocess.check_output(cmdline, **kwargs)
        if logger: logger.debug('Subprocess {} complete. Output is "{}".'.format(cmdline, output))

        return output

    except subprocess.CalledProcessError as e:
        if display_output_on_exception and logger:
            logger.exception('Subprocess {} returned {}: '.format(cmdline, e.returncode, e.output.decode('ascii', errors='ignore')))

        raise
    #end try

    return ''
#end def


def get_ext(document_uri):
    o = urlparse(document_uri)
    _, ext = os.path.splitext(o.path)  # get format from extension
    ext = ext.lower()
    return ext
