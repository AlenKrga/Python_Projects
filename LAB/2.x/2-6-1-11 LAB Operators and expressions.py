hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# Write your code here.

# Conver time to minutes 
given_time_in_minutes = (hour * 60)+ mins

# duration added to time
total_time_in_minutes = given_time_in_minutes + dura

final_hours = total_time_in_minutes // 60
final_minutes = total_time_in_minutes % 60

print(f"final time: {final_hours} : {final_minutes}")