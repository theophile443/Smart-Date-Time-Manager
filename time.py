# Import modules
from datetime import datetime
from dateutil import parser
from dateutil.relativedelta import relativedelta
import arrow
import pendulum

# 1. Current Date & Time (datetime)
print("=== CURRENT DATE & TIME ===")
now = datetime.now()
print("Datetime module:", now)

# 2. Parse Date (dateutil)
print("\n=== DATE PARSING ===")
date_input = input("Enter a date (e.g., 2026-05-01 or '1 May 2026'): ")
parsed_date = parser.parse(date_input)
print("Parsed date:", parsed_date)

# 3. Date Difference (dateutil)
print("\n=== DATE DIFFERENCE ===")
future_date = parsed_date + relativedelta(days=30)
print("Date after 30 days:", future_date)

# 4. Arrow Module Usage
print("\n=== ARROW MODULE ===")
arrow_now = arrow.now()
print("Current time (Arrow):", arrow_now)

formatted = arrow_now.format('YYYY-MM-DD HH:mm:ss')
print("Formatted (Arrow):", formatted)

# Timezone conversion
utc_time = arrow_now.to('UTC')
print("Converted to UTC:", utc_time)

# 5. Pendulum Module Usage
print("\n=== PENDULUM MODULE ===")
pendulum_now = pendulum.now()
print("Current time (Pendulum):", pendulum_now)

# Timezone example (Kigali)
kigali_time = pendulum.now('Africa/Kigali')
print("Kigali time:", kigali_time)

# Difference calculation
tomorrow = pendulum_now.add(days=1)
diff = tomorrow - pendulum_now
print("Difference (in hours):", diff.in_hours())

# 6. Combine Everything
print("\n=== FINAL SUMMARY ===")
print(f"""
Original input date: {parsed_date}
After 30 days: {future_date}
Current local time: {now}
Arrow UTC time: {utc_time}
Kigali time (Pendulum): {kigali_time}
""")