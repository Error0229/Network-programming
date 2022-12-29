#include <arpa/inet.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <unistd.h>
double cal_PI(int start, int end)
{
    double PI = 0;
    for (int i = start; i < end; i++) {
        PI += 4.0 * (1 - (i % 2) * 2) / (2 * i + 1);
    }
    return PI;
}

int main()
{
    int sockfd, connfd, len;
    struct sockaddr_in servaddr, cli;
    bzero(&servaddr, sizeof(servaddr));
    servaddr.sin_family = AF_INET;
    servaddr.sin_addr.s_addr = htonl(INADDR_ANY);
    servaddr.sin_port = htons(7070);
    while (1) {
        sockfd = socket(AF_INET, SOCK_STREAM, 0);
        bind(sockfd, (struct sockaddr*)&servaddr, sizeof(servaddr));
        listen(sockfd, 5);
        connfd = accept(sockfd, (struct sockaddr*)&cli, &len);
        int data[2];
        recv(connfd, data, sizeof(data), 0);
        double PI = cal_PI(data[0], data[1]);
        send(connfd, &PI, sizeof(PI), 0);
        close(sockfd);
    }
}
