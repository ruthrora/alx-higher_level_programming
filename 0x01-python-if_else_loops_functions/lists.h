#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>
/*
 * struct listint_s - singly linked lists
 * @n: integer
 * @next: next node
 */
typedef struct listint_s
{
	int n;
	struct listint_s *next
} listint_t;

def print_last_digit(number);
def add(a, b);
def pow(a, b);
listint_t *insert_node(listint_t **head, int number);
def remove_char_at(str, n);
def magic_calculation(a, b, c);

#endif /* LISTS_H */
