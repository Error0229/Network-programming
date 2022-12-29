#include <stdio.h>
#include <stdlib.h>
#include <sys/ipc.h>
#include <sys/shm.h>
#include <sys/types.h> // sf1.c
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
int main()
{
    pid_t pid;
    pid = fork();
    if (pid == 0) {

        int shm_id;
        key_t key;
        char *shm, *s;
        byte *pk, *pj;
        double k = 3.1415926535;
        double j = 1.6180339887;
        // 命名共享記憶體(shared memory segment) "567".
        // Create the segment.
        if ((shm_id = shmget(KEY, SHM_SIZE, IPC_CREAT | 0666)) < 0) {
            perror("shmget");
            printf("creat fail");
            exit(1);
        }
        if ((shm = shmat(shm_id, NULL, 0)) == (char*)-1) {
            perror("shmat");
            printf("attach fail");
            exit(1);
        }
        // 寫入資料到共享記憶體，等待其他 process 讀取
        pk = getBytes(&k);
        pj = getBytes(&j);
        s = shm;
        // 寫入double (8 bit) 到共享記憶體，
        // 等待其他 process 讀取
        for (int i = 0; i < 8; i++) {
            *s++ = pj[i];
        }
        for (int i = 0; i < 8; i++) {
            *s++ = pk[i];
        }
        while (*shm != '*') {
            sleep(1);
        }
        exit(0);
    } else {
        int shm_id, size = 16;
        char *shm, *s;
        byte p[8], k[8];
        double valuep, valuek;
        // sleep(3);
        // get the segment named "567", created by the server.
        //  Locate the segment.
        if ((shm_id = shmget(KEY, SHM_SIZE, 0666)) < 0) {
            perror("shmget");
            exit(1);
        }
        // attach the segment to our data space.
        if ((shm = shmat(shm_id, NULL, 0)) == (char*)-1) {
            perror("shmat");
            exit(1);
        }
        // read what the server put in the memory.
        s = shm;
        for (int i = 0; i < size; i++) {
            if (i < 8)
                p[i] = s[i];
            else
                k[i - 8] = s[i];
        }

        valuep = getValue(p);
        valuek = getValue(k);
        printf("\np = %.10f\nk = %.10f\n", valuep, valuek);
        // change the first character of the segment to '*',
        // indicating read the segment.
        *shm = '*';
    }
    //等待其他 process 修改記憶體第一個字元 '*',
    // 表示已經讀取本 process 寫入資料
    return 0;
}
