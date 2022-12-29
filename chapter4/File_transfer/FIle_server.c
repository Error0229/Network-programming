#include <arpa/inet.h>
#include <math.h>
#include <netinet/in.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <unistd.h>

int main()
{
    // receive client.txt from client
    int sockfd, connfd;
    struct sockaddr_in servaddr, cli;
    bzero(&servaddr, sizeof(servaddr));
    servaddr.sin_family = AF_INET;
    servaddr.sin_addr.s_addr = htonl(INADDR_ANY);
    servaddr.sin_port = htons(8800);
    sockfd = socket(AF_INET, SOCK_STREAM, 0);
    bind(sockfd, (struct sockaddr*)&servaddr, sizeof(servaddr));
    listen(sockfd, 5);
    // listen is a function that blocks the execution of the program
    // until a client connects to the server
    int len = sizeof(cli);
    connfd = accept(sockfd, (struct sockaddr*)&cli, &len);
    // accept is a function that blocks the execution of the program
    // until a client sends a request to the server
    char buffer[256];
    FILE* fp = fopen("server.txt", "w");
    while (recv(connfd, buffer, sizeof(buffer), 0) > 0) {
        fprintf(fp, "%s", buffer);
        bzero(buffer, sizeof(buffer));
    }
    fclose(fp);
    close(sockfd);
    close(connfd);
    return 0;
}