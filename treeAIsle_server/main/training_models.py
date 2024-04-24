
# Testing
def main():
    # import tensorflow as tf
    import pandas as pd
    import numpy as np
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import StandardScaler
    from sklearn.datasets import fetch_california_housing
    import matplotlib.pyplot as plt
    import tensorflow as tf

    # Load the California housing data
    data = fetch_california_housing()
    X = pd.DataFrame(data.data, columns=data.feature_names)
    y = data.target

    # Standardize the features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Split data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

    layers_sizes = [10,10,1]
    optimizer = 'adam'
    loss_function = 'mean_squared_error'
    metrics = ['mean_absolute_error']
    activation_functions = ['relu','relu','output']
    
    # Define a TensorFlow model
    model_table = []
    model_table.append(tf.keras.layers.Dense(layers_sizes[0],activation=activation_functions[0],input_shape=(X_train.shape[1],)))
    for i in range(1,len(layers_sizes)):
        if activation_functions[i] == 'output':
            model_table.append(tf.keras.layers.Dense(layers_sizes[i]))
        else:
            model_table.append(tf.keras.layers.Dense(layers_sizes[i],activation=activation_functions[i]))
    model = tf.keras.Sequential(model_table)    

    # Compile the model
    model.compile(optimizer=optimizer, loss=loss_function, metrics=metrics)

    # Model summary
    model.summary()

    # Train the model
    history = model.fit(X_train, y_train, epochs=10, validation_split=0.1)

    # Evaluate the model
    test_loss, test_mae = model.evaluate(X_test, y_test)
    print(f"Test Loss: {test_loss}, Test MAE: {test_mae}")

    # Plot training & validation loss values
    plt.plot(history.history['loss'], label='Train')
    plt.plot(history.history['val_loss'], label='Validation')
    plt.title('Model loss')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.legend(loc='upper right')
    plt.show()
    
if __name__ == "__main__":
    print("Model testing")
    main()
    
# An alternative to consider
# 
# from tensorflow import keras
# class MyModel(keras.Model):
#     def __init__(self):
#         super().__init__()
#         self.dense1 = keras.layers.Dense(32, activation="relu")
#         self.dense2 = keras.layers.Dense(5, activation="softmax")
#         self.dropout = keras.layers.Dropout(0.5)

#     def call(self, inputs, training=False):
#         x = self.dense1(inputs)
#         x = self.dropout(x, training=training)
#         return self.dense2(x)

# model = MyModel()
class Model():
    def __init__(self,model_type='adam',layers_sizes=[10,10,1],layers_functions=['relu','relu','output'],metrics=['mean_absolute_error'],loss_function = 'mean_squared_error',activation_functions = ['relu','relu','output'],library='tensorflow'):
        self.model_type = model_type
        self.model = None
        self.library = library
        self.layers_sizes = layers_sizes
        self.layer_functions = layers_functions
        self.loss_function = loss_function
        self.metrics = metrics
        self.activation_functions = activation_functions
    def train(self,trainingDataset, resultDataset, hypervaules):
        if self.library == 'tensorflow':
            try:
                import pandas as pd
                import numpy as np
                from sklearn.model_selection import train_test_split
                from sklearn.preprocessing import StandardScaler
                from sklearn.datasets import fetch_california_housing
                import matplotlib.pyplot as plt
                import tensorflow as tf
                data = fetch_california_housing()
                X = pd.DataFrame(data.data, columns=data.feature_names)
                y = data.target
                scaler = StandardScaler()
                # X_scaled = scaler.fit_transform(X)
                
                # # This happens in the chain, as the chain saves the given dataset
                # X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

                layers_sizes = self.layers_sizes
                optimizer = self.model_type
                metrics = self.metrics
                layer_functions = self.layer_functions
                activation_functions = self.activation_functions
                loss_function = self.loss_function
                
                # Define a TensorFlow model
                model_table = []
                model_table.append(tf.keras.layers.Dense(layers_sizes[0],activation=activation_functions[0],input_shape=(X_train.shape[1],)))
                for i in range(1,len(layers_sizes)):
                    if activation_functions[i] == 'output':
                        model_table.append(tf.keras.layers.Dense(layers_sizes[i]))
                    else:
                        model_table.append(tf.keras.layers.Dense(layers_sizes[i],activation=layer_functions[i]))
                self.model = tf.keras.Sequential(model_table)

                self.model.compile(optimizer=optimizer, loss=loss_function, metrics=metrics)
                self.model.summary()
                history = self.model.fit(trainingDataset, resultDataset, epochs=10, validation_split=0.1)

            except Exception as e:
                print(f"An exception occurred during model training {e}")
    def get_performace(self,model,testData,testResult):
        try:
            # Evaluate the model    
            if self.model_type == 'tensorflow':
                import tensorflow as tf
                test_loss, test_mae = model.evaluate(testData, testResult)
            else: # As the project grows, we can add more models here, however the whole structure seems a bit inefficient
                print("Unknown model")
                raise ValueError("Unknown models")
        except Exception as e:
            print(f"An exception occurred during model verification {e}")