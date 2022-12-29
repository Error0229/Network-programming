// cal Hn by given N using socket
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
    int sockfd = 0, clientSockfd = 0;
    sockfd = socket(AF_INET, SOCK_STREAM, 0);
    struct sockaddr_in serverInfo, clientInfo;
    int addrlen = sizeof(clientInfo);
    bzero(&serverInfo, sizeof(serverInfo));
    serverInfo.sin_family = AF_INET;
    serverInfo.sin_addr.s_addr = INADDR_ANY;
    serverInfo.sin_port = htons(8800);
    bind(sockfd, (struct sockaddr*)&serverInfo, sizeof(serverInfo));
    listen(sockfd, 8);
    clientSockfd = accept(sockfd, (struct sockaddr*)&clientInfo, &addrlen);
    int N = 0;
    int range[2];
    recv(clientSockfd, range, sizeof(range), 0);
    double Hn = 0.0;
    for (int i = range[0]; i <= range[1]; i++) {
        Hn += 1.0 / (double)(i);
    }
    printf("Calculate H(31) to H(60): %.6f\n", Hn);
    send(clientSockfd, &Hn, sizeof(Hn), 0);
    close(sockfd);
}