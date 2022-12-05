#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: singly linked list node structure
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t **stack = malloc(sizeof(listint_t *));

	if (*head == NULL || (*head)->next == NULL)
	{
		return (1);
	}

	int stack_size = 0;

	while (fast != NULL && fast->next != NULL)
	{
		stack[stack_size++] = slow;
		slow = slow->next;
		fast = fast->next->next;
	}

	if (fast != NULL)
	{
		slow = slow->next;
	}

	while (stack_size > 0 && slow != NULL)
	{
		if (stack[--stack_size]->n != slow->n)
		{
			return (0);
		}
		slow = slow->next;
	}

	return (1);
}

