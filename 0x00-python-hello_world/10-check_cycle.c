#include "lists.h"
#include <stdio.h>
/**
 * check_cycle - checks for cycle
 * @list: list to check
 *
 * Return: 1 (Cycle), 0 (No cycle)
*/
int check_cycle(listint_t *list)
{
	listint_t *turt = list;
	listint_t *hare = list;

	if (!list)
		return (0);
	while (turt && hare && hare->next)
	{
		turt = turt->next;
		hare = hare->next->next;
		if (turt == hare)
			return (1);
	}
	return (0);
}
