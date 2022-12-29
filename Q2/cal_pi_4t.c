#include<stdio.h>
// #include<stdlib.h>
#include<pthread.h>
#include <time.h>
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
    pthread_t t1, t2, t3;
    double sum = 0;
    begin_time = clock();
    double data1[3] = {3,22,0}, data2[3] = {23,42,0}, data3[3] = {43,62,0};
    pthread_create(&t1, NULL, cal_pi, (void*)data1);
    pthread_create(&t2, NULL, cal_pi, (void*)data2);
    pthread_create(&t3, NULL, cal_pi, (void*)data3);
    pthread_join(t1, NULL);
    pthread_join(t2, NULL);
    pthread_join(t3, NULL);
    sum = 1.0 - (double)1/3 + data1[2] + data2[2] + data3[2];
    printf("sum = %f\n", sum*4.0);
    end_time = clock();
    printf("with thread time = %ld\n",(end_time-begin_time)*100/CLOCKS_PER_SEC);
}
void test2(){
    long begin_time, end_time;
    double sum = 0;
    double main_part[3] = {1.0,62.0,0};
    begin_time = clock();
    cal_pi((void*)main_part);
    sum = main_part[2];
    printf("sum = %f\n", sum*4.0);
    end_time = clock();
    printf("without thread time = %ld\n", (end_time-begin_time)*100/CLOCKS_PER_SEC);
}
int main(){
    test1();
    test2();
}

