#include <stdio.h>
#include <string.h>
int main()
{
   char str[100], i=0;
   int str_len;
 

   scanf("%s",str);

 
   while(1)
   {
      str_len = strlen(str) - (i+1);
 
      if (str[i] == str[str_len])
      {
         if (i == str_len || i+1 == str_len)
         {
            printf("The word \%s\ is a palindrome.", str);
            break;
         }
         i = i+1;
      }
      else
      {
         printf("\nEntered word \"%s\" is not a palindrome", str);
         break;
      }
   }
   return 0;
}
