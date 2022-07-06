#include"lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: singly list head
 * @number: number to insert
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current;
	listint_t *prev;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	current = *head;
	prev = current;

	while (current != NULL)
	{
		if (number <= current->n)
		{
			if (prev == current)
			{
				new->next = current;
				*head = new;
				break;

			}
			else
			{
			prev->next = new;
			new->next = current;
			prev = new;
			break;
			}
		}

		prev = current;
		if (prev->next == NULL && number > current->n)
			prev->next = new;

		current = current->next;
	}
	return (new);
}
