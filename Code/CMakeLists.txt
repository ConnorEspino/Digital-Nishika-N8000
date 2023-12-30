cmake_minimum_required(VERSION 3.12)
project(MyProject)

set(CMAKE_CXX_STANDARD 11)

# FLTK requires additional configuration
find_package(FLTK REQUIRED)
include_directories(${FLTK_INCLUDE_DIRS})

# Set the source files
set(SOURCES
    src/main.cpp
    src/gui/MyWindow.h
    src/gui/MyWindow.cpp
)

# Create the main executable
add_executable(MyExecutable ${SOURCES})

# Link against FLTK libraries
target_link_libraries(MyExecutable ${FLTK_LIBRARIES})

# Additional targets for ArduCAM examples
add_executable(ov2640_capture IMPORTED)
set_target_properties(ov2640_capture PROPERTIES IMPORTED_LOCATION /home/pi/ArduCAM/example/RaspberryPi/ov2640_capture)
add_dependencies(MyExecutable ov2640_capture)

add_executable(ov5640_capture IMPORTED)
set_target_properties(ov5640_capture PROPERTIES IMPORTED_LOCATION /home/pi/ArduCAM/example/RaspberryPi/ov5640_capture)
add_dependencies(MyExecutable ov5640_capture)

add_executable(ov5642_capture IMPORTED)
set_target_properties(ov5642_capture PROPERTIES IMPORTED_LOCATION /home/pi/ArduCAM/example/RaspberryPi/ov5642_capture)
add_dependencies(MyExecutable ov5642_capture)

add_executable(ov2640_4cams_capture IMPORTED)
set_target_properties(ov2640_4cams_capture PROPERTIES IMPORTED_LOCATION /home/pi/ArduCAM/example/RaspberryPi/ov2640_4cams_capture)
add_dependencies(MyExecutable ov2640_4cams_capture)