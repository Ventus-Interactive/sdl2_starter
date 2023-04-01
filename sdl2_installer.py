
cmd = 'sudo apt install '  #'git gcc'
cmd += "libsdl2-dev "
cmd += "libsdl2-image-dev "

from subprocess import run
run(cmd, shell=True)
