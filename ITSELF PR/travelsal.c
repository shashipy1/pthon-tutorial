
#include<stdio.h>
#include<stdlib.h>
struct Node{
    int data;
    struct Node *next;
};   
void linkedListTraversal(struct Node *ptr)
{
    while(ptr!=NULL){
    printf("Element %d\n",ptr->data);
    ptr=ptr->next;
    }
}
int main(){
    struct Node *head;
    struct Node *second;
    struct Node *third;
    struct Node *forth;
    struct Node *fifth;
    struct Node *sixth;
    struct Node *seventh;
    struct Node *eighth ;
    head = (struct Node*)malloc(sizeof(struct Node));
    second = (struct Node*)malloc(sizeof(struct Node));
    third = (struct Node*)malloc(sizeof(struct Node));
    forth = (struct Node*)malloc(sizeof(struct Node));
    fifth = (struct Node*)malloc(sizeof(struct Node));
    sixth = (struct Node*)malloc(sizeof(struct Node));
    seventh = (struct Node*)malloc(sizeof(struct Node));
    eighth = (struct Node*)malloc(sizeof(struct Node));
    
    head->data=34;
    head->next=second;
    
    second->data=55;
    second->next=third;
    
    third->data=87;
    third->next=forth;
    
    forth->data=48;
    forth->next=fifth;
    
    fifth->data=4;
    fifth->next=sixth;
    
    sixth->data=7;
    sixth->next=seventh;
    
    seventh->data=68;
    seventh->next=eighth;
    
    eighth->data=6;
    eighth->next=NULL;
     
    linkedListTraversal(head);
    return 0;
    
}