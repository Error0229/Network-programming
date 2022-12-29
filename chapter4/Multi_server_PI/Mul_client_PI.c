#include <arpa/inet.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <unistd.h>
int main()
{
    int sockfd, connfd, len;
    struct sockaddr_in servaddr_1, servaddr_2;
    bzero(&servaddr_1, sizeof(servaddr_1));
    bzero(&servaddr_2, sizeof(servaddr_2));
    servaddr_1.sin_family = AF_INET;
    servaddr_2.sin_family = AF_INET;
    servaddr_1.sin_addr.s_addr = htonl(INADDR_ANY);
    servaddr_2.sin_addr.s_addr = htonl(INADDR_ANY);
    servaddr_1.sin_port = htons(8080);
    servaddr_2.sin_port = htons(7070);
    int N;
    double PI_1, PI_2;
    scanf("%d", &N);
    int data_1[2] = { 0, N / 2 };
    int data_2[2] = { N / 2, N };
    sockfd = socket(AF_INET, SOCK_STREAM, 0);
    connect(sockfd, (struct sockaddr*)&servaddr_1, sizeof(servaddr_1));
    send(sockfd, data_1, sizeof(data_1), 0);
    recv(sockfd, &PI_1, sizeof(PI_1), 0);
    close(sockfd);
    // printf("PI = %f\n", PI_1);
    sockfd = socket(AF_INET, SOCK_STREAM, 0);
    connect(sockfd, (struct sockaddr*)&servaddr_2, sizeof(servaddr_2));
    send(sockfd, data_2, sizeof(data_2), 0);
    recv(sockfd, &PI_2, sizeof(PI_2), 0);
    close(sockfd);
    printf("PI = %f\n", PI_1 + PI_2);
}