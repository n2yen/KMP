# Specify the minimum version for CMake
cmake_minimum_required(VERSION 2.8)
set(PROJ_NAME kmp)
# Project's name
project(${PROJ_NAME})

#set(SRCS kmp.cpp main.cpp)
set(SRCS kmp.cpp)
add_executable(${PROJ_NAME} ${SRCS})
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")

