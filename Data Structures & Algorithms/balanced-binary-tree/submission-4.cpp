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
    int checkHeight(TreeNode* root){
        // Base Case
        if(root == nullptr){
            return 0;
        }
        // check each subtree
        int left = this->checkHeight(root->left);
        if(left == -1){
            return -1;
        }
        
        int right = this->checkHeight(root->right);
        if(right == -1){
            return -1;
        }

        // if height differ by 1 for each node
        if(abs(left - right) > 1){
            // return false
            return -1;
        }

        return max(left, right)+1;
    }

    bool isBalanced(TreeNode* root) {
        return this->checkHeight(root) != -1;
    }
};
