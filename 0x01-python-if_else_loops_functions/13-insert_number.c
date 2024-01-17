#include "lists.h"
/**
 * insert_node - Insert a new node into listint_t list
 * @head: Pointer to the pointer of the first node of listint_t list
 * @number: Integer to be inserted
 *
 * Return: The address of the new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *temp;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (new);
	if (!*head)
	{
		new->n = number;
		new->next = NULL;
		*head = new;
		return (new);
	}
	temp = *head;
	new->next = *head;
	while (temp->next != NULL)
	{
		if (temp->next->n < number)
			temp = temp->next;
		else
			break;
	}
	if (new->next == temp)
	{
		new->n = number;
		*head = new;
		return (new);
	}
	new->n = number;
	new->next = temp->next;
	temp->next = new;
	return (new);
}
