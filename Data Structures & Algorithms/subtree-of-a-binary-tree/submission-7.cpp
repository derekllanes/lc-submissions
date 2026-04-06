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
    bool match(TreeNode* root, TreeNode* subRoot){
        if(root == nullptr && subRoot == nullptr){
            return true;
        }
        if(root == nullptr || subRoot == nullptr){
            return false;
        }
        if(root->val != subRoot->val){
            return false;
        }

        bool left = this->match(root->left, subRoot->left);
        bool right = this->match(root->right, subRoot->right);

        if(left == false || right == false){
            return false;
        }else{
            return true;
        }
    }


    bool isSubtree(TreeNode* root, TreeNode* subRoot) {
        // Find the subRoot in root
        // if found then check if subtree are the same
        // if !subtree then continue checking for other instances of subRoot in root
        // if searched all subtrees and subRoot in root return false

        if(root == nullptr){
            return false;
        }

        if(root->val == subRoot->val){
            bool isFound = this->match(root, subRoot);
            if(isFound == true){
                return true;
            }
        }

        bool left = this->isSubtree(root->left, subRoot);
        bool right = this->isSubtree(root->right, subRoot);

        if(left == true || right == true){
            return true;
        }else{
            return false;
        }
    }
};
