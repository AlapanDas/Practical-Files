#include <stdio.h>
#include <stdlib.h>

struct node {
  int key;
  struct node* left;
  struct node* right;
};

struct node *create(int item) {
  struct node *newnode = (struct node *)malloc(sizeof(struct node));
  newnode->key = item;
  newnode->left = newnode->right = NULL;
  return newnode;
}

void inorder( struct node* root)
{
    if(root==NULL)
    {
        return;
    }
    inorder(root->left);
    printf("%d->",root->key);
    inorder(root->right);
}
int minvalue(struct node*root)
{
    int min=root->key;
    while(root->left!=NULL)
    {
        min=root->left->key;
        root=root->left;
    }
    return min;
}

struct node *insert(struct node *node, int key) {

  if (node == NULL) 
    return create(key);

  if (key < node->key)
    node->left = insert(node->left, key);
  else
    node->right = insert(node->right, key);

  return node;
}

struct node *delete(struct node *root, int key) {
 
  if (root == NULL) 
    return root;
  if (key < root->key)
    root->left = delete(root->left, key);
  else if (key > root->key)
    root->right = delete(root->right, key);

  else {

    if (root->left == NULL) {
      struct node *temp = root->right;
      free(root);
      return temp;
    } else if (root->right == NULL) {
      struct node *temp = root->left;
      free(root);
      return temp;
    }

    struct node *temp = minvalue(root->right);
    root->key = temp->key;
    root->right = delete(root->right, temp->key);
  }
  return root;
}

int main() {
  struct node *root = NULL;
  int min;
  int value;
  int choice;
  while(1)
  {
        printf("insert\n");
        printf("inorder\n");
        printf("minvalue\n");
        printf("delete\n");
        printf("ENTER THE CHOICE: \n");
        scanf("%d",&choice);
        switch(choice)
        {
        case 1:
          printf("\n Enter the value of the new node :\n ");
          scanf("%d", &value);
          root= insert(root, value);
          break;
        case 2:
          printf("Inorder traversal: ");
          inorder(root);
          printf("\n \n ");
          break;
        case 3:
          min=minvalue(root);
          printf("%d\n",min);
          break;
        case 4:
          printf("\ndeleting \n");
          scanf("%d", &value);
         root=delete(root, value);
          printf("%d is deleted\n",value);
        // case 5:
        //   exit(0);
        //   break;
        default:
        printf("WRONG CHOICE!!!\n");
         
        }
  }
          
}