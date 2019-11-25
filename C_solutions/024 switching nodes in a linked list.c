/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* swapPairs(struct ListNode* head){
    int index = 0;
    struct ListNode* tmp = head , * ret = head , *one = NULL , *two = NULL , *three = NULL , *four = NULL , *father = NULL , *grandpa = NULL , *tail = NULL;
    if(head == NULL){
        return NULL;
    }
    if(tmp->next == NULL){
        return ret;
    }
    ret = head->next;
    while(tmp != NULL && tmp->next != NULL && tmp->next->next != NULL && tmp->next->next->next != NULL){
        one = tmp;
        two = one->next;
        three = two->next;
        four = three->next;
        tmp = four->next;
        tail = four->next;
        two->next = one;
        one->next = four;
        four->next = three;
        grandpa = four;
        father = three;
        if(tail == NULL){
            three->next = NULL;
        }else if(tail->next != NULL){
            three->next = tail->next;
        }else{
            three->next = tail;
        }
    }
    if(tmp != NULL){
        if(tmp->next != NULL){
            if(three != NULL && tail != NULL && tmp != NULL){
                three->next = tmp->next;
                tail = three->next->next;
                three->next->next = tmp;
                tmp->next = tail;
            }else{
                ret = head->next;
                tmp = head->next->next;
                head->next->next = head;
                head->next = tmp;
            }
        }
    }
    return ret;
}
