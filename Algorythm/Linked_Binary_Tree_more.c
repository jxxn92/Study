#include <stdio.h>
#include <stdlib.h>
#include <memory.h>

typedef struct TreeNode {
    int data;
    struct TreeNode *left,*right;
} TreeNode;

        

TreeNode n1 = {1, NULL, NULL};
TreeNode n2 = {4, &n1, NULL};
TreeNode n3 = {16, NULL, NULL};
TreeNode n4 = {25, NULL, NULL};
TreeNode n5 = {20, &n3, &n4};
TreeNode n6 = {15, &n2, &n5};
TreeNode *root = &n6;

// inorder 중위순회(LVR)
void inorder(TreeNode* root){
    if(root != NULL){
        inorder(root->left);
        printf("[%d] ",root->data);
        inorder(root->right);
    }
}

// preorder 전위순회(VLR)
void preorder(TreeNode *root){
    if(root != NULL){
        printf("[%d] ",root->data);
        preorder(root->left);
        preorder(root->right);
    }
}

// postorder 후위순회(LRV)
void postorder(TreeNode *root){
    if (root != NULL){
        postorder(root->left);
        postorder( root->right);
        printf("[%d] ",root->data);
    }
}

int get_node_count(TreeNode *root){
    int count = 0;

    if (root != NULL)
        count = 1 + get_node_count(root->left) + get_node_count(root->right);

    return count;
}

// TreeNode *search(TreeNode *root, int key){
//     if (root == NULL) return NULL;
//     if (root->data == key) return root;
//     else if (root->data > key){
//         return search(root->left, key);
//     } else {
//         return search(root->right, key);
//     }
// }

TreeNode *search(TreeNode *root, int key){

    while (root != NULL){
        if (root->data == key){
            return root;
        } else if (root->data > key) {
            root = root->left;
        } else {
            root = root->right;
        }
    }
    return NULL;
}

TreeNode *insert_node(TreeNode *root, int data){
    if (root == NULL){
        return new_node(data);
    }
    if (root->data > data){
        root->left = insert_node(root->left, data);
    } else if (root->data < data) {
        root->right = insert_node(root->right, data);
    }
    
    return root;

}

TreeNode *new_node(int key){
    TreeNode *tmp = (TreeNode *)malloc(sizeof(TreeNode));
    tmp->data = key;
    tmp->left = tmp->right = NULL;
    return tmp;
}

/**
 * 삭제 연산의 경우 3가지 존재가 존재한다.
 * 1. 삭제하는 노드가 단말 노드일 경우 (LV. 1) 이런 경우 그냥 부모 노드를 찾아 링크를 끊어 주면 된다.
 * 2. 삭제하는 노드가 하나의 서브트리만 가지고 있는 경우 (LV. 2) 이 경우에는 임시 노드를 만들어 삭제한 링크에 있는 서브트리를 부모 노드의 링크에 연결 시켜 줘야 한다.
 * 3. 삭제하는 노드가 두개의 서브트리를 모두 가지고 있는 경우 (LV. 3) 이 경우에는 위의 2번의 경우를 왼쪽 오른쪽 두번 하면 되는거 아닌가 생각해본다.
 * 3번의 경우 왼쪽 서브트리에서 가장 큰 값 또는 오른쪽 서브트리에서 가장작은 값을 사용하여 노드를 이어줘야한다...?
*/



int main(void){


    printf("%d",search(root,20));

    return 0;
}