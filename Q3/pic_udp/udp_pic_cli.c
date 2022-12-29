// client.c
#include <arpa/inet.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <unistd.h>
#define SERVER "127.0.0.1"
#define BUFLEN 255
#define PORT 50001
int main(int argc, char* argv[])
{

    FILE* file = fopen("recv_udp.png", "w");
    struct sockaddr_in servaddr;
    int s, i;
    s = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP);
    memset((char*)&servaddr, 0, sizeof(servaddr));
    servaddr.sin_family = AF_INET;
    servaddr.sin_port = htons(PORT);
    inet_aton(SERVER, &servaddr.sin_addr);
    servaddr.sin_addr.s_addr = inet_addr(SERVER);
    char buffer[BUFLEN];
    bzero(buffer, BUFLEN);
    int recv_len = 0;
    while (1) {
        sendto(s, buffer, 255, 0, (struct sockaddr*)&servaddr, sizeof(servaddr));
        recv_len = recvfrom(s, buffer, BUFLEN, 0, NULL, NULL);
        if (recv_len < BUFLEN) {
            break;
        }
        fwrite(buffer, 1, recv_len, file);
        bzero(buffer, BUFLEN);
    }
    fclose(file);
    close(s);
    return 0;
}