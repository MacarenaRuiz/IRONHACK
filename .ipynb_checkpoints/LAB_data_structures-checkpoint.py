
#1. Define a list called products that contains the following items: "t-shirt", "mug", "hat", "book", "keychain".

products = ["t-shirt", "mug", "hat", "book", "keychain"]
#2. Create an empty dictionary called inventory.
inventory={}
#3. Ask the user to input the quantity of each product available in the inventory. 
product_inventory_mug=int(input('Please, insert the quantity for mug: '))
product_inventory_hat=int(input('Please, insert the quantity for hat: '))


#Use the product names from the products list as keys in the inventory dictionary and assign the respective quantities as values.

#4. Create an empty set called customer_orders.
#5. Ask the user to input the name of three products that a customer wants to order (from those in the products list, meaning three products out of "t-shirt", "mug", "hat", "book" or "keychain". Add each product name to the customer_orders set.
#6. Print the products in the customer_orders set.
#7. Calculate the following order statistics:
#Total Products Ordered: The total number of products in the customer_orders set.
#Percentage of Products Ordered: The percentage of products ordered compared to the total available products.
#Store these statistics in a tuple called order_status.
#8. Print the order statistics using the following format:
#Order Statistics:
#Total Products Ordered: <total_products_ordered>
#Percentage of Products Ordered: <percentage_ordered>% 
#9. Update the inventory by subtracting 1 from the quantity of each product. Modify the inventory dictionary accordingly.
#10. Print the updated inventory, displaying the quantity of each product on separate lines.