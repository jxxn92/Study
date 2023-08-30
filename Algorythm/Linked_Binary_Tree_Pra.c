#include <stdio.h>
#include <stdlib.h>
#include <memory.h>

typedef struct TreeNode
{
    int data;
    struct TreeNode *left, *right;
} TreeNode;

int main(void){
    
    TreeNode *n1, *n2, *n3, *n4;

    n1 = (TreeNode *)malloc(sizeof(TreeNode));
    n2 = (TreeNode *)malloc(sizeof(TreeNode));
    n3 = (TreeNode *)malloc(sizeof(TreeNode));
    n4 = (TreeNode *)malloc(sizeof(TreeNode));

    n1->data = 10;
    n1->left = NULL;
    n1->right = n2;

    n2->data = 20;
    n2->left = NULL;
    n2->right = n3;
    
    n3->data = 30;
    n3->left = n4;
    n3->right = NULL;

    n4->data = 25;
    n4->left = NULL;
    n4->right = NULL;

    free(n1);
    free(n2);
    free(n3);
    free(n4);

    return 0;
}