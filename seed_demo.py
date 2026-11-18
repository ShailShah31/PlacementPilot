"""Populate PlacementPilot with clearly fictional demo data for screenshots."""
from app import Store

store = Store()
if store.list_applications() or store.list_skills() or store.list_goals():
    raise SystemExit("Database is not empty. Refusing to mix demo data with your records.")

for item in [
    {"company":"Atlassian","role":"Software Engineer Intern","status":"Applied","applied_date":"2026-11-12","deadline":"2026-11-28","location":"Bengaluru","job_url":"https://www.atlassian.com/","notes":"Fictional demo entry — replace with a real application."},
    {"company":"Razorpay","role":"Backend Developer Intern","status":"Online Assessment","applied_date":"2026-11-08","deadline":"2026-11-22","location":"Remote","job_url":"https://razorpay.com/","notes":"Fictional demo entry."},
    {"company":"Adobe","role":"Software Development Intern","status":"Wishlist","deadline":"2026-12-05","location":"Noida","job_url":"https://www.adobe.com/","notes":"Fictional demo entry."},
    {"company":"Zoho","role":"Developer Intern","status":"Interview","applied_date":"2026-10-30","deadline":"2026-11-25","location":"Chennai","job_url":"https://www.zoho.com/","notes":"Fictional demo entry."},
]: store.save_application(item)
for item in [
    {"name":"Java","category":"Programming","level":3,"target_level":5},
    {"name":"Python","category":"Programming","level":4,"target_level":5},
    {"name":"Data Structures & Algorithms","category":"Core CS","level":2,"target_level":5},
    {"name":"HTML & CSS","category":"Web Development","level":4,"target_level":5},
    {"name":"SQL","category":"Database","level":2,"target_level":4},
]: store.save_skill(item)
for item in [
    {"title":"Solve 50 array and string problems","target_date":"2026-11-30"},
    {"title":"Build and publish one full-stack project","target_date":"2026-12-10","completed":True},
    {"title":"Revise DBMS fundamentals","target_date":"2026-12-05"},
]: store.save_goal(item)
print("Demo data added. All company names and records are fictional examples.")
