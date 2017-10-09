
/* ======================================================================
         KNAPSACK CONTAINER LOADING PROBLEMS, David Pisinger 1998
   ====================================================================== */

/* This code generates instances for the knapsack container loading 
 * problem and solves them using the "contload" algorithm.
 *
 * A description of the test instances is found in:
 *
 *   D.Pisinger (1999)
 *   "A tree search algorithm for the container loading problem"
 *   to appear in Ricerca Operativa.
 *
 * This algorithm prompts for four arguments:
 *   mindim  Minimum dimension of the boxes to be packed
 *   maxdim  Maximum dimension of the boxes to be packed
 *   fillpct Boxes are generated until fillpct percent of the container volume
 *   maxtyp  Number of different box types 
 *
 * Results are written to the file "contload.out".
 *
 * (c) Copyright, December 1998,
 *   David Pisinger                     
 *   DIKU, University of Copenhagen      
 *   Universitetsparken 1              
 *   Copenhagen, Denmark               
 *
 * This code can be used free of charge for research and academic purposes
 * only.
 */              


/* ======================================================================
				   constants
   ====================================================================== */

#define MAXITEMS           1000        /* max number of boxes */
#define TESTS                20        /* number of test instances solved */

#include <stdlib.h>
#include <stdio.h>
#include <time.h>
#include <stdarg.h>
#include <float.h>
#include <string.h>
#include <limits.h>


/* ======================================================================
                                     macros
   ====================================================================== */

#define VOL(i)                 ((i)->dx * (long) (i)->dy * (i)->dz)
#define srand(x)               srand48x(x)
#define randm(x)               (lrand48x() % (long) (x))


/* ======================================================================
                                global variables
   ====================================================================== */

FILE *trace;


/* ======================================================================
				 type declarations
   ====================================================================== */

typedef short         boolean; /* logical variable       */
typedef short         ntype;   /* number of states,bins  */
typedef short         itype;   /* can hold up to W,H,D   */
typedef long          stype;   /* can hold up to W*H*D   */
typedef double        ptype;   /* product type           */

typedef int (*funcptr) (const void *, const void *);

/* item record */
typedef struct irec {
  short    no;    /* item number */
  itype    dx;    /* box x-size */
  itype    dy;    /* box y-size */
  itype    dz;    /* box z-size */
  itype    x;     /* optimal x-position */
  itype    y;     /* optimal y-position */
  itype    z;     /* optimal z-position */
  boolean  k;     /* knapsack solution */
} item;


/* **********************************************************************
   **********************************************************************
                             Small procedures
   **********************************************************************
   ********************************************************************** */



/* =======================================================================
                                random
   ======================================================================= */

/* to generate the same instances as at HP9000 - UNIX, */
/* here follows C-versions of SRAND48, and LRAND48.  */

unsigned long _h48, _l48;

void srand48x(long s)
{
  _h48 = s;
  _l48 = 0x330E;
}

long lrand48x(void)
{
  _h48 = (_h48 * 0xDEECE66D) + (_l48 * 0x5DEEC);
  _l48 = _l48 * 0xE66D + 0xB;
  _h48 = _h48 + (_l48 >> 16);
  _l48 = _l48 & 0xFFFF;
  return (_h48 >> 1);
}


/* **********************************************************************
   **********************************************************************
                             Timing routines
   **********************************************************************
   ********************************************************************** */

/* This timing routine is based on the ANSI-C procedure "clock", which
 * has a resolution of 1000000 ticks per second. This however implies
 * that we pass the limit of a long integer after only 4295 seconds.
 * The following routine attempts to correct such situations by adding
 * the constant ULONG_MAX to the counter whenever wraparound can be
 * detected. But the user is advised to use a timing routine like "times"
 * (which however is not ANSI-C standard) for measuring longer time
 * periods.
 */

void timeused(double *time)
{
  static double tstart, tend, tprev;

  if (time == NULL) {
    clock(); /* one extra call to initialize clock */
    tstart = tprev = clock();
  } else {
    tend = clock();
    if (tend < tprev) tstart -= ULONG_MAX; /* wraparound occured */
    tprev = tend;
    *time = (tend-tstart) / CLOCKS_PER_SEC; /* convert to seconds */
  }
}


/* **********************************************************************
   **********************************************************************
                             Test generation
   **********************************************************************
   ********************************************************************** */

/* ======================================================================
                             checksol
   ====================================================================== */

/* check correctnes of solution, i.e. no items overlap, no duplicated items */

void checksol(item *f, item *l, int W, int H, int D, int vol)
{
  item *i, *j, *m;
  int svol;

  for (i = f, m = l+1, svol = 0; i != m; i++) {
    if (!i->k) continue;  /* item currently not chosen */ 
    svol += VOL(i);
    if ((i->x + i->dx > W) || (i->y + i->dy > H) || (i->z + i->dz > D)) {
      printf("badplace item %d [%d,%d,%d] %d,%d,%d\n",
            i->no, i->dx, i->dy, i->dz, i->x, i->y, i->z); 
      exit(-1);
    }
    for (j = f; j != m; j++) {
      if (i == j) continue;
      if (i->no == j->no) { printf("duplicated item %d\n", i->no); exit(-1); }
      if (!j->k) continue;
      if ((i->x + i->dx > j->x) && (j->x + j->dx > i->x) &&
          (i->y + i->dy > j->y) && (j->y + j->dy > i->y) &&
          (i->z + i->dz > j->z) && (j->z + j->dz > i->z)) {
        printf("overlap item %d,%d: [%d,%d,%d] [%d,%d,%d]",
              i->no, j->no, i->dx, i->dy, i->dz, j->dx, j->dy, j->dz);
        exit(-1); 
      }
    }
  }
  if (vol != svol) { 
    printf("incorrect objective %d %d\n", vol, svol); exit(-1); 
  }
}


/* ======================================================================
				printinstance
   ====================================================================== */

void printinstance(item *f, item *l, itype W, itype H, itype D)
{
  item *i;
  itype x1, y1, z1;
  stype vol, totvol;

  vol = 0; totvol = W * (ptype) H * D;
  fprintf(trace,"printinstance n=%d\n", (int) (l-f+1));
  fprintf(trace," no [ dx, dy, dz]   x   y   z packed\n");
  for (i = f; i <= l; i++) {
    x1 = i->dx; y1 = i->dy; z1 = i->dz;
    fprintf(trace,"%3d [%3d,%3d,%3d] %3d %3d %3d %s\n",
            (int)(i-f+1), x1, y1, z1, i->x, i->y, i->z, (i->k ? "yes" : "no"));
   if (i->k) vol += VOL(i);
  }
  fprintf(trace,"TOTAL VOLUME %ld OF %ld FILL %f\n", 
          vol, totvol, vol/(double)(totvol));
  fflush(trace);
}


/* ======================================================================
                                randomtype
   ====================================================================== */

void randomtype(item *i, int mindim, int maxdim)
{
  i->dx = randm(maxdim-mindim+1) + mindim;
  i->dy = randm(maxdim-mindim+1) + mindim;
  i->dz = randm(maxdim-mindim+1) + mindim;
  i->x = i->y = i->z = i->k = 0;
}


/* ======================================================================
                                maketest
   ====================================================================== */

void maketest(item *f, item **l, int *mx, int *my, int *mz,
              int mindim, int maxdim, int fillpct, int maxtyp)
{
  item t[MAXITEMS];
  register item *i, *j, *m;
  register stype vol;
  int no;

  *mx = 230;
  *my = 230;
  *mz = 590;

  /* make maxtypes item types */
  for (i = t, m = t+maxtyp; i != m; i++) {
    randomtype(i, mindim, maxdim);
    /* printf("type (%hd,%hd,%hd) vol %ld\n", i->dx, i->dy, i->dz, VOL(i)); */
  }

  /* generate till "fillpct" of container is filled */
  vol = (fillpct * *mx * (double) *my * *mz) / 100;
  for (i = f, no = 1; ; i++, no++) {
    if (i == *l) { printf("too small array"); exit(-1); }
    if (maxtyp == 0) { 
      randomtype(i, mindim, maxdim); 
    } else {
      j  = t + randm(maxtyp); *i = *j; 
    }
    i->no = no; vol -= VOL(i);
    if (vol < 0) { *l = i; break; }
  }
  printf("maketest: generated %d boxes\n", (int)(*l-f+1));
}


/* ======================================================================
                                prepareitems
   ====================================================================== */

void prepareitems(item *f, item *l, int *w, int *h, int *d)
{
  item *i;
  int k;

  for (i = f, k = 0; i != l+1; i++, k++) {
    w[k] = i->dx; h[k] = i->dy; d[k] = i->dz;
  }
}


/* ======================================================================
                                updateitems
   ====================================================================== */

void updateitems(item *f, item *l, int *w, int *h, int *d, 
                 int *x, int *y, int *z, int *k, int *miss)
{
  item *i;
  int j;
  
  *miss = 0;
  for (i = f, j = 0; i != l+1; i++, j++) {
    i->dx = w[j]; i->dy = h[j]; i->dz = d[j]; 
    i->x  = x[j]; i->y  = y[j]; i->z  = z[j]; i->k = k[j];
    if (!k[j]) (*miss)++; 
  }
}


/* ======================================================================
				main
   ====================================================================== */

int main(int argc, char *argv[])
{
  int v, n, mindim, maxdim, fillpct, maxtyp;
  item *f, *l;
  int W, H, D, cvol, vol, miss;
  item tab[MAXITEMS];
  int w[MAXITEMS], h[MAXITEMS], d[MAXITEMS]; 
  int x[MAXITEMS], y[MAXITEMS], z[MAXITEMS], k[MAXITEMS];
  double time, sumtime, sumfill, sumn, summiss;
  char s[100];

  if (argc == 5) {
    mindim  = atoi(argv[1]);
    maxdim  = atoi(argv[2]);
    fillpct = atoi(argv[3]);
    maxtyp  = atoi(argv[4]); 
    printf("CONTAINER LOADING [%d,%d] %d %d\n",mindim,maxdim,fillpct,maxtyp);
  } else {
    printf("CONTAINER LOADING\n");
    printf("mindim  = ");
    scanf("%d", &mindim);
    printf("maxdim  = ");
    scanf("%d", &maxdim);
    printf("fillpct = ");
    scanf("%d", &fillpct);
    printf("maxtyp  = ");
    scanf("%d", &maxtyp);
  }

  trace = fopen("contload.out", "a");
  fprintf(trace,"\nCONTAINER LOADING PROBLEM %2d-%2d %2d %2d\n",
          mindim, maxdim, fillpct, maxtyp);

  sumtime = sumfill = sumn = summiss = 0; 
  for (v = 1; v <= TESTS; v++) {
    printf("TEST %d\n", v);
    srand(v);     /* initialize random generator */
    f = &tab[0]; l = &tab[MAXITEMS-1];
    maketest(f, &l, &W, &H, &D, mindim, maxdim, fillpct, maxtyp);
    prepareitems(f, l, w, h, d); 
    n = (l - f + 1); cvol = W * (long) H * D;

    /* now do the packing */
    timeused(NULL);
    contload(n, W, H, D, w, h, d, x, y, z, k, &vol);
    timeused(&time);

    updateitems(f, l, w, h, d, x, y, z, k, &miss); 
    /* printinstance(f, l, W, H, D); */
    checksol(f, l, W, H, D, vol);
    sprintf(s, "%2d : n %3d fill %4.1f miss %d time %6.2f", 
            v, n, 100 * (double) vol / cvol, miss, time);
    fprintf(trace,"%s\n", s); printf("%s\n", s); fflush(trace);
    sumtime += time;
    sumfill += vol / (double) cvol;
    sumn    += n;
    summiss += miss;
  }
 
  fprintf(trace, "mindim  = %d\n", mindim);
  fprintf(trace, "maxdim  = %d\n", maxdim);
  fprintf(trace, "fillpct = %d\n", fillpct);
  fprintf(trace, "maxtyp  = %d\n", maxtyp);
  fprintf(trace, "n       = %.2f\n", sumn    / TESTS);
  fprintf(trace, "fill    = %.1f\n", 100 * sumfill / TESTS);
  fprintf(trace, "miss    = %.1f\n", summiss / TESTS);
  fprintf(trace, "time    = %.2f\n", sumtime / TESTS);
  fclose(trace);
  return 0; /* correct termination */
}



