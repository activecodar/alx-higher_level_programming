#include "lists.h"

/**
* insert_node - inserts a new node at a given position.
* @head: head of a list.
* @number: index of the list where the new node is added.
* Return: the address of the new node, or NULL if it
* failed.
*/

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *n_node, *curr_head, *prev_head;

	curr_head = *head;
	n_node = malloc(sizeof(listint_t));

	if (n_node == NULL)
	{
		return (NULL);
	}

	while (curr_head != NULL)
	{
		if (curr_head->n > number)
		{
			break;
		}
		prev_head = curr_head;
		curr_head = curr_head->next;
	}
	n_node->n = number;
	if (*head == NULL)
	{
		n_node->next = NULL;
		*head = n_node;
	}
	else
	{
		n_node->next = curr_head;
		if (curr_head == *head)
		{
			*head = n_node;
		}
		else
		{
			prev_head->next = n_node;
		}
	}

	return (n_node);
}
