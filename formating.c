#include <stdio.h>
#include <string.h>
#include <fcntl.h>
#include <unistd.h>
#include <stdlib.h>
int main()
{
	FILE *fd = fopen("data", "r");
	FILE *fd2 = fopen("data2", "w+");
	char *line;
	size_t n = 0;
	ssize_t readed;
	while ((readed = getline(&line, &n,fd)) != -1)
	{
		line[readed - 1] = ',';
		fwrite(line, sizeof(char), readed, fd2);
		fwrite(" ", sizeof(char), 1, fd2);
	}
	free(line);
	fclose(fd);
	fclose(fd2);
}
