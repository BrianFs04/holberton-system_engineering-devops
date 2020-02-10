#include <sys/types.h>
#include <sys/wait.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * infinite_while - Infinite loop
 * Return: 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
/**
 * main - Creates 5 zombie processes
 * Return: Always 0
 */
int main(void)
{
	int i = 0;

	while (i < 5)
	{
		if (fork())
			dprintf(1, "Zombie process created, PID: %d\n",
				getpid());
		else
			exit(0);
		i++;
	}
	infinite_while();
	return (0);
}
