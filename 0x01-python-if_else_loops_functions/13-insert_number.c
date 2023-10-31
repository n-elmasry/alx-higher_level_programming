#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly linked list.
 * @head: Pointer to the head of the list.
 * @number: Number to insert.
 * Return: A pointer to the new node or NULL if it fails.
 */
listint_t *insert_node(listint_t **head, int number)
{
listint_t *new_node, *current, *prev;

if (head == NULL)
return (NULL);

new_node = malloc(sizeof(listint_t));
if (new_node == NULL)
return (NULL);

new_node->n = number;
new_node->next = NULL;

if (*head == NULL || number < (*head)->n)
{
new_node->next = *head;
*head = new_node;
return (new_node);
}

current = *head;
prev = NULL;

while (current != NULL && current->n < number)
{
prev = current;
current = current->next;
}
prev->next = new_node;
new_node->next = current;

return (new_node);
}
