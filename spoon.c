#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <stdlib.h>
int main(){
    pid_t pid;
    int status, i;
    pid = fork();
    if (pid == 0){
        sleep(50);
        printf("I am child\n");
        exit(6);
    }
    else if (pid > 0){
        printf("I am parent 1\n");
        sleep(5);
        printf("I am parent 2\n");
        wait(&status);
        i = WEXITSTATUS(status);
        printf("Child exited with status %d\n", i);
    }
    else{
        printf("Error!\n");
    }
}
