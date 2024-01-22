#include "lists.h"
int list_len(listint_t **list);

/**
 * is_palindrome - Checks if a singly linked list is a palindrome or not
 * @head: Points to the pointer of the head node of singly linked list
 *
 * Return: 0 if not palindrome. 1 otherwise
 */
int is_palindrome(listint_t **head)
{
    listint_t *temp;
    listint_t *locate;
    int len, i = 0, j, pali = 1;

    if (!*head)
	return (pali);
    len = list_len(head);
    temp = *head;
    for (; i < len / 2; i++)
    {
	locate = temp;
	for (j = i; j < len - (i + 1); j++)
	{
	    locate = locate->next;
	}
	if (temp->n != locate->n)
	{
	    pali = 0;
	    break;
	}
	temp = temp->next;
    }
    return (pali);
}
/**
 * list_len - Determines the number of items in a listint_t list
 * @list: Points to the pointer of the heade node of singly linked list
 *
 * Return: The number of items in a list
 */
int list_len(listint_t **list)
{
    int len = 0;
    listint_t *iterate = *list;

    while (iterate)
    {
	len += 1;
	iterate = iterate->next;
    }
    return (len);
}
