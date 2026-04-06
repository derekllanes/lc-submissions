/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:

    bool res;

    int checkDepth(TreeNode* root){
        if(root == nullptr){
            return 0;
        }

        int left = this->checkDepth(root->left);
        int right = this->checkDepth(root->right);

        if(abs(left - right) > 1){
            this->res = false;
        }

        return max(left, right)+1;
    }

    
    bool isBalanced(TreeNode* root) {
        res = true;
        int count = this->checkDepth(root);
        return res;
    }
};
