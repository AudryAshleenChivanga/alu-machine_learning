# Regularization (mathematics)

Regularization is a technique used to prevent overfitting in machine learning models by adding constraints or penalties to the learning process. It ensures that the model generalizes well to unseen data.

## An Overview of Regularization Techniques in Deep Learning  
Regularization techniques help improve the generalization ability of deep learning models. Some common methods include:
- **L1 and L2 Regularization (Weight Decay)**
- **Dropout**
- **Early Stopping**
- **Data Augmentation**
- **Batch Normalization**

## L2 Regularization and Back-Propagation  
L2 regularization, also known as **Ridge Regression** or **weight decay**, adds a penalty term to the loss function that is proportional to the square of the model's weights:

\[
L_{reg} = \lambda \sum w^2
\]

This discourages large weights, preventing overfitting. During backpropagation, the gradients are adjusted to include this penalty, encouraging the model to learn smaller and more stable weights.

## Intuitions on L1 and L2 Regularization  
- **L1 Regularization (Lasso)** encourages sparsity by adding an absolute weight penalty:  
  \[
  L_{reg} = \lambda \sum |w|
  \]
  This can lead to feature selection by driving some weights to zero.
- **L2 Regularization (Ridge)** penalizes large weights and prevents extreme weight values.

### Key Differences:
| Feature       | L1 Regularization | L2 Regularization |
|--------------|------------------|------------------|
| Penalty Term | \( \sum |w| \) | \( \sum w^2 \) |
| Effect       | Leads to sparsity (some weights become zero) | Shrinks weights but keeps them nonzero |
| Feature Selection | Yes (eliminates less useful features) | No |

## Analysis of Dropout  
Dropout is a regularization technique that randomly deactivates neurons during training with a probability \( p \). This prevents the model from relying too much on specific neurons, leading to better generalization.

### How Dropout Works:
1. During training, neurons are randomly "dropped" (set to zero).
2. During inference, no neurons are dropped, but their outputs are scaled by \( 1 - p \).

### Advantages of Dropout:
- Reduces overfitting
- Makes the network more robust
- Acts as an ensemble learning technique

## Early Stopping  
Early stopping is a simple yet effective regularization technique that stops training when the validation loss starts increasing, indicating overfitting.

### How to use early stopping properly for training deep neural networks?  
1. Monitor validation loss during training.
2. Set a patience parameter (number of epochs to wait before stopping).
3. Stop training when the validation loss stops improving.

## Data Augmentation | How to use Deep Learning when you have Limited Data  
Data augmentation helps improve model performance by artificially increasing the dataset size using transformations such as:
- **Rotation**
- **Scaling**
- **Flipping**
- **Adding noise**
- **Color jittering**
