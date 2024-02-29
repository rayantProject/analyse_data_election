# Projet MSPR
import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Chargement des données depuis le fichier CSV
data = pd.read_csv(r"C:\Users\ferga\Downloads\merged.csv")

# Effacer les elements vide
data.dropna(inplace=True)

# Calcul de l'age moyen
data['moyenne_age'] = (data['population_15_29'] * 22 + data['population_30_44'] * 37 + data['population_45_59'] * 52 + data['population_60_74'] * 67 + data['population_75_89'] * 82) / (data['population_15_29'] + data['population_30_44'] + data['population_45_59'] + data['population_60_74'] + data['population_75_89'])

# Calcul du rapport homme-femme
data['rapport_homme_femme'] = data['population_homme'] / data['population_femme']

# Sélection des colonnes pour les paramètres d'entrée et de sortie
X = data[['nb_crimes_5ans', 'salaire_net_horaire_moyen', 'taux_pauvrete', 'mediane_niveau_vie', 'moyenne_age', 'rapport_homme_femme']]
y = data['vainqueur_id']

# Nettoyage des données
X = X.apply(pd.to_numeric, errors='coerce')
X.fillna(X.median(), inplace=True)

# Normalisation des données
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Séparation des données en ensembles de train et de test
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Définition du modele (reseau de neurones)
model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(len(y.unique()), activation='softmax')  # Activation softmax car vainqueur_id est catégoriel
])



# Compilation du modele
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Entrainement du modele
model.fit(X_train, y_train, epochs=100, batch_size=32, validation_split=0.1)

# Évaluation du modele sur l'ensemble de test
loss, accuracy = model.evaluate(X_test, y_test)
print("Loss sur l'ensemble de test:", loss)
print("Accuracy sur l'ensemble de test:", accuracy)

# Utilisation du modèle pour faire des prédictions
predictions = model.predict(X_test)

# Affichage des prédictions
for i in range(10):
    print("Prédiction:", np.argmax(predictions[i]), " - Réel:", y_test.iloc[i])
