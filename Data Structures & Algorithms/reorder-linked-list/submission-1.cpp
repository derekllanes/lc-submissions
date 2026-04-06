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
    void reorderList(ListNode* head) {
        // find half
        ListNode* s = head;
        ListNode* f = head->next;

        while(f && f->next != nullptr){
            s = s->next;
            f = f->next->next;
        }
        ListNode* r = s->next;
        s->next = nullptr;
        ListNode* prev = nullptr;

        // reverse second half
        while(r != nullptr){
            ListNode* nxt = r->next;
            r->next = prev;
            prev = r;
            r = nxt;
        }

        // merge
        r = prev;
        ListNode* l = head;

        while(r != nullptr){
            ListNode* nxtL = l->next;
            ListNode* nxtR = r->next;
            l->next = r;
            r->next = nxtL;
            l = nxtL;
            r = nxtR;
        }
    }
};
