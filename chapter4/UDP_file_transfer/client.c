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
#define PORT 8885
int main()
{
    char file_name[256];
    read(STDIN_FILENO, file_name, 256);
    file_name[strcspn(file_name, "\n")] = 0;
    FILE* file = fopen(file_name, "r");
    long file_size = 0;
    fseek(file, 0L, SEEK_END);
    file_size = ftell(file);
    fseek(file, 0L, SEEK_SET);
    struct sockaddr_in servaddr;
    bzero(&servaddr, sizeof(servaddr));
    int s;
    s = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP);

    servaddr.sin_family = AF_INET;
    servaddr.sin_port = htons(PORT);
    inet_aton(SERVER, &servaddr.sin_addr);
    int send_times = file_size / BUFLEN + 1;
    char buffer[BUFLEN];
    int i;
    for (i = 0; i < send_times; i++) {
        fread(buffer, 1, BUFLEN, file);
        sendto(s, buffer, BUFLEN, 0, (struct sockaddr*)&servaddr, sizeof(servaddr));
        bzero(buffer, BUFLEN);
    }
    // send end flag
    sendto(s, "end", 3, 0, (struct sockaddr*)&servaddr, sizeof(servaddr));

    fclose(file);
    close(s);
    return 0;
}