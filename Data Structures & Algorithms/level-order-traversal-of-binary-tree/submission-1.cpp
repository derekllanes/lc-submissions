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
    vector<vector<int>> levelOrder(TreeNode* root) {
        if(root == nullptr){
            return {};
        }

        vector<vector<int>> res;
        queue<TreeNode*> bfs;
        bfs.push(root);
        
        while(!empty(bfs)){
            int level = bfs.size();
            vector<int> track;

            for(int i = 0; i < level; ++i){
                TreeNode* node = bfs.front();
                bfs.pop();
                track.push_back(node->val);

                if(node->left != nullptr){
                    bfs.push(node->left);
                }
                if(node->right != nullptr){
                    bfs.push(node->right);
                }
            }

            res.push_back(track);
        }
        
        return res;
    }
};
