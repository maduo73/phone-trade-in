# Used Phone Trade-in Dashboard

## Audience and decision
This dashboard is for a trade-in platform's pricing and operations manager. It supports decisions about which phone groups deserve closer offer review and how resale values vary by tier, screen condition, brand, and time since launch.

## What the dashboard shows
The app displays the phone count, median and mean resale price, median price by tier, price against days since launch, and median price by screen condition. A brand filter lets the manager examine segments without hiding the overall decision context.

## What I left out and why
I left out individual phone-level recommendations, causal claims, and detailed model diagnostics. The supplied assignment data are simulated, so presenting the dashboard as a production pricing authority could mislead a decision-maker. Instead, this is a descriptive monitoring view that supports investigation rather than automatic offers.

## Refresh cadence
Refresh after each new quality-checked resale cohort, review the dashboard monthly, and investigate changes in device mix or price patterns before using a model for offers. Replace simulated coursework data with approved operational data before any business use.

## Run locally
Install dependencies with `pip install -r requirements.txt`, then run `streamlit run app.py`. Upload `phone_trade_in.csv` in the app.

## Deployment links
After creating your own GitHub repository and deploying through your own Streamlit Cloud account, add the repository and app URLs here.
