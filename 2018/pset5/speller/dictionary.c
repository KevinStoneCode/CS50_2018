// Implements a dictionary's functionality
#include <ctype.h>
#include <stdio.h>
#include <stdbool.h>
#include <string.h>
#include <stdlib.h>
#include "dictionary.h"

// Returns true if word is in dictionary else false
bool check(const char *word)
{
    // TODO
    node *curr = root;
    for (int i = 0, n = strlen(word); i < n; i++)
    {
        int index = (word[i] == '\'') ? 26 : tolower(word[i]) - 97;
        if (!curr->children[index]) {
            return false;
        }
        curr = curr->children[index];
    }
    return curr->is_word;
}

// Loads dictionary into memory, returning true if successful else false
bool load(const char *dictionary)
{
    // open input file
    FILE *inptr = fopen(dictionary, "r");
    if (inptr == NULL)
    {
        fprintf(stderr, "Could not open %s.\n", dictionary);
        return false;
    }
    // TODO
    root = malloc(sizeof(node));
    memset(root, 0, sizeof(node));
    node *curr, *newnode;
    char *word = malloc(sizeof(char) * LENGTH + 1);
    while (fscanf(inptr, "%s", word) != EOF)
    {
        dic_size++;
        curr = root;
        for (int i = 0, n = strlen(word); i < n; i++)
        {
            int index = (word[i] == '\'') ? 26 : word[i] - 97;
            if (!curr->children[index]) {
                newnode = malloc(sizeof(node));
                memset(newnode, 0, sizeof(node));
                curr->children[index] = newnode;
            }
            curr = curr->children[index];
        }
        curr->is_word = true;
    }
    free(word);
    fclose(inptr);
    return true;
}

// Returns number of words in dictionary if loaded else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    return dic_size;
}

// Unloads dictionary from memory, returning true if successful else false
bool unload(void)
{
    // TODO
    myfree(root);
    return true;
}

void myfree(node *rt)
{
	for (int i = 0; i < TRIE_WIDTH; i++){
		if(rt->children[i] != NULL){
			myfree(rt->children[i]);
			rt->children[i] = NULL;
		}
	}
	free(rt);
	return;
}