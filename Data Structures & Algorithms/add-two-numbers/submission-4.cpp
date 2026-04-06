/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* a = l1;
        ListNode* b = l2;
        ListNode* res = new ListNode();
        ListNode* head = res;
        int carry = 0;
        int aVal = 0;
        int bVal = 0;
        int total = 0;

        while(a != nullptr || b != nullptr){
            if(a != nullptr){
                aVal = a->val;
            }else{
                aVal = 0;
            }
            if(b != nullptr){
                bVal = b->val;
            }else{
                bVal = 0;
            }

            total = aVal + bVal + carry;

            ListNode* curr = new ListNode(total % 10);

            carry = total / 10;

            res->next = curr;
            res = res->next;

            if(a != nullptr){
                a = a->next;
            }
            if(b != nullptr){
                b = b->next;
            }

        }

        if(carry > 0){
            ListNode* curr = new ListNode(1);
            res->next = curr;
        }

        return head->next;
    }
};
