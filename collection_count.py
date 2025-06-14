# Enter your code here. Read input from STDIN. Print output to STDOUT
import collections

 
shoe_count = int(input())

 
shoes_in_stock = collections.Counter(map(int, input().split()))

# Total revenue 
total_revenue = 0

# Read the number of customers
num_customers = int(input())

# Loop through each customer
for i in range(num_customers):
    requested_size, offered_price = map(int, input().split())
    
    # If the requested shoe size is available
    if shoes_in_stock[requested_size]:
        total_revenue += offered_price   
        shoes_in_stock[requested_size] -= 1   

print(total_revenue)
