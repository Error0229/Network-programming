// server.c
#include <arpa/inet.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <unistd.h>
#define BUFLEN 255
#define PORT 50001
int main(int argc, char* argv[])
{
    // send file use udp
    struct sockaddr_in si_self, si_other;
    int s, slen = sizeof(si_other), recv_len = 0;
    FILE* fp;
    s = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP);
    memset((char*)&si_self, 0, sizeof(si_self));
    si_self.sin_family = AF_INET;
    si_self.sin_port = htons(PORT);
    si_self.sin_addr.s_addr = htonl(INADDR_ANY);
    bind(s, (struct sockaddr*)&si_self, sizeof(si_self));
    char buffer[BUFLEN];
    fp = fopen(argv[1], "r");
    // get file size
    fseek(fp, 0, SEEK_END);
    int file_size = ftell(fp);
    fseek(fp, 0, SEEK_SET);
    // send file size

    recv_len = recvfrom(s, buffer, BUFLEN, 0, (struct sockaddr*)&si_other, &slen);
    int send_times = file_size / BUFLEN + 1;
    int i;
    for (i = 0; i < send_times; i++) {
        fread(buffer, 1, BUFLEN, fp);
        sendto(s, buffer, BUFLEN, 0, (struct sockaddr*)&si_other, slen);
        bzero(buffer, BUFLEN);
    }
    // send end flag
    sendto(s, "end", 3, 0, (struct sockaddr*)&si_other, slen);
    fclose(fp);
    close(s);
    return 0;
}