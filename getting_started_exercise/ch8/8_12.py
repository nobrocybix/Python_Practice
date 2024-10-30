def sandwich(*ingredients):
    print("\nMaking a sandwich with the following ingredients:")
    for ingredient in ingredients:
        print("- " + ingredient)

sandwich('lettuce', 'tomato', 'bread', 'meat', 'cheese')