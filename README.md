python-for-android
==================

[![Unit tests & build apps](https://github.com/kivy/python-for-android/workflows/Unit%20tests%20&%20build%20apps/badge.svg?branch=develop)](https://github.com/kivy/python-for-android/actions?query=workflow%3A%22Unit+tests+%26+build+apps%22)
[![Coverage Status](https://coveralls.io/repos/github/kivy/python-for-android/badge.svg?branch=develop&kill_cache=1)](https://coveralls.io/github/kivy/python-for-android?branch=develop)
[![Backers on Open Collective](https://opencollective.com/kivy/backers/badge.svg)](#backers)
[![Sponsors on Open Collective](https://opencollective.com/kivy/sponsors/badge.svg)](#sponsors)

python-for-android is a packaging tool for Python apps on Android. You can
create your own Python distribution including the modules and
dependencies you want, and bundle it in an APK or AAB along with your own code.

Features include:

-  Different app backends including Kivy, PySDL2, and a WebView with
   Python webserver.
-  Automatic support for most pure Python modules, and built in support
   for many others, including popular dependencies such as numpy and
   sqlalchemy.
-  Multiple architecture targets, for APKs optimised on any given
   device.
-  AAB: Android App Bundle support.

For documentation and support, see:

-  Website: http://python-for-android.readthedocs.io
-  Mailing list: https://groups.google.com/forum/#!forum/kivy-users or
   https://groups.google.com/forum/#!forum/python-android.

## Documentation

**Quick instructions**: install python-for-android with:

    pip install python-for-android

Test that the install works with:

    p4a --version

To build any actual apps, **set up the Android SDK and NDK**
as described in the [quickstart](
<https://python-for-android.readthedocs.org/en/latest/quickstart/#installing-android-sdk>).
**Use the SDK/NDK API level & NDK version as in the quickstart,**
other API levels may not work.

With everything installed, build an APK with SDL2 with e.g.:

    p4a apk --requirements=kivy --private /home/username/devel/planewave_frozen/ --package=net.inclem.planewavessdl2 --name="planewavessdl2" --version=0.5 --bootstrap=sdl2

**If you need to deploy your app on Google Play, Android App Bundle (aab) is required since 1 August 2021:**

**For full instructions and parameter options,** see [the
documentation](https://python-for-android.readthedocs.io/en/latest/quickstart/#usage).


See [our
documentation](https://python-for-android.readthedocs.io/en/latest/contribute/)
for more information about the python-for-android development and
release model, but don't worry about the details. You just need to
make a pull request, we'll take care of the rest.

The following mailing list and IRC channel are used exclusively for
discussions about developing the Kivy framework and its sister projects:

## License

python-for-android is released under the terms of the MIT License.
Please refer to the LICENSE file.

## History

In 2015 these tools were rewritten to provide a new, easier-to-use and
easier-to-extend interface.

In the last quarter of 2018 the python recipes were changed. The
new recipe for python3 (3.7.1) had a new build system which was
applied to the ancient python recipe, allowing us to bump the python2
version number to 2.7.15. This change unified the build process for
both python recipes, and probably solved various issues detected over the
years. These **unified python recipes** require a **minimum target api level of 21**,
*Android 5.0 - Lollipop*. If you need to build targeting an
api level below 21, you should use an older version of python-for-android
(<=0.7.1).

On March of 2020 we dropped support for creating apps that use Python 2. The latest
python-for-android release that supported building Python 2 was version 2019.10.6.

On August of 2021, we added support for Android App Bundle (aab). As a collateral,
now We support multi-arch apk.
