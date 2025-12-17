# Projet Data Analyst – Pipeline Marketing

## Contexte

Vous êtes data analyst dans une entreprise de e-commerce. Les données marketing sont collectées de différentes sources et arrivent dans une base de données brute avec de nombreuses erreurs et valeurs manquantes.

**Votre mission :** construire un pipeline de données pour nettoyer et analyser ces informations.

---

## Architecture

Le projet suit une architecture **Medallion** en 3 couches :

* **Bronze** : Données brutes (déjà fourni)
* **Silver** : À construire – Nettoyage et anonymisation
* **Gold** : À construire – Agrégations et analytics

---

## Données fournies (Bronze)

La base MongoDB `bronze_db` contient 3 collections :

### customers (5000 documents)

```json
{
  "customer_id": "CUST12345",
  "first_name": "Jean",          
  "last_name": "Dupont",         
  "email": "jean@email.com",     
  "phone": "+33612345678",       
  "age": 35,                     
  "country": "France",          
  "city": "Paris",              
  "gender": "M",                
  "marketing_consent": true      
}
```

### transactions (15000 documents)

```json
{
  "transaction_id": "TXN98765",
  "customer_id": "CUST12345",    
  "product": "Laptop",           
  "amount": 999.99,              
  "quantity": 1,                 
  "payment_method": "Card",     
  "discount_applied": 50.00,     
  "shipping_cost": 10.00,        
  "timestamp": "ISODate(...)"
}
```

### campaigns (200 documents)

```json
{
  "campaign_id": "CAMP123",
  "campaign_name": "Summer Sale", 
  "campaign_type": "Email",       
  "budget": 10000.00,             
  "spend": 8500.00,               
  "impressions": 100000,          
  "clicks": 5000,                 
  "conversions": 250,             
  "start_date": "ISODate(...)"
}
```

---

## Mission 1 : Construire la couche SILVER

### Objectif

Créer un script Python qui lit les données Bronze, les nettoie et les enregistre dans MongoDB `silver_db`.

### Traitements à effectuer

#### Clients

* Créer un champ `full_name` à partir de `first_name` et `last_name`
* Anonymiser `email` et `phone` (hash MD5)
* Remplacer les valeurs manquantes par des valeurs par défaut appropriées

#### Transactions

* Calculer `total_amount = amount - discount_applied + shipping_cost`
* Gérer les valeurs manquantes

#### Campagnes

Calculer les KPIs marketing :

* `CTR = (clicks / impressions) * 100`
* `conversion_rate = (conversions / clicks) * 100`
* `CPC = spend / clicks`
* `CPA = spend / conversions`
* `ROI = ((budget - spend) / budget) * 100`

➡️ Gérer les divisions par zéro.

### Livrable

* Fichier `processor.py`

---

## Mission 2 : Construire la couche GOLD

### Objectif

Créer un script Python qui agrège les données Silver et les exporte vers PostgreSQL `gold_db`.

### Tables à créer

### 1. customer_metrics

Pour chaque client ayant au moins une transaction :

* `customer_id`, `full_name`, `country`, `city`
* `total_transactions`
* `total_spent`
* `avg_transaction_amount`
* `first_purchase_date`, `last_purchase_date`

### 2. product_performance

Pour chaque produit :

* `product`
* `total_sales`
* `total_revenue`
* `avg_price`
* `unique_customers`

### 3. campaign_performance

Pour chaque campagne :

* `campaign_id`, `campaign_name`, `campaign_type`
* `total_impressions`, `total_clicks`, `total_conversions`
* `avg_ctr`, `avg_conversion_rate`, `avg_cpc`, `avg_cpa`
* `roi`, `status`

### 4. monthly_revenue

Revenus agrégés par mois :

* `month` (DATE)
* `total_revenue`, `total_transactions`
* `unique_customers`, `avg_transaction_value`

### 5. country_statistics

Statistiques par pays :

* `country`
* `total_customers`, `total_revenue`
* `avg_customer_value`
* `marketing_consent_rate`

### Livrable

* Fichier `aggregator.py`

---

## Environnement technique

### Bases de données

* **MongoDB** : `mongodb://admin:admin123@localhost:27017`

  * Bronze : `bronze_db`
  * Silver : `silver_db`

* **PostgreSQL** : `postgresql://analyst:analyst123@localhost:5432/gold_db`

  * Gold : `gold_db`

### Lancer l'environnement

```bash
docker-compose up -d
```

### Générer les données Bronze

```bash
docker-compose up bronze_generator
```

---

## Questions Business à résoudre

1. Qui sont les 10 meilleurs clients ?
2. Quel produit génère le plus de revenus ?
3. Quelle campagne a le meilleur ROI ?
4. Quelle est l'évolution des ventes mois par mois ?
5. Quel pays génère le plus de revenus ?

➡️ Écrire les requêtes SQL correspondantes.

---

**Bon courage !**
