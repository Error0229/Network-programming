
#include <arpa/inet.h>
#include <netinet/in.h>
#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/ipc.h>
#include <sys/mman.h>
#include <sys/shm.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <time.h>
#include <unistd.h>
typedef unsigned char byte;
#define SHM_SIZE 2048
#define KEY 5678
static double* glob_var;
// client sen range to server

int main(int argc, char* argv[])
{
    glob_var = mmap(NULL, sizeof *glob_var, PROT_READ | PROT_WRITE,
        MAP_SHARED | MAP_ANONYMOUS, -1, 0);
    int status;
    *glob_var = 0;
    int data[2][2] = { { 1, 30 }, { 31, 60 } };
    pid_t pid;
    pid = fork();
    if (pid == 0) {
        int sockfd = 0;
        sockfd = socket(AF_INET, SOCK_STREAM, 0);
        struct sockaddr_in serverInfo;
        bzero(&serverInfo, sizeof(serverInfo));
        serverInfo.sin_family = AF_INET;
        serverInfo.sin_addr.s_addr = inet_addr("127.0.0.1");
        serverInfo.sin_port = htons(8700);
        connect(sockfd, (struct sockaddr*)&serverInfo, sizeof(serverInfo));
        send(sockfd, data[0], sizeof(data[0]), 0);
        double Hn = 0.0;
        recv(sockfd, &Hn, sizeof(Hn), 0);
        *glob_var = Hn;

        exit(0);
    } else {
        WEXITSTATUS(status);
        wait(&status);

        int sockfd = 0;
        sockfd = socket(AF_INET, SOCK_STREAM, 0);
        struct sockaddr_in serverInfo;
        bzero(&serverInfo, sizeof(serverInfo));
        serverInfo.sin_family = AF_INET;
        serverInfo.sin_addr.s_addr = inet_addr("127.0.0.1");
        serverInfo.sin_port = htons(8800);
        connect(sockfd, (struct sockaddr*)&serverInfo, sizeof(serverInfo));
        send(sockfd, data[1], sizeof(data[1]), 0);
        double Hn = 0.0;
        recv(sockfd, &Hn, sizeof(Hn), 0);

        double ps1 = *glob_var, ps2 = Hn, total;

        printf("Parent server result : %.6f\n", ps1);
        printf("Child server result : %.6f\n", ps2);
        total = ps1 + ps2;
        printf("H(1,60): %.6f\n", total);

        exit(0);
    }
}