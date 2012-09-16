#include <stdio.h>
#include <yaml.h>

int main(void) 
{
	FILE *fh = fopen("config/public.yaml", "r");
	yaml_parser_t parser;
	yaml_token_t token;

	if (!yaml_parser_initialize(&parser))
		fputs("Failed to initialize parser!\n", stderr);
	if (fh == NULL)
		fputs("Failed to open file!\n", stderr);
	
	yaml_parser_set_input_file(&parser, fh);

	yaml_parser_delete(&parser);
	fclose(fh);
	return 0;
}
