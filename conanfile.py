from conans import ConanFile, CMake, tools

class Testlib2(ConanFile):
    name = "testlib2"
    description = "This is another TEST!"
    homepage = "https://tnt-coders.gitlab.io/cpp/libraries/testlib2"
    url = "https://gitlab.com/tnt-coders/cpp/libraries/testlib2"
    license = "GNU Lesser General Public License v3.0"
    author = "TNT Coders <tnt-coders@googlegroups.com>"

    topics = ("testlib2")

    settings = ("os", "compiler", "build_type", "arch")

    options = {
        "shared": [True, False],
    }

    default_options = {
        "shared": False,
    }


    build_requires = (
        "catch2/3.0.0-1@tnt-coders/stable"
    )

    exports_sources = ("CMakeLists.txt", "docs/*", "images/*", "include/*", "src/*", "test/*")
    
    generators = ("cmake", "cmake_paths")

    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.configure()
        return cmake

    def configure(self):
        tools.check_min_cppstd(self, "17")

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()
        cmake.test()

    def package(self):
        cmake = self._configure_cmake()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)