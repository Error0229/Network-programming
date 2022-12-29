#include <arpa/inet.h>
#include <math.h>
#include <netinet/in.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <unistd.h>
// send file to client use tcp and split the file into 255 bytes
int main(int argc, char* argv[])
{
    // send file use tcp
    FILE* file = fopen(argv[1], "r");
    struct sockaddr_in servaddr;
    int s, i;
    s = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP);
    memset((char*)&servaddr, 0, sizeof(servaddr));
    servaddr.sin_family = AF_INET;
    servaddr.sin_port = htons(8880);
    servaddr.sin_addr.s_addr = htonl(INADDR_ANY);
    bind(s, (struct sockaddr*)&servaddr, sizeof(servaddr));
    listen(s, 10);
    int client = accept(s, NULL, NULL);
    char buffer[255];
    int send_len = 0;
    while (1) {
        send_len = fread(buffer, 1, 255, file);
        send(client, buffer, send_len, 0);
        if (send_len < 255) {
            break;
        }
        // sleep(1);
        recv(client, buffer, 255, 0);
        memset(buffer, 0, 255);
    }
    fclose(file);
    close(s);
    return 0;
}