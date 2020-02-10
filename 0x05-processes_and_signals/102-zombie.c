#include <sys/types.h>
#include <sys/wait.h>
#include <stdio.h>
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
		dprintf(1, "Zombie process created, PID: %d\n", getpid());
		i++;
		return (0);
	}
	infinite_while();
	return (0);
}
