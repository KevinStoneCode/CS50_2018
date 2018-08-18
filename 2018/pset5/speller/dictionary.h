// Declares a dictionary's functionality

#ifndef DICTIONARY_H
#define DICTIONARY_H

#include <stdbool.h>

// Maximum length for a word
// (e.g., pneumonoultramicroscopicsilicovolcanoconiosis)
#define LENGTH 45
#define TRIE_WIDTH 27
// Prototypes
bool check(const char *word);
bool load(const char *dictionary);
unsigned int size(void);
bool unload(void);
#endif // DICTIONARY_H

typedef struct node
{
    bool is_word;
    struct node *children[TRIE_WIDTH];
}
node;
void myfree(struct node *rt);

node *root;
int dic_size;