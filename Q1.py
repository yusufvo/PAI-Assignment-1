from itertools import combinations
transactionLog = [
  {'orderId': '1001', 'customerId': 'cust_Ahmed', 'productId': 'prod_10'},
  {'orderId': '1001', 'customerId': 'cust_Ahmed', 'productId': 'prod_12'},
  {'orderId': '1002', 'customerId': 'cust_Bisma', 'productId': 'prod_10'},
  {'orderId': '1002', 'customerId': 'cust_Bisma', 'productId': 'prod_15'},
  {'orderId': '1003', 'customerId': 'cust_Ahmed', 'productId': 'prod_15'},
  {'orderId': '1004', 'customerId': 'cust_Faisal', 'productId': 'prod_12'},
  {'orderId': '1004', 'customerId': 'cust_Faisal', 'productId': 'prod_10'},
]

productCatalog = {
  'prod_10': 'Wireless Mouse',
  'prod_12': 'Keyboard',
  'prod_15': 'USB-C Hub',
}
# 1. Transform Data
def processtransactions(transactionLog):
    uniqueproducts={}
    for i in transactionLog:
        customerID=i["customerId"]
        productId=i["productId"]
        if customerID not in uniqueproducts:
            uniqueproducts[customerID]= {productId}
        else:
            uniqueproducts[customerID].add(productId)
    return uniqueproducts
print(processtransactions(transactionLog))
# 2. Find Pairs
def findFrequentPairs(transactionLog):
    orders = {}
    for transaction in transactionLog:
        order = transaction['orderId']
        product = transaction['productId']
        
        if order not in orders:
            orders[order] = {product}
        else:
            orders[order].add(product)
            
    pair_counts = {}
    
    for product_set in orders.values():
        
        if len(product_set) < 2:
            continue
            
        sorted_products = sorted(list(product_set))
        
        pairs = combinations(sorted_products, 2)
        
        for pair in pairs:
            pair_counts[pair] = pair_counts.get(pair, 0) + 1
            
    return pair_counts

frequent_pairs = findFrequentPairs(transactionLog)
print("--- Frequent Pairs (by Order) ---")
print(frequent_pairs)

# 3. Recommendation
def getRecommendations(targetProductId, frequentPairs):
    recommendations = []
    
    for pair, count in frequentPairs.items():
        if targetProductId in pair:
            other_product = ''
            if pair[0] == targetProductId:
                other_product = pair[1]
            else:
                other_product = pair[0]
                
            recommendations.append( (other_product, count) )
            
    recommendations.sort(key=lambda x: x[1], reverse=True)
    
    return recommendations
# 4. Report Generqtion
def generateReport(targetProductId, recommendations, catalog):
    print("-------------------------------------------------")
    print(f"Product Recommendation Report for: {catalog[targetProductId]}")
    print("-------------------------------------------------")
    
    if not recommendations:
        print("No recommendations found.")
        return

    ranks = [rank for rank, _ in enumerate(recommendations, start=1)]
    prod_ids = [prod_id for prod_id, count in recommendations]
    counts = [count for prod_id, count in recommendations]
    prod_names = [catalog[pid] for pid in prod_ids]

    for rank, name, count in zip(ranks, prod_names, counts):
        print(f"  {rank}. {name} (Purchased together {count} times)")


frequent_pairs = findFrequentPairs(transactionLog)
target_product = 'prod_10'
recommendations = getRecommendations(target_product, frequent_pairs)
generateReport(target_product, recommendations, productCatalog)

target_product_2 = 'prod_11'
recommendations_2 = getRecommendations(target_product_2, frequent_pairs)
generateReport(target_product_2, recommendations_2, productCatalog)