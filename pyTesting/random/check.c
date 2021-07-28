#include <stdio.h>
#include <stdlib.h>
#define ROW 5
#define COL 4
void right_ani(){
	int c,r;
	char pixel='#';
	for(r=0;r<ROW;r++){
		for(c=0;c<COL;c++){
			//For Blue
			if((r==1 && c==1) ||
					 (r==1 && c==2) ||
					 (r==1 && c==3) ||
					 (r==2 && c==1) ||
					 (r==2 && c==2) ||
					 (r==2 && c==3)
					 ){printf("\033[0;34m");printf("%c",pixel);
			//For Red
			}else if((r==3 && c==1) ||
					 (r==3 && c==3)
					){printf("\033[0;31m");printf("%c",pixel);
			//For Brown
			}else if((r==0 && c==2) ||
					 (r==4 && c==1) ||
					 (r==3 && c==2)
					){printf("\033[0;37m");printf("%c",pixel);
			//For Background
			}else{
				printf("\033[0;37m");printf(" ");
			}
		}
		printf("\n");
	}
}
void left_ani(){
	int c,r;
	char pixel='#';
	for(r=0;r<ROW;r++){
		for(c=0;c<COL;c++){
			//For Blue
			if((r==1 && c==1) ||
					 (r==1 && c==2) ||
					 (r==1 && c==3) ||
					 (r==2 && c==1) ||
					 (r==2 && c==2) ||
					 (r==2 && c==3)
					 ){printf("\033[0;34m");printf("%c",pixel);
			//For Red
			}else if((r==3 && c==1) ||
					 (r==3 && c==3)
					){printf("\033[0;31m");printf("%c",pixel);
			//For Brown
			}else if((r==0 && c==2) ||
					 (r==3 && c==0) ||
					 (r==4 && c==3)
					){printf("\033[0;37m");printf("%c",pixel);
			//For Background
			}else{
				printf("\033[0;37m");printf(" ");
			}
		}
		printf("\n");
	}
}
void delay(){
	int c,d;
	for (c = 1; c <= 4000; c++)
       for (d = 1; d <= 32767; d++)
       {}
   	printf("\e[1;1H\e[2J");
}

int main(int argc, char const *argv[])
{	
	for(int i=0;i<5;i++){
		right_ani();
		delay();
		left_ani();
		delay();
	}
	return 0;
}