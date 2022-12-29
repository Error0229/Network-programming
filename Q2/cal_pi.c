#include<stdio.h>
#include<stdlib.h>
#include<pthread.h>
#include <time.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
void* cal_pi(void* data){
    double* data_double = (double*)data;
    double start = data_double[0];
    double end = data_double[1];
    double sum = 0;
    int i;
    for (i = start; i <= end; i++){
        if(i&1){
            sum += 1/(2*(double)i-1);
        }
        else {
            sum -= 1/(2*(double)i-1);
        }
        // printf("sum = %f\n", sum);
    }
    data_double[2] = sum;
}

void test1(){
    long begin_time, end_time;
    int status,i;
    begin_time = clock();
    pid_t  pid;
    double sum = 0;
    double start = 1, end = 30;
    double data[3] = {start, end, 0};
    double main_part[3] = {31,60,0};
    pid = fork();
    if (pid == 0){
        cal_pi((void*)data);
        int exits = data[2] * 100;
        exit(exits);
    }
    else if(pid>0){
        cal_pi((void*)main_part);
        wait(&status);
        i = WEXITSTATUS(status);
        sum = (double)i/100 + main_part[2];
        printf("sum = %f\n", sum*4.0);
        end_time = clock();
        printf("with process time = %ld\n", end_time-begin_time);
    }
}
void test2(){
    long begin_time, end_time;
    begin_time = clock();
    double sum = 0;
    double main_part[3] = {1,60,0};
    cal_pi((void*)main_part);
    sum = main_part[2];
    printf("sum = %f\n", sum*4.0);
    end_time = clock();
    printf("without process time = %ld\n", end_time-begin_time);
}
int main(){
    test1();
    test2();
}

