#include <arpa/inet.h>
#include <netinet/in.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <unistd.h>
int main(int argc, char* argv[])
{
    int N = 0;
    int* nptr = &N;
    char str[100];
    int sockfd = 0;
    sockfd = socket(AF_INET, SOCK_STREAM, 0);
    if (sockfd == -1) {
        printf("Fail to create a socket.");
    }
    struct sockaddr_in info;
    bzero(&info, sizeof(info));
    info.sin_family = PF_INET;
    info.sin_addr.s_addr = inet_addr(argv[1]);
    int port_n = atoi(argv[2]);
    info.sin_port = htons(port_n);
    int err = connect(sockfd, (struct sockaddr*)&info, sizeof(info));
    puts("connect success");
    if (err == -1) {
        printf("Connection error");
    }
    // while (1) {
    send(sockfd, nptr, sizeof(N), 0);
    recv(sockfd, str, sizeof(str), 0);
    printf("%s", str);
    // printf("%.10f\n", result);
    // }
    close(sockfd);
    return 0;
}