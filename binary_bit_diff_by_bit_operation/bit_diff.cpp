#include "stdio.h"
#include "stdlib.h"
#include "iostream"

typedef unsigned int UINT32;
const UINT32 m1  = 0x55555555;  // 01010101010101010101010101010101
const UINT32 m2  = 0x33333333;  // 00110011001100110011001100110011
const UINT32 m4  = 0x0f0f0f0f;  // 00001111000011110000111100001111
const UINT32 m8  = 0x00ff00ff;  // 00000000111111110000000011111111
const UINT32 m16 = 0x0000ffff;  // 00000000000000001111111111111111
const UINT32 h01 = 0x01010101;  // the sum of 256 to the power of 0, 1, 2, 3

/* This is a naive implementation, shown for comparison, and to help in 
   * understanding the better functions. It uses 20 arithmetic operations
   * (shift, add, and). */
int popcount_1(UINT32 x)
{
      x = (x & m1) + ((x >> 1) & m1);
      x = (x & m2) + ((x >> 2) & m2);
      x = (x & m4) + ((x >> 4) & m4);
      x = (x & m8) + ((x >> 8) & m8);
      x = (x & m16) + ((x >> 16) & m16);
      return x;
}

/* This uses fewer arithmetic operations than any other known implementation
   * on machines with slow multiplication. It uses 15 arithmetic operations. */
int popcount_2(UINT32 x)
{
      x -= (x >> 1) & m1;             //put count of each 2 bits into those 2 bits
      x = (x & m2) + ((x >> 2) & m2); //put count of each 4 bits into those 4 bits 
      x = (x + (x >> 4)) & m4;        //put count of each 8 bits into those 8 bits 
      x += x >> 8;           //put count of each 16 bits into their lowest 8 bits
      x += x >> 16;          //put count of each 32 bits into their lowest 8 bits
      return x & 0x1f;
}

/* This uses fewer arithmetic operations than any other known implementation
   * on machines with fast multiplication. It uses 12 arithmetic operations, 
   * one of which is a multiply. */
int popcount_3(UINT32 x)
{
      x -= (x >> 1) & m1;             //put count of each 2 bits into those 2 bits
      x = (x & m2) + ((x >> 2) & m2); //put count of each 4 bits into those 4 bits 
      x = (x + (x >> 4)) & m4;        //put count of each 8 bits into those 8 bits 
      return (x * h01) >> 24;  // left 8 bits of x + (x<<8) + (x<<16) + (x<<24)
}

unsigned int hweight32(unsigned int w)
{
    unsigned int res = w - ((w >> 1) & 0x55555555);
    res = (res & 0x33333333) + ((res >> 2) & 0x33333333);
    res = (res + (res >> 4)) & 0x0F0F0F0F;
    res = res + (res >> 8);
    return (res + (res >> 16)) & 0x000000FF;
}

unsigned long long hweight32_test(unsigned long long w)
{
    unsigned long long res = w - ((w >> 1) & 0x55555555);
    res = (res & 0x33333333) + ((res >> 2) & 0x33333333);
    res = (res + (res >> 4)) & 0x0F0F0F0F;
    res = res + (res >> 8);
    return (res + (res >> 16)) & 0x000000FF;
}

unsigned long long hweight32_mycode(unsigned long long w)
{
    unsigned long long count = w;
    count = (count & 0x55555555) + ((count >> 1) & 0x55555555);
    count = (count & 0x33333333) + ((count >> 2) & 0x33333333);
    count = (count & 0x0F0F0F0F) + ((count >> 4) & 0x0F0F0F0F);
    count = (count & 0x00FF00FF) + ((count >> 8) & 0x00FF00FF);
    count = (count & 0x0000FFFF) + ((count >> 16) & 0x0000FFFF);
    return count;
}

unsigned long long hweight64(unsigned long long w)
{
    unsigned long long count = w;
    count = (count & 0x5555555555555555) + ((count >> 1) & 0x5555555555555555);
    count = (count & 0x3333333333333333) + ((count >> 2) & 0x3333333333333333);
    count = (count & 0x0F0F0F0F0F0F0F0F) + ((count >> 4) & 0x0F0F0F0F0F0F0F0F);
    count = (count & 0x00FF00FF00FF00FF) + ((count >> 8) & 0x00FF00FF00FF00FF);
    count = (count & 0x0000FFFF0000FFFF) + ((count >> 16) & 0x0000FFFF0000FFFF);
    count = (count & 0x00000000FFFFFFFF) + ((count >> 32) & 0x00000000FFFFFFFF);
    return count;
}
    
int main()
{
      int i = 0x1ff12ee2; 
      printf("i = %d = 0x%x %b\n", i, i, i);
      printf("popcount_1(%d) = %d\n", i, popcount_1(i));
      printf("popcount_2(%d) = %d\n", i, popcount_2(i));
      printf("popcount_3(%d) = %d\n", i, popcount_3(i));
      printf("hweight32(%d) = %d\n", i, hweight32(i));
      printf("hweight32_test(%d) = %d\n", i, hweight32_test(i));
      printf("hweight32_mycode(%d) = %d\n", i, hweight32_mycode(i));

      unsigned long long ii = 0x1ff12ee21ff12ee2;
      printf("hweight64(%llu) = %d\n", ii, hweight64(ii));
      /* If compiled with other compiler than gcc, comment the line bellow. */
      printf("GCC's  __builtin_popcount(%d) = %d\n", i,  __builtin_popcount(i));
      return 0;
}
