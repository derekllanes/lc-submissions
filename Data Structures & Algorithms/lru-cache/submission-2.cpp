class Node{
public:
    int key;
    int val;
    Node* prev;
    Node* nxt;

    Node(int k, int v) : key(k), val(v), prev(nullptr), nxt(nullptr){}
};

class LRUCache {
private:
    int cap;
    unordered_map<int, Node*> cache;
    Node* left;
    Node* right;

    void remove(Node* node){
        Node* prev = node->prev;
        Node* next = node->nxt;

        prev->nxt = next;
        next->prev = prev;
    };

    void insert(Node* node){
        Node* prev = right->prev;

        prev->nxt = node;
        node->prev = prev;

        right->prev = node;
        node->nxt = right;
    };

public:
    LRUCache(int capacity): cap(capacity), left(new Node(0, 0)), right(new Node(0, 0)){
        left->nxt = right;
        right->prev = left;
    } 
    
    int get(int key) {
        if(cache.find(key) != cache.end()){
            remove(cache[key]);
            insert(cache[key]);
            return(cache[key]->val);
        }else{
            return -1;
        }
    }
    
    void put(int key, int value) {
        if(cache.find(key) != cache.end()){
            cache[key]->val = value;
            remove(cache[key]);
            insert(cache[key]);
        }else{
            if(cache.size() >= cap){
                Node* lru = left->nxt;
                remove(lru);
                cache.erase(lru->key);
                cache[key] = new Node(key, value);
                insert(cache[key]);
                delete lru;
            }else{
                cache[key] = new Node(key, value);
                insert(cache[key]);
            }
        }
    }
};
