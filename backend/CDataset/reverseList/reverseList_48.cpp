class Solution {
public:
    class ListNode{
        public:
        ListNode* next;
        int val;
    };

    ListNode* reverseList(ListNode* head) {
        if(head == nullptr || head->next == nullptr){
            return head;
        }
        ListNode* prev = reverseList(head->next);
        head->next->next = head;
        head->next = nullptr;
        return prev;
    }
};
