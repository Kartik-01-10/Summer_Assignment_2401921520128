class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode* c = new ListNode(10);  
        ListNode* t = c;
        ListNode* a = list1;
        ListNode* b = list2;

        while (a != NULL && b != NULL) {
            if (a->val <= b->val) {
                t->next = a;
                a = a->next;
            } else {
                t->next = b;
                b = b->next;
            }
            t = t->next;
        }

        // Attach the remaining part
        if (a == NULL) {
            t->next = b;
        } else {
            t->next = a;
        }

        return c->next;
    }
};