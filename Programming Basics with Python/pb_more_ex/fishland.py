mackerel_price = float(input())
sprinkle_price = float(input())

bonito_kg = float(input())
safrid_kg = float(input())
mussels_kg = int(input())
mussels_price = 7.50

bonito_price = mackerel_price + (mackerel_price * 0.60)
bonito_sum = bonito_kg * bonito_price
safrid_price = sprinkle_price + (sprinkle_price * 0.80)
safrid_sum = safrid_kg * safrid_price
mussels_sum = mussels_kg * mussels_price

total_sum = bonito_sum + safrid_sum + mussels_sum


print(f"{total_sum:.2f}")