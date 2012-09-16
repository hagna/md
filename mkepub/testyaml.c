#include <stdio.h>
#include <yaml.h>

int main(void) 
{
	FILE *fh = fopen("test.yaml", "r");
	yaml_parser_t parser;
	yaml_token_t token;

	if (!yaml_parser_initialize(&parser))
		fputs("Failed to initialize parser!\n", stderr);
	if (fh == NULL)
		fputs("Failed to open file!\n", stderr);
	
	yaml_parser_set_input_file(&parser, fh);


	do {
		yaml_parser_scan(&parser, &token);
		switch (token.type)
		{
			case YAML_STREAM_START_TOKEN: puts("STREAM START");
				break;
			case YAML_STREAM_END_TOKEN: puts("STREAM END");
				break;
			case YAML_KEY_TOKEN: printf("(Key token)    "); 
				break;
			case YAML_VALUE_TOKEN: printf("(Value token)    ");
				break;
			case YAML_BLOCK_SEQUENCE_START_TOKEN:
				puts("<b|Start Block (Sequence>"); break;
			case YAML_BLOCK_ENTRY_TOKEN: 
				puts("<b|Start Block (Entry)>"); break;
			case YAML_BLOCK_END_TOKEN: 
				puts("<b|End block>");
			case YAML_BLOCK_MAPPING_START_TOKEN:
				puts("[Block mapping]");
				break;
			case YAML_SCALAR_TOKEN:
				printf("scalar %s\n", token.data.scalar.value);
				break;
			default:
				printf("Got token of typed %d\n", token.type);
		}
		if (token.type != YAML_STREAM_END_TOKEN)
			yaml_token_delete(&token);
	} while (token.type != YAML_STREAM_END_TOKEN);
	yaml_token_delete(&token);

	
	yaml_parser_delete(&parser);

	fclose(fh);
	return 0;
}
