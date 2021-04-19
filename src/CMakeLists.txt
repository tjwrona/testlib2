tnt_project_AddLibrary(${PROJECT_NAME}
  TARGET
    ${PROJECT_NAME}
  SOURCES
    testlib2.cpp
)

target_compile_features(${PROJECT_NAME} PUBLIC cxx_std_17)