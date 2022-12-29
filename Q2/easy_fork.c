#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>
int main()
{
    pid_t pid;
    int status, i;
    pid = fork();
    if (pid == 0) {
        double sum = 0;
        for (int i = 0; i <= 6; i++) {
            double k = 1;
            for (int j = 1; j <= i; j++) {
                k *= j;
            }
            sum += 1 / k;
        }
        printf("child pid: %d, child result: %.9f\n", getpid(), sum);
    } else if (pid > 0) {
        wait(&status);
        double sum = 0;
        for (int i = 7; i <= 12; i++) {
            double k = 1;
            for (int j = 1; j <= i; j++) {
                k *= j;
            }
            sum += 1 / k;
        }
        printf("parent pid: %d, parent result: %.9f\n", getpid(), sum);
    } else {
        printf("Error!\n");
    }
}
