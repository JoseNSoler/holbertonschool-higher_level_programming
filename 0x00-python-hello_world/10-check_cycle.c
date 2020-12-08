#include "lists.h"

/**
 * check_cycle - check for a existing cycle in a list
 * @list: pointer to head of list
 * Return: 0 on success -- 1 on error
 */

int check_cycle(listint_t *list)
{
	listint_t *header = list;

	if (list != NULL)
	{
		while (list && header && header->next)
		{
			list = list->next;
			header = header->next->next;
			if (header == list)
				return (1);
		}

	}
	return (0);
}
