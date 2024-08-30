import pytz
from datetime import datetime, timedelta

# Get today's date at 12 AM UTC
utc_datetime = datetime.utcnow().replace(hour=12, minute=0, second=0, microsecond=0)
utc_datetime_str = utc_datetime.strftime("%Y-%m-%dT%H:%M:%S.%fZ")

# Specify the target time zone (Pacific Time Zone for California)
time_zone_str = "America/Los_Angeles"
target_time_zone = pytz.timezone(time_zone_str)

# Convert the UTC datetime to the specified local time zone
utc_datetime = datetime.strptime(utc_datetime_str, "%Y-%m-%dT%H:%M:%S.%fZ")
local_datetime = utc_datetime.replace(tzinfo=pytz.utc).astimezone(target_time_zone)

# Get the current time in the specified timezone
current_time = datetime.now(target_time_zone)

# Add 7 hours to the current time and save as time2
time2 = current_time + timedelta(hours=7)

# Get the UTC offset for the current time
offset_hours = current_time.utcoffset().total_seconds() / 3600

# Print the results
print("UTC Datetime:", utc_datetime)
print("Local Datetime in", time_zone_str, ":", local_datetime)
print("Current Time in", time_zone_str, ":", current_time)
print("Time2 (Current Time + 7 hours):", time2)
print("UTC Offset:", offset_hours, "hours")
