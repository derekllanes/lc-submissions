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

    int res;

    int checkLength(TreeNode* root){
        // Base case return 0
        if(root == nullptr){
                return 0;
        }
        // check left
        int left = this->checkLength(root->left);
        // check right
        int right = this->checkLength(root->right);
        // label each node with max number of edges
        this->res = max(res, left + right);
        // send up running count of edges
        return 1+max(left,right);
    }

    int diameterOfBinaryTree(TreeNode* root) {
        int length = this->checkLength(root);
        return this->res;
    }
};
