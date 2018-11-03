#include <unistd.h>
#include <iostream>
#include <sys/socket.h>
#include <arpa/inet.h>

#include <cstring>
#include <stdio.h>
#include <stdlib.h>

#define MAXSIZE 1024

using namespace std;

class tcp_server
{
private:
        int socket_fd,accept_fd;
        sockaddr_in myserver;
        sockaddr_in remote_addr;

public:
        tcp_server(int listen_port);
        int recv_msg();
};
