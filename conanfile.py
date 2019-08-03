from conans import ConanFile

class SvdDataConan(ConanFile):
    name = "svd-data"
    version = "0.1"
    license = "MIT"
    author = "Matthew Knight <mgk1795@gmail.com>"
    url = "https://github.com/matt1795/svd-data"
    description = "Collection of SVD files for different MCUs"
    topics = ("embeded", "mcu", "svd")
    exports_sources = "data/*"

    def package(self):
        self.copy("*", ".")
