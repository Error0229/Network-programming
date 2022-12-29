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

int main()
{
    int i, len;
    char string[1024];
    fgets(string, 1024, stdin);
    len = strlen(string);
    for (i = 0; i < len; i++) {
        if (!isalpha(string[i])) {
            continue;
        }
        string[i] += 5;
        if (string[i] > 'z')
            string[i] -= 26;
        if (string[i] > 'Z' && string[i] < 'a')
            string[i] -= 26;
    }
    FILE* file = fopen("client.txt", "w");
    fprintf(file, "%s", string);
    fclose(file);
    int sockfd;
    struct sockaddr_in servaddr;
    bzero(&servaddr, sizeof(servaddr));
    servaddr.sin_family = AF_INET;
    servaddr.sin_addr.s_addr = inet_addr("127.0.0.1");
    servaddr.sin_port = htons(8800);
    sockfd = socket(AF_INET, SOCK_STREAM, 0);
    int err = connect(sockfd, (struct sockaddr*)&servaddr, sizeof(servaddr));
    if (err == -1) {
        printf("Connection with the server failed...\n");
        exit(0);
    }
    // transfer client.txt to server
    // split the file into chunks of 256 byte
    FILE* fp = fopen("client.txt", "r");
    char buffer[256];
    while (fgets(buffer, 256, fp) != NULL) {
        send(sockfd, buffer, sizeof(buffer), 0);
        bzero(buffer, sizeof(buffer));
    }
}