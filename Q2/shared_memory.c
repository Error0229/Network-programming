
#include <stdio.h>
#include <stdlib.h>
#include <sys/ipc.h>
#include <sys/shm.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <time.h>
#include <unistd.h>
#define SHM_SIZE 1024
#define KEY 567
typedef unsigned char byte;
double getValue(byte* p)
{
    double* pValue = (double*)p;
    return *pValue;
}
byte* getBytes(double* pValue)
{
    byte* p = (byte*)(pValue);
    return p;
}
void* cal_b(void* data)
{
    double* data_double = (double*)data;
    double start = data_double[0];
    double end = data_double[1];
    double sum = 0;
    int i;
    for (i = start; i <= end; i++) {
        sum += (((double)i - 1.) / (double)i);
        // printf("sum = %f\n", sum);
    }
    data_double[2] = sum;
}

void test1()
{
    long begin_time, end_time;
    int status, i;
    begin_time = clock();
    pid_t pid, pid2;
    double sum = 0;
    double start = 1, end = 30;
    double data[3] = { 1, 30, 0 };
    double main_part[3] = { 31, 60, 0 };
    pid = fork();
    if (pid == 0) {
        cal_b((void*)data);
        printf("child pid: %d, child result: %.9f\n", getpid(), data[2]);
        int shm_id;
        key_t key;
        char *shm, *s;
        byte *pk, *pj;
        double k;
        k = data[2];
        pk = getBytes(&k);
        s = shm;
        for (int i = 0; i < 8; i++) {
            *s++ = pk[i];
        }
        exit(0);
    } else if (pid > 0) {
        WEXITSTATUS(status);
        wait(&status);
        cal_b((void*)main_part);
        int shm_id, size = 16;
        char *shm, *s;
        byte p[8], k[8];
        double valuep, valuek = main_part[2];
        s = shm;
        for (int i = 0; i < 8; i++) {
            p[i] = s[i];
        }

        valuep = getValue(p);
        printf("parent pid: %d, parent result: %.9f\n", getpid(), valuep + valuek);
        *shm = '*';
    }
}
int main()
{
    test1();
}