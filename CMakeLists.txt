project(CUSP LANGUAGES CXX CUDA)

find_package(GLUT)

# create a header-only library
add_library(cusp INTERFACE)
target_include_directories(cusp INTERFACE ${PROJECT_SOURCE_DIR})

# add a test executable
add_executable(cusp_example)
target_link_libraries(cusp_example 
    cusp
    ${CUDA_LIBRARIES}
    GLUT::GLUT)

# target_compile_definitions(cusp_example PRIVATE "-Dmain=example_main")
target_include_directories(cusp_example PRIVATE ${PROJECT_SOURCE_DIR}/catch2)
set_target_properties(cusp_example PROPERTIES CUDA_SEPARABLE_COMPILATION ON)
set_target_properties(cusp_example PROPERTIES CUDA_RESOLVE_DEVICE_SYMBOLS ON)
set_target_properties(cusp_example PROPERTIES CUDA_ARCHITECTURES 75)

file(GLOB_RECURSE HEADER_FILES "cusp/*.h")
file(GLOB_RECURSE CUDA_FILES "examples/*.cu")
set(CUDA_FILES ${CUDA_FILES} "example.cu")

target_sources(cusp_example PRIVATE  main.cpp ${CUDA_FILES} ${HEADER_FILES})

source_group(TREE ${PROJECT_SOURCE_DIR} FILES ${HEADER_FILES})
source_group(TREE ${PROJECT_SOURCE_DIR} FILES ${CUDA_FILES})
source_group(TREE ${PROJECT_SOURCE_DIR} FILES main.cpp)