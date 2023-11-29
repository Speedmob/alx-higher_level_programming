#include <stdlib.h>
#include "lists.h"
/**
 * insert_node - inserts a node in a sorted LL
 * @head: start of LL
 * @number: num to add
 *
 * Return: address of LL or NULL
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *p, *c = *head;

	p = malloc(sizeof(listint_t));
	if (!p)
		return (NULL);
	p->n = number;
	if (c == NULL || c->n >= number)
	{
		p->next = *head;
		*head = p; }
	else
	{
		while (c->next && c->next->n < number)
			c = c->next;
		p->next = c->next;
		c->next = p; }
	return (p);
}
