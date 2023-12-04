#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * reverse_listint - reverses a string
 * @head: head of LL
 *
 * Return: LL but reversed
*/
listint_t *reverse_listint(listint_t **head)
{
	listint_t *a, *b;

	if (!head || !*head)
		return (NULL);
	if (!(*head)->next)
		return (*head);
	a = (*head)->next;
	b = a->next;
	(*head)->next = NULL;
	while (a)
	{
		a->next = *head;
		*head = a;
		a = b;
		b = b ? b->next : NULL;
	}
	return (*head);
}
/**
 * is_palindrome - checks if LL is palendrome
 * @head: LL to check
 *
 * Return: 0 (Not), 1 (is)
*/
int is_palindrome(listint_t **head)
{
	listint_t *middle = NULL, *full = *head, *half = *head, *point = *head;

	if (!*head || !(*head)->next)
		return (1);
	while (!middle)
	{
		full = full->next->next;
		if (!full)
		{
			middle = half->next;
			continue; }
		else if (!full->next)
		{
			middle = half->next->next;
			continue; }
		half = half->next; }
	reverse_listint(&middle);
	while (middle && point)
	{
		if (point->n != middle->n)
			return (0);
		middle = middle->next;
		point = point->next; }
	if (middle)
		return (0);
	return (1); }
