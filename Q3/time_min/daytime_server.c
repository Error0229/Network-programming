#include <arpa/inet.h>
#include <math.h>
#include <netinet/in.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <time.h>
#include <unistd.h>
int main(int argc, char** argv)
{
    puts("QQ");
    printf("%s", argv[1]);
    printf("%d", atoi(argv[1]));
    int N = 0;
    char str[100];
    time_t ticks = time(NULL);
    int year = localtime(&ticks)->tm_year + 1900;
    int month = localtime(&ticks)->tm_mon + 1;
    int day = localtime(&ticks)->tm_mday;
    year -= 1911;
    sprintf(str, "%d/%d/%d", year, month, day);
    int* nptr = &N;
    double result = 0.0;
    double* resptr = &result;
    int sockfd = 0, clientSockfd = 0;
    sockfd = socket(AF_INET, SOCK_STREAM, 0);
    struct sockaddr_in serverInfo, clientInfo;
    int addrlen = sizeof(clientInfo);
    bzero(&serverInfo, sizeof(serverInfo));
    serverInfo.sin_family = AF_INET;
    serverInfo.sin_addr.s_addr = INADDR_ANY;
    serverInfo.sin_port = htons(atoi(argv[1]));
    bind(sockfd, (struct sockaddr*)&serverInfo, sizeof(serverInfo));
    listen(sockfd, 8);
    clientSockfd = accept(sockfd, (struct sockaddr*)&clientInfo, &addrlen);
    recv(clientSockfd, nptr, sizeof(N), 0);
    // recv(clientSockfd, nptr, sizeof(N), 0);
    send(clientSockfd, str, sizeof(str), 0);
    // printf("Get:%s\n",inputBuffer);
    return 0;
}
