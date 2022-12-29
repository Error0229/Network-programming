#include <arpa/inet.h>
#include <ctype.h>
#include <math.h>
#include <netinet/in.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <unistd.h>
// use tcp to recv a file from server (pic_server.c)

#define SERVER "127.0.0.1"
#define BUFLEN 255
#define PORT 8880
int main()
{
    // receive file use udp
    FILE* file = fopen("recv_tcp.png", "w");
    struct sockaddr_in servaddr;
    int s, i;
    s = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP);
    memset((char*)&servaddr, 0, sizeof(servaddr));
    servaddr.sin_family = AF_INET;
    servaddr.sin_port = htons(PORT);
    servaddr.sin_addr.s_addr = inet_addr(SERVER);
    connect(s, (struct sockaddr*)&servaddr, sizeof(servaddr));
    char buffer[BUFLEN];
    int recv_len = 0;
    while (1) {
        send(s, buffer, 255, 0);
        recv_len = read(s, buffer, BUFLEN);
        fwrite(buffer, 1, recv_len, file);
        memset(buffer, 0, BUFLEN);
        if (recv_len < BUFLEN) {
            break;
        }
    }
    fclose(file);
    close(s);
    return 0;
}