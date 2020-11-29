#include<stdio.h>
int main()
{
 int i,j,n,temp,temp_i,temp_j,cl,mcl=0;

 printf("Enter values of i & j:\n");
 scanf("%d%d",&i,&j);

temp_i=i;                    // Storing the values of i & j in temporary variable 
temp_j=j;                         
                  
// Swapping the values if First number is greater than Second number 
if(i>j)                       
{
 temp=i;
      i=j;
    j=temp;
}

// Iterating the loop for all the values of i to j
while(i<=j)
{
  n=i;          // Storing the values of i in n for calculating the sequence
  cl=1;        // As n gets any value other than 0 cycle length starts from 1

// Terminating Condition 
while(n!=1)
{
  if(n%2==0)                // Checking if n is Even,divide it by 2 
    n=n/2;                           
  else                            
   n=3*n+1;                  //If found odd , Multiply it by 3 and add 1 to it                                            
                    
cl++;                             //Increment the cycle length 
}

// If cycle length of n is found greater than maximum cycle length
if(cl>mcl)
mcl=cl;
i++;
}
printf("%d\t%d\t%d",temp_i,temp_j,mcl);
return 0;
}
