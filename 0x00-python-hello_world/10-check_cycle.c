#include "lists.h"
/**
 * check_cycle - Check if a singly linked list has a cycle or not
 * @list: Points to the linked listint_s
 *
 * Return: 0 if no cycle. 1 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *temp = list;
	listint_t *search = list;

	while (temp && search && search->next)
	{
		temp = temp->next;
		search = search->next->next;
		if (temp == search)
			return (1);
	}
	return (0);
}
