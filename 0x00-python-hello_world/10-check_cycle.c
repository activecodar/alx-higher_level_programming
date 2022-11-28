#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has
 * a cycle in it
 * @list: pointer to the list
 * Return: 0 if there is no cycle,
 * 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *a;
	listint_t *b;

	a = list;
	b = list;
	while (list && a && a->next)
	{
		list = list->next;
		a = a->next->next;

		if (list == a)
		{
			list = b;
			b =  a;
			while (1)
			{
				a = b;
				while (a->next != list && a->next != b)
				{
					a = a->next;
				}
				if (a->next == list)
					break;

				list = list->next;
			}
			return (1);
		}
	}

	return (0);
}
