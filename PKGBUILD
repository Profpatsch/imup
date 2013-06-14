# Maintainer: Profpatsch <mail[at]profpatsch[dot]de>
pkgname=imup
pkgver=0.2.2
pkgrel=1
pkgdesc="Upload an image to an image host and return the link to the file."
url="https://github.com/Profpatsch/imup"
arch=('any')
license=('GPL3')
depends=('python2')
makedepends=('git')
optdepends=()
conflicts=()
replaces=()
backup=()
groups=()
provides=()
options=()
install=
source=(git+https://github.com/Profpatsch/imup.git)
noextract=()
md5sums=('SKIP') #generate with 'makepkg -g'

build() {
  cd $pkgname
  # Use the tag of the specified version
  git checkout $pkgver || \
    msg "Couldn’t check out tag of last version ($pkgver) from GIT. Checking out master instead."
}

package() {
  cd $pkgname
  echo $pkgdir/
  python2 setup.py install --root="$pkgdir/" --optimize=1

  # Link executable in /usr/bin
  # Get link of executable
  EXECUTABLE_PATH=$(python2 << EOFINTERNAL
import distutils.sysconfig
print distutils.sysconfig.get_python_lib()
EOFINTERNAL
  )
  mkdir -p $pkgdir/usr/bin
  ln -s $EXECUTABLE_PATH/imup.py $pkgdir/usr/bin/$pkgname

  # Make imup executable
  chmod 755 $pkgdir/$EXECUTABLE_PATH/imup.py
}

# vim:set ts=2 sw=2 et:
