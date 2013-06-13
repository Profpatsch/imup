# Maintainer: Profpatsch <mail[at]profpatsch[dot]de>
pkgname=imup
pkgver=0.2.2
pkgrel=1
pkgdesc="Upload an image to an image host and return the link to the file."
url="https://github.com/Profpatsch/imup"
arch=('any')
license=('GPLv3')
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
md5sums=() #generate with 'makepkg -g'

pkgver() {
  echo $pkgname
}

build() {
  # Use the tag of the last commit
  git checkout $pkgver
  RETVAL=$?
  if [ $RETVAL -ne 0 ]; then
    msg "Couldn’t check out tag of last version ($pkgver) from GIT. Checking out master instead."
  fi
}

package() {
  cd $_gitname
  python setup.py install --root="$pkgdir/" --optimize=1
}

# vim:set ts=2 sw=2 et:
