class Solution {
public:
    ListNode* reverse(ListNode* head) {
        ListNode* prev = nullptr;
        ListNode* curr = head;
        ListNode* next = head;
        while (curr){
            next = curr->next;
            curr->next = prev;
            prev = curr;
            curr = next;
        }
        return prev;
    }
    bool isPalindrome(ListNode* head) {
        ListNode* slow = head;
        ListNode* fast = head ;
        while (fast->next&&fast->next->next){
            slow = slow->next;
            fast = fast->next->next;
        }
        ListNode* c = reverse(slow->next);
        ListNode* a = head;
        ListNode* b = c;
        while (b){
            if (a->val!=b->val) return false;
            a = a->next;
            b = b->next;
        }
        return true;
    }
};