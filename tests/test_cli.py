import depfinder
import subprocess
import os
from os.path import dirname, join

def test_cli():
    output = subprocess.check_output(
        ['depfinder', dirname(depfinder.__file__)],
        env=dict(os.environ)).decode()
    dependencies_file = join(dirname(dirname(depfinder.__file__)),
                             'requirements.txt')
    print(output)
    dependencies = set([dep for dep in open(dependencies_file, 'r').read().split('\n') if dep])
    assert dependencies == set(eval(output)['required'])
