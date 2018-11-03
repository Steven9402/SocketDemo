cmake_minimum_required(VERSION 2.8.11)
project(sockettcp)
add_executable(tcp_server tcp_server.h tcp_server.cpp tcp_server_main.cpp)

add_executable(tcp_client tcp_client.h tcp_client.cpp tcp_client_main.cpp)

