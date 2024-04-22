
# Testing
def main():
    import tensorflow as tf
    import pandas as pd
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import StandardScaler
    import matplotlib.pyplot as plt
    
    # Load dataset
    data = pd.read_csv('path_to_data.csv')
    
    # Preview the data
    print(data.head())

    # Feature scaling
    scaler = StandardScaler()
    data[['Size', 'Bedrooms', 'Bathrooms']] = scaler.fit_transform(data[['Size', 'Bedrooms', 'Bathrooms']])

    # Split data into features and target
    X = data[['Size', 'Bedrooms', 'Bathrooms']]
    y = data['Price']

    # Split data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Customizable model, which will be adjusted automatically or by the requested training
    layer_amount = [10,10,1]
    optimizer = 'adam'
    loss_function = 'mse'
    metrics = ['mae']
    activation_functions = ['relu','relu','output']
    input_shape = (3,)
    model_size = len(layer_amount)
    model_table = []
    model_table.append(tf.keras.layers.Dense(layer_amount[0],activation=activation_functions[0],input_shape=input_shape))
    for i in range(1,model_size):
        if activation_functions[i] == 'output':
            model_table.append(tf.keras.layers.Dense(layer_amount[i]))
        else:
            model_table.append(tf.keras.layers.Dense(layer_amount[i],activation=activation_functions[i]))

    model = tf.keras.Sequential(model_table)

    # Compile the model
    model.compile(optimizer=optimizer, loss=loss_function, metrics=metrics)

    # Model summary
    model.summary() 

    # Train the model
    history = model.fit(X_train, y_train, epochs=100, validation_split=0.1)


    # requirements numpy pandas tensorflow scikit-learn


    # Load dataset
    data = pd.read_csv('path_to_data.csv')

    # Preview the data
    print(data.head())

    # Feature scaling
    scaler = StandardScaler()
    data[['Size', 'Bedrooms', 'Bathrooms']] = scaler.fit_transform(data[['Size', 'Bedrooms', 'Bathrooms']])

    # Split data into features and target
    X = data[['Size', 'Bedrooms', 'Bathrooms']]
    y = data['Price']

    # Split data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


    # Build the model
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(10, activation='relu', input_shape=(3,)),  # 3 features: Size, Bedrooms, Bathrooms
        tf.keras.layers.Dense(10, activation='relu'),
        tf.keras.layers.Dense(1)  # Output layer: Predicted price
    ])

    # Compile the model
    model.compile(optimizer='adam', loss='mse', metrics=['mae'])

    # Model summary
    model.summary()

    history = model.fit(X_train, y_train, epochs=100, validation_split=0.1)

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