import openai

# Set your OpenAI API key
openai.api_key = 'your-api-key'


def extract_features(post: str):
    prompt = f"""
You are an intelligent assistant that extracts structured information from real estate rental posts.
Given the following post:

---
{post}
---

Extract the information in this structured format (if not available, return "not mentioned"):

Output :
Contact - 
Flat - 
Flat name - 
male/female/family - 
Rent - 
Type - 
has pool - 
has gym - 
power backups - 
vegetarian requirement - 
smoking allowed - 
Availability - 
balcony - 
bathroom - 
amenities - (comma separated list)

Other notes - (any useful info not captured above)
"""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )

    return response['choices'][0]['message']['content']


# Example usage
post = """3BHK Gated Community Semi Furnished Flat In Kondapur Shilpa Park Family or Female bachelor Immediately Available 
With one balcony & Attached Bathroom
Rent_55k + maintenance 
Amenities 3A/c split modular kitchen chimney wardrobe geyser fan light power backups water facility car parking lift with club house swimming pool gym badminton court supermarket salon etc more details contact me 9603212336"""

result = extract_features(post)
print(result)
