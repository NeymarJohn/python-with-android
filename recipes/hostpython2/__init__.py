
from toolchain import Recipe, shprint, get_directory, current_directory
from os.path import join, exists
from os import chdir
import sh


class Hostpython2Recipe(Recipe):
    version = '2.7.2'
    url = 'http://python.org/ftp/python/{version}/Python-{version}.tar.bz2'
    name = 'hostpython2'

    def prebuild_armeabi(self):
        # Override hostpython Setup?
        print('Running hostpython2 prebuild')
        shprint(sh.cp, join(self.get_recipe_dir(), 'Setup'),
                join(self.get_build_dir('armeabi'),
                     get_directory(self.versioned_url),
                     'Modules', 'Setup'))

    def build_armeabi(self):
        # AND: Should use an i386 recipe system
        print('Running hostpython build. Arch is armeabi! '
              'This is naughty, need to fix the Arch system!')

        # AND: Fix armeabi again
        with current_directory(join(self.get_build_dir('armeabi'),
                                    get_directory(self.versioned_url))):

            if exists('hostpython'):
                print('hostpython already exists, skipping build')
                self.ctx.hostpython = join(self.get_build_dir('armeabi'),
                                           get_directory(self.versioned_url),
                                           'hostpython')
                self.ctx.hostpgen = join(self.get_build_dir('armeabi'),
                                           get_directory(self.versioned_url),
                                           'hostpgen')
                return
            
            configure = sh.Command('./configure')
            print('Configuring hostpython2')

            shprint(configure)
            shprint(sh.make, '-j5')

            shprint(sh.mv, join('Parser', 'pgen'), 'hostpgen')

            if exists('python.exe'):
                shprint(sh.mv, 'python.exe', 'hostpython')
            elif exists('python'):
                shprint(sh.mv, 'python', 'hostpython')
            else:
                print('Unable to find the python executable after '
                      'hostpython build!')
                exit(1)

        self.ctx.hostpython = join(self.get_build_dir('armeabi'),
                                   get_directory(self.versioned_url),
                                   'hostpython')
        self.ctx.hostpgen = join(self.get_build_dir('armeabi'),
                                   get_directory(self.versioned_url),
                                   'hostpgen')

        
        

        


recipe = Hostpython2Recipe()
