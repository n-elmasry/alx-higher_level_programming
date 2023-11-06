#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: pointer to the head of the list
 * Return: 1 if it is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
listint_t *slow_ptr = *head, *fast_ptr = *head, *prev = NULL, *temp;

if (*head == NULL || (*head)->next == NULL)
return (1);

while (fast_ptr && fast_ptr->next)
{
fast_ptr = fast_ptr->next->next;
temp = slow_ptr;
slow_ptr = slow_ptr->next;
}

fast_ptr = *head;
temp->next = NULL;

while (slow_ptr)
{
temp = slow_ptr->next;
slow_ptr->next = prev;
prev = slow_ptr;
slow_ptr = temp;
}

while (prev)
{
if (prev->n != fast_ptr->n)
return (0);
prev = prev->next;
fast_ptr = fast_ptr->next;
}
return (1);
}
