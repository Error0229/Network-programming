// use socket to build a 1 to 1 chatting room
#include <arpa/inet.h>
#include <netinet/in.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <unistd.h>
// server
int main(int argc, char* argv[])
{
    char msg[1024];
    int sockfd = 0, clientSockfd = 0;
    sockfd = socket(AF_INET, SOCK_STREAM, 0);
    struct sockaddr_in serverInfo, clientInfo;
    int addrlen = sizeof(clientInfo);
    bzero(&serverInfo, sizeof(serverInfo));
    serverInfo.sin_family = AF_INET;
    serverInfo.sin_addr.s_addr = INADDR_ANY;
    serverInfo.sin_port = htons(8700);
    bind(sockfd, (struct sockaddr*)&serverInfo, sizeof(serverInfo));
    listen(sockfd, 8);
    clientSockfd = accept(sockfd, (struct sockaddr*)&clientInfo, &addrlen);
    while (1) {
        recv(clientSockfd, msg, sizeof(msg), 0);
        if (strcmp(msg, "Bye\n") == 0) {
            puts("close socket");
            break;
        }
        printf("Receive From Client : %s", msg);
        printf("Send To Client : ");
        fgets(msg, sizeof(msg), stdin);
        send(clientSockfd, msg, sizeof(msg), 0);
        if (strcmp(msg, "Bye\n") == 0) {
            puts("close socket");
            break;
        }
    }
    close(sockfd);
}