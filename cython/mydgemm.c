
void my_dgemm( int m, int n, int k, 
              double a[m][n], double b[n][k], float c[m][k] )
{
  
  for( int j = 0 ; j < n ; j++ ) {
    for( int i = 0 ; i < k ; i++ ) {
      double ab=0.0;
      for( int l = 0 ; l < n ; l++ ){
        ab += a[j][l] * b[l][i];
      }
      c[j][i] = ab ;
    }
  }
}
