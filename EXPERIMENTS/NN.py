import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

(X_train, y_train),(X_test, y_test)=tf.keras.datasets.mnist.load_data()
X_train=X_train.reshape(-1,784).astype("float32") / 255.0
X_test=X_test.reshape(-1,784).astype("float32") / 255.0

input_size=784
hidden_size=128
output_size=10
epochs=50
batch_size=128 
learning_rate=0.01

experiments={
    "zero":(tf.keras.initializers.Zeros(),"sigmoid"), 
    "Random":(tf.keras.initializers.RandomNormal(),"sigmoid"),
    "Xavier+Normal":(tf.keras.initializers.GlorotNormal(),"sigmoid"),
    "Xavier+Uniform":(tf.keras.initializers.GlorotUniform(),"tanh"), 
    "He+Normal_relu":(tf.keras.initializers.HeNormal(),"relu"), 
    "He+Normal_LeakyReLu":(tf.keras.initializers.HeNormal(),"LeakyReLu") 
}

results={}
accuracy_history={}
loss_history={}

for name,(initializer, activation) in experiments.items(): 
    print(f"\nRunning experiment: {name}")
    tf.keras.utils.set_random_seed(42) 

    model=tf.keras.Sequential() 
    model.add(tf.keras.layers.InputLayer(input_shape=(input_size,))) 

    if activation=="LeakyReLu":
        model.add(tf.keras.layers.Dense(hidden_size, kernel_initializer=initializer)) 
        model.add(tf.keras.layers.LeakyReLU(negative_slope=0.01))
    else:
        model.add(tf.keras.layers.Dense(hidden_size, activation=activation, kernel_initializer=initializer)) 

    model.add(tf.keras.layers.Dense(output_size, activation="softmax")) 

    model.compile(optimizer=tf.keras.optimizers.SGD(learning_rate=learning_rate),
                  loss="SparseCategoricalCrossentropy", 
                  metrics=["accuracy"]) 

    history=model.fit(X_train,y_train,epochs=epochs,batch_size=batch_size,verbose=0)
    train_loss,train_acc=model.evaluate(X_train,y_train,verbose=0)
    test_loss,test_acc=model.evaluate(X_test,y_test,verbose=0)

    results[name]=[train_acc, test_acc, train_loss, test_loss] 
    accuracy_history[name]=history.history["accuracy"]
    loss_history[name]=history.history["loss"]

    print(f"Train Accuracy: {train_acc:.4f}, Test Accuracy: {test_acc:.4f}")
    print(f"Train Loss: {train_loss:.4f}, Test Loss: {test_loss:.4f}")

print("\n"+"="*80)
print("TABLE 1: ACCURACY")
print("="*80)

print(f"{'Method':35}{'Training':15}{'Testing':15}")
print("-"*80)

for name,  values in results.items():
    print(f"{name:35}{values[0]:<15.4f}{values[1]:.4f}")


print("\n"+"="*80)
print("TABLE 2:LOSS")
print("="*80)

print(f"{'Method':35}{'Training':15}{'Testing':15}")
print("-"*80)

for name,  values in results.items():
    print(f"{name:35}{values[2]:<15.4f}{values[3]:.4f}")

plt.figure(figsize=(10,6))
for name in experiments:
    plt.plot(range(1,epochs+1),
             accuracy_history[name],label=name)
plt.xlabel("Epoch")
plt.ylabel("Training Accuracy")
plt.title("MNIST _ Training Accuracy")
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()
