#include<stdio.h>
#include<stdlib.h>
struct Node
{
    int data;
    struct Node* next;
};
void linkedListTraversal(struct Node *ptr)
{
    while(ptr!=NULL)
    {
        printf("Element %d\n",ptr->data);
        ptr=ptr->next;
    }
    printf("\n");
}
struct Node* insertionAtFirst(struct Node *head, int data)
{
    struct Node* ptr=(struct Node*)malloc(sizeof(struct Node));
    ptr->data=data;
    ptr->next=head;
    return ptr;
}

struct Node* insertionAtEnd(struct Node *head, int data)
{
    struct Node* ptr=(struct Node*)malloc(sizeof(struct Node));
    ptr->data=data;
    struct Node* p= head;
    while(p->next!=NULL)
    {
        p = p->next;
    }
     p->next = ptr;
     ptr->next = NULL;
     return head;
}
    
struct Node* insertionAtIndex(struct Node *head, int data, int index)
{
    struct Node* ptr=(struct Node*)malloc(sizeof(struct Node));
    struct Node* p= head;
    int i=0;
    while(i!=index-1)
    {
        p = p->next;
        i++;
    }
    // printf("%d",head->data); 
    ptr->data=data;
    ptr->next=p->next;
    p->next=ptr;
    
    return head;
}
int main(){
    struct Node *head;
    struct Node *second;
    struct Node *third;
    head=(struct Node*)malloc(sizeof(struct Node));
    second=(struct Node*)malloc(sizeof(struct Node));
    third=(struct Node*)malloc(sizeof(struct Node));
    
    head->data=32;
    head->next=second;
    
    second->data=35;
    second->next=third;
    
    third->data=43;
    third->next=NULL;
    
    printf("linked List before insertion\n");
    linkedListTraversal(head);
    head = insertionAtEnd(head,44);
    printf("linked List after insertion\n");
    linkedListTraversal(head);
    return 0;
}