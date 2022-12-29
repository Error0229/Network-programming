#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h> // f3.c
#include <sys/wait.h>
#include <unistd.h>
int main()
{
    int value = 0;
    pid_t pid;
    int fd[2];
    pipe(fd);
    pid = fork(); // fork a child process
    if (pid < 0) { // error occurred
        fprintf(stderr, "Fork Failed");
        return 1;
    } else if (pid == 0) { // child process
        close(fd[0]);
        value = 15;
        printf("child value=%d\n", value);
        write(fd[1], &value, sizeof(value));
        close(fd[1]);
    } else { // parent process
        wait(NULL); // parent wait child complete
        read(fd[0], &value, sizeof(value));
        printf("Child Complete\n");
        printf("parent value=%d\n", value);
        close(fd[0]);
    }
    return 0;
}