#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "lists.h"
/**
*check_cycle - checks if a singly linked list has a cycle in it.
*@list: list
* Return:  if there is no cycle, 1 if there is a cycle
*/

int check_cycle(listint_t *list)
{
listint_t *i = list, *j = list;


while (j != NULL && j->next != NULL)
{
i = i->next;
j = j->next->next;
    
if(i == j)
{

return (1);
}

}
return (0);
}

