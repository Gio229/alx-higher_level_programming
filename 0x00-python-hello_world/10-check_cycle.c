#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer to head of list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *current;
	listint_t *temp;
	listint_t *currentTemp;
	int addressVal;

	temp = NULL;
	current = list;


	while (current != NULL)
	{
		addressVal = (long int) current;
		add_nodeint(&temp, addressVal);
		current = current->next;
		currentTemp = temp;
		addressVal = (long int) current;

		while (currentTemp != NULL)
		{

			if (currentTemp->n == addressVal)
			{
				free_listint(temp);
				return (1);
			}
			currentTemp = currentTemp->next;
		}
	}
	free_listint(temp);

	return (0);
}
