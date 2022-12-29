// use socket to build a 1 to 1 chatting room
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
    char msg[1024];
    int sockfd = 0;
    sockfd = socket(AF_INET, SOCK_STREAM, 0);
    if (sockfd == -1) {
        printf("Fail to create a socket.");
    }
    struct sockaddr_in info;
    bzero(&info, sizeof(info));
    info.sin_family = AF_INET;
    info.sin_addr.s_addr = inet_addr("127.0.0.1");
    info.sin_port = htons(8700);
    int err = connect(sockfd, (struct sockaddr*)&info, sizeof(info));
    if (err == -1) {
        printf("Connection error");
    }
    while (1) {
        printf("Send To Server : ");
        fgets(msg, sizeof(msg), stdin);
        send(sockfd, msg, sizeof(msg), 0);
        if (strcmp(msg, "Bye\n") == 0) {
            puts("close socket");
            break;
        }
        recv(sockfd, msg, sizeof(msg), 0);
        printf("Receive From Server : %s", msg);
        if (strcmp(msg, "Bye\n") == 0) {
            puts("close socket");
            break;
        }
    }
    close(sockfd);
    return 0;
}