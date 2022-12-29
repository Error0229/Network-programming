#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
double _sum;
void* calb(void* data)
{
    int input = *(int*)data;
    int i;
    double sum = 0;
    for (i = 1; i <= input; i++) {
        if (i & 1)
            sum += 1. / (double)i;
        else
            sum -= 1. / (double)i;
    }
    _sum = sum;
    pthread_exit(NULL);
}

int main(int argc, char* argv[])
{
    int i;
    double db20, db30;
    int b20 = 20, b30 = 30;
    int* b20p = &b20;
    int* b30p = &b30;
    int t1, t2, t3;
    pthread_t thread1, thread2, thread3;
    t1 = pthread_create(&thread1, NULL, (void*)calb, (void*)b20p);

    pthread_join(thread1, NULL);
    printf("thread1: %.9f\n", _sum);
    db20 = _sum;
    t2 = pthread_create(&thread2, NULL, (void*)calb, (void*)b30p);
    pthread_join(thread2, NULL);
    printf("thread2: %.9f\n", _sum);
    db30 = _sum;
    printf("main: %.9f\n", db30 / db20);
}
