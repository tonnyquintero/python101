import csv

new_product = {
    'name': 'Wireless Charger',
    'price': 75,
    'quantity': 100,
    'brand': 'ChargerMAster',
    'category': 'Accessories',
    'entry_date': '2024-07-01'
}

with open('products.csv', mode='a', newline='') as file:
    csv_writer = csv.DictWriter(file, fieldnames= new_product.keys())
    csv_writer.writerow(new_product)