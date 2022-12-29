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
#define PORT 8885
int main()
{
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
    fp = fopen("recieve.txt", "w");
    while (1) {
        recv_len = recvfrom(s, buffer, BUFLEN, 0, (struct sockaddr*)&si_other, &slen);
        fprintf(fp, "%s", buffer);
        bzero(buffer, BUFLEN);
        // determine if the file is end
        if (recv_len < BUFLEN) {
            break;
        }
    }
    fclose(fp);
    close(s);
    return 0;
}