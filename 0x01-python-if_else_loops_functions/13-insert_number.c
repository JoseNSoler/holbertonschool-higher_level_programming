#include "lists.h"


/**
 * insert_node - Add a new node in a linked list
 * @head: Head of the given list
 * @number: Data number for node
 * Return: Address at the new node -- NULL on fail
 */


listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp, *node;

	if (head == NULL)
		return (NULL);

	node = malloc(sizeof(listint_t));
	if (node == NULL)
		return (NULL);

	node->n = number;
	node->next = NULL;

	if (*head == NULL)
	{
		*head = node;
		return (node);
	}

	temp = *head;

	while (temp->next)
	{
		if (number >= temp->n && number < temp->next->n)
		{
			node->next = temp->next;
			temp->next = node;
			return (node);
		}
		temp = temp->next;
	}
	if (number >= temp->n)
		temp->next = node;
	else
	{
		node->next = *head;
		*head = node;
	}

	return (node);
}
